#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extrair_n3.py — extrator determinístico do Modelo Funcional Canônico (PFC 1.0) a partir
da estrutura de documentação N3 do siesa-engine (features em modules/**/f-*.md).

Lê, de cada N3: front-matter (id, entidade, endpoints, error_codes, estado), `## Superfície`,
`## Campos`, `## Colunas do resultado`, `## Dados lidos e gravados`, `## Métricas de tamanho`
com `### Memória de cálculo` (ALR por processo elementar), `## API` e `## Eventos`, e aplica
as regras de mapeamento do capítulo 10 (RM-01 a RM-08). Toda movimentação cita a seção de
origem como evidência (`DOC:<arquivo>#<seção>`), verificável por `pfc.py auditar`.

Uso:
  python3 extrair_n3.py <raiz-da-instancia> [-o modelo.json] [--escopo PREFIXO ...]
                        [--git] [--antes <raiz-da-versao-anterior>]
  --escopo  limita às features cujo id começa pelo prefixo (ex.: ADM-USR, DEM)
  --git     atribui o modo de produção por feature a partir do histórico git (RP-01, heurística)
  --antes   marca como 'alterado' todo movimento cuja seção de origem mudou em relação à versão
            anterior da instância (RD-01, aproximação por seção)
"""
import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata

VERSAO_EXTRATOR = "1.0"
UF = {
    "pessoa": {"id": "UF-PESSOA", "nome": "Usuário da conta (tela)", "tipo": "pessoa"},
    "sistema": {"id": "UF-SISTEMA", "nome": "Sistema externo, webhook ou orquestrador de etapas", "tipo": "sistema"},
    "relogio": {"id": "UF-RELOGIO", "nome": "Agendador", "tipo": "relogio"},
}
ACESSORIO = re.compile(r"\((combobox|card|menu|tela|lista)\)", re.I)


def norm(t):
    t = unicodedata.normalize("NFKD", str(t or ""))
    return " ".join("".join(c for c in t if not unicodedata.combining(c)).lower().split())


# ---------------------------------------------------------------------------
# leitura do N3
# ---------------------------------------------------------------------------

def front_matter(linhas):
    """Subconjunto de YAML: chave: valor, chave: [] e listas '  - item'. Blocos aninhados são ignorados."""
    fm, i = {}, 0
    while i < len(linhas) and linhas[i].strip() != "---":
        i += 1
    i += 1
    chave = None
    while i < len(linhas) and linhas[i].strip() != "---":
        l = linhas[i]
        m = re.match(r"^([a-z_]+):\s*(.*)$", l)
        if m:
            chave, val = m.group(1), m.group(2).strip()
            if val == "[]":
                fm[chave] = []
            elif val == "":
                fm[chave] = []
            else:
                fm[chave] = val.strip('"')
        elif chave and re.match(r"^\s+-\s+", l) and isinstance(fm.get(chave), list):
            fm[chave].append(l.split("-", 1)[1].strip().strip('"'))
        i += 1
    return fm, i + 1


def secoes(linhas, inicio):
    """{titulo: texto} para cada '## Título' (fora de blocos de código)."""
    out, atual, buf, fence = {}, None, [], False
    titulo_doc = ""
    for l in linhas[inicio:]:
        if l.startswith("```"):
            fence = not fence
        if not fence and l.startswith("# ") and not titulo_doc:
            titulo_doc = l[2:].strip()
        if not fence and l.startswith("## "):
            if atual is not None:
                out[atual] = "\n".join(buf)
            atual, buf = l[3:].strip(), []
            continue
        buf.append(l)
    if atual is not None:
        out[atual] = "\n".join(buf)
    return titulo_doc, out


def tabelas(texto):
    """Todas as tabelas markdown do texto como (cabecalho, linhas)."""
    out, cab, corpo = [], None, []
    for l in texto.splitlines():
        if not l.strip().startswith("|"):
            if cab is not None:
                out.append((cab, corpo))
                cab, corpo = None, []
            continue
        if re.fullmatch(r"\|[\s\-:|]+\|", l.strip()):
            continue
        cels = [c.strip() for c in l.strip().strip("|").split("|")]
        if cab is None:
            cab = cels
        else:
            corpo.append(cels)
    if cab is not None:
        out.append((cab, corpo))
    return out


def coluna(cab, *nomes):
    for i, c in enumerate(cab):
        for n in nomes:
            if re.fullmatch(n, norm(c)):
                return i
    return -1


def blocos_json(texto):
    out = []
    for m in re.finditer(r"```json\s*(\{.*?\})\s*```", texto, re.S):
        try:
            out.append(json.loads(m.group(1)))
        except json.JSONDecodeError:
            pass
    return out


EXTERNOS = (("github", "GitHub"), ("google", "Identidade Google"))


def limpar_entidade(nome):
    nome = re.sub(r"^(ALI|AIE)\s+", "", nome.strip().strip("`*"))
    nome = re.sub(r"\s*\((AIE|ALI)\)\s*$", "", nome).strip()
    for chave, canonico in EXTERNOS:          # sistemas externos: um nome só, qualquer grafia
        if chave in norm(nome):
            return canonico
    return nome


# ---------------------------------------------------------------------------
# desfechos (RM-06): um por código de erro de negócio da tabela de erros da ## API
# ---------------------------------------------------------------------------

CODIGOS_TECNICOS = re.compile(r"^(AUTH_|INTERNAL|RATE_|SERVICE_UNAVAILABLE|TIMEOUT)", re.I)
SEPARADORES_CODIGO = re.compile(r"\s*[·,/]\s*|\s+ou\s+")
SEPARADORES_CAUSA = re.compile(r"\s*/\s*|\s+ou\s+")


def desfechos_n3(sec, fm, ev):
    """RM-06: um desfecho por código de erro de negócio distinto na tabela de erros de ## API, mais
    os códigos do front-matter sem linha na tabela. Célula com vários códigos ("A · B", situação
    "x / y") vale um desfecho por código. Códigos técnicos de autenticação e infraestrutura ficam
    fora (RI-10). O desfecho principal não é listado (RI-12)."""
    desfechos, vistos = [], set()

    def registrar(codigo, descricao):
        if codigo in vistos:
            return
        vistos.add(codigo)
        desfechos.append({"id": codigo, "descricao": (descricao or "recusa ou erro de negócio")[:120],
                          "tipo": "recusa", "evidencia": [ev("API")]})

    for cab, corpo in tabelas(sec.get("API", "")):
        ic, isit = coluna(cab, "code", "codigo", "código"), coluna(cab, "situacao", "situação", "quando")
        if ic < 0 or coluna(cab, "http") < 0:
            continue
        for r in corpo:
            if ic >= len(r):
                continue
            cel = re.sub(r"[`*⚠️]", "", r[ic]).split("(")[0]
            codigos = [c.strip() for c in SEPARADORES_CODIGO.split(cel) if c.strip() and not CODIGOS_TECNICOS.match(c.strip())]
            situ = r[isit].strip() if 0 <= isit < len(r) else ""
            causas = [x.strip() for x in SEPARADORES_CAUSA.split(situ) if x.strip()]
            for k, c in enumerate(codigos):
                registrar(c, causas[k] if len(codigos) > 1 and len(causas) == len(codigos) else situ)
    for c in fm.get("error_codes") or []:
        c = str(c).strip()
        if c and not CODIGOS_TECNICOS.match(c):
            registrar(c, "")
    return desfechos


# ---------------------------------------------------------------------------
# mapeamento N3 -> processos e movimentos (RM-01 a RM-08)
# ---------------------------------------------------------------------------

def extrair_feature(caminho, raiz):
    rel = os.path.relpath(caminho, raiz).replace(os.sep, "/")
    with open(caminho, encoding="utf-8") as f:
        linhas = f.read().splitlines()
    fm, ini = front_matter(linhas)
    titulo, sec = secoes(linhas, ini)
    fid = fm.get("id") or os.path.basename(caminho)
    principal = limpar_entidade(fm.get("entidade") or "") or "Entidade"
    ev = lambda s: f"DOC:{rel}#{s}"

    # RM-01 disparador: superfície e eventos consumidos
    superficie = norm(sec.get("Superfície", ""))
    consumidos = [c for cab, corpo in tabelas(sec.get("Eventos", "").split("### Consumidos")[-1]) for c in corpo]
    endpoints = fm.get("endpoints") if isinstance(fm.get("endpoints"), list) else []
    api = sec.get("API", "")
    linha_sup = (sec.get("Superfície", "").strip().splitlines() or ["ação em tela"])[0].strip("* ").strip()
    if superficie.startswith(("acao em tela", "tela propria")) or endpoints and not consumidos:
        uf, evento = "pessoa", linha_sup
    elif "webhook" in norm(api):
        uf, evento = "sistema", "chamada recebida de sistema externo (webhook)"
    elif consumidos:
        uf, evento = "sistema", f"evento consumido: {consumidos[0][0]}"
    elif re.search(r"\b(agendad|periodic|diari|cron)", norm(api)):
        uf, evento = "relogio", "execução agendada"
    else:
        uf, evento = "pessoa", linha_sup

    # RM-02 entradas: ## Campos (coluna Entidade; seleção/lista vira R+X da entidade de origem)
    entradas, selecoes = {}, set()
    for cab, corpo in tabelas(sec.get("Campos", "")):
        ic, ie, ip, it = coluna(cab, "label po", "campo"), coluna(cab, "entidade"), coluna(cab, "preenchimento"), coluna(cab, "tipo")
        for r in corpo:
            if ic < 0 or len(r) <= max(ic, 0):
                continue
            preench = norm(r[ip]) if 0 <= ip < len(r) else "entrada do usuario"
            if "entrada" not in preench and "query" not in preench and "body" not in preench:
                continue
            ent = limpar_entidade(r[ie]) if 0 <= ie < len(r) else ""
            tipo = norm(r[it]) if 0 <= it < len(r) else ""
            if not ent or norm(ent) in ("—", "-", "dado de codigo", "n/a"):
                ent = principal
            if ent != principal and ("lista" in tipo or "selec" in tipo):
                selecoes.add(ent)          # RM-02 b: opções carregadas de outra entidade
                entradas.setdefault(principal, set()).add(r[ic])
            else:
                entradas.setdefault(ent, set()).add(r[ic])

    # RM-03 leituras e gravações: ## Dados lidos e gravados (quando existe)
    le, grava = set(), set()
    for cab, corpo in tabelas(sec.get("Dados lidos e gravados", "")):
        ie, ip = coluna(cab, "entidade"), coluna(cab, "papel")
        for r in corpo:
            if ie < 0 or ip < 0 or len(r) <= max(ie, ip):
                continue
            ent, papel = limpar_entidade(r[ie]), norm(r[ip])
            if "le" in papel.split() or papel.startswith("le"):
                le.add(ent)
            if "grava" in papel:
                grava.add(ent)

    # RM-04 processos elementares e ALR: ## Métricas de tamanho + memória de cálculo
    metricas = sec.get("Métricas de tamanho", "")
    pes = []
    for cab, corpo in tabelas(metricas.split("### Memória")[0]):
        inome, ipapel, itipo, ipf = coluna(cab, "funcao de transacao", "processo elementar"), coluna(cab, "papel"), coluna(cab, "tipo"), coluna(cab, "pf")
        if inome < 0 or itipo < 0:
            continue
        for r in corpo:
            nome = r[inome].strip("* ")
            papel = norm(r[ipapel]) if 0 <= ipapel < len(r) else ("acessorio" if ACESSORIO.search(nome) else "principal")
            tipo = r[itipo].strip().upper() if itipo < len(r) else ""
            try:
                pf = int(re.sub(r"\D", "", r[ipf])) if 0 <= ipf < len(r) and re.search(r"\d", r[ipf]) else 0
            except ValueError:
                pf = 0
            pes.append({"nome": nome, "papel": "acessorio" if papel.startswith("acess") else "principal", "tipo": tipo, "pf": pf, "alr": [], "motivos": {}})
    memoria = metricas.split("### Memória")[-1] if "### Memória" in metricas else metricas
    for b in blocos_json(memoria):
        if "alr" in b:
            alvo = next((p for p in pes if norm(p["nome"]) == norm(b.get("pe", ""))), pes[0] if pes else None)
            if alvo is not None:
                alvo["alr"] = [limpar_entidade(a) for a in b["alr"]]
    # motivos "N. `Entidade` — razão" (formato novo) e "ALI X — razão; AIE Y — razão" (formato antigo)
    for m in re.finditer(r"`([^`]+)`\s+—\s+([^\n]+)", memoria):
        for p in pes:
            if limpar_entidade(m.group(1)) in p["alr"]:
                p["motivos"].setdefault(limpar_entidade(m.group(1)), norm(m.group(2)))
    if pes and not any(p["alr"] for p in pes):
        for m in re.finditer(r"(ALI|AIE)\s+([A-Z][\w]+)\s+—\s+([^;)]+)", memoria):
            ent = m.group(2)
            if ent not in pes[0]["alr"]:
                pes[0]["alr"].append(ent)
                pes[0]["motivos"][ent] = norm(m.group(3))
    if not pes:
        pes = [{"nome": titulo, "papel": "principal", "tipo": "EE" if endpoints and any(e.split()[0] in ("POST", "PUT", "PATCH", "DELETE") for e in endpoints) else "CE", "pf": 0, "alr": [], "motivos": {}}]

    # RM-05 saídas: ## API, ## Colunas do resultado
    devolve_objeto = bool(re.search(r"//\s*2\d\d[^\n]*\n\s*\{\s*\"data\"\s*:\s*\{", api))
    erros = [r for cab, corpo in tabelas(api) if coluna(cab, "http") >= 0 for r in corpo]
    tem_mensagem = bool(erros) or bool(fm.get("error_codes")) or bool(re.search(r"(?m)^\s*(Then|Então)\b.*\b(nao|não|recus|impede|bloque|apont)", sec.get("Cenários", "")))
    consulta = "Colunas do resultado" in sec

    processos = []
    primeiros = [p for p in pes if p["papel"] == "principal"] or pes[:1]
    acessorios = [p for p in pes if p["papel"] == "acessorio"]
    for n, pe in enumerate(primeiros):
        pid = fid if n == 0 else f"{fid}.{n + 1}"
        tipo_pe = pe["tipo"] or ("CE" if consulta else "EE")
        movs = {}

        def add(t, e, s):
            movs.setdefault((t, e), set()).add(s)

        # entradas (RM-02 / RM-01)
        if n == 0 and entradas:
            for e in entradas:
                add("E", e, ev("Campos"))
        elif uf != "pessoa" or not entradas:
            add("E", "DISPARO" if (uf != "pessoa" or tipo_pe in ("CE", "SE")) and not entradas else principal,
                ev("Superfície" if "Superfície" in sec else "API"))
        else:
            add("E", principal, ev("Métricas de tamanho"))
        # leituras e gravações (RM-03 / RM-04)
        alr = pe["alr"] or ([principal] if n == 0 else [])
        if n == 0 and (le or grava):
            for e in le:
                add("R", e, ev("Dados lidos e gravados"))
            for e in grava:
                add("W", e, ev("Dados lidos e gravados"))
        for e in alr:
            motivo = pe["motivos"].get(e, "")
            externo = bool(re.search(r"\b(github|google|aie)\b", norm(e) + " " + motivo))
            if externo:
                add("E", e, ev("Memória de cálculo"))      # RM-03 c: AIE acessado por chamada = resposta usada
                continue
            mantido = tipo_pe == "EE" and (e == principal or re.search(r"mantid|grav|atualiz|cria|registr|altera", motivo))
            lido = re.search(r"lid|valid|consult|verific|nome|exib|confer|busca", motivo) or tipo_pe in ("CE", "SE") or e != principal
            if mantido:
                add("W", e, ev("Memória de cálculo"))
            if lido and (not mantido or re.search(r"lid|valid|consult|verific|confer", motivo)):
                add("R", e, ev("Memória de cálculo"))
        for e in selecoes:                                  # RM-02 b
            add("R", e, ev("Campos"))
            add("X", e, ev("Campos"))
        # saídas (RM-05)
        if tipo_pe in ("CE", "SE"):
            add("X", principal, ev("Colunas do resultado" if consulta else "API"))
            for e in alr:
                if e != principal and re.search(r"nome|exib|linha|mostr|apresent|descri", pe["motivos"].get(e, "")):
                    add("X", e, ev("Memória de cálculo"))
        elif devolve_objeto:
            add("X", principal, ev("API"))
        if n == 0:
            for a in acessorios:                            # RM-07: acessório = R+X dentro do processo
                for e in a["alr"]:
                    add("R", e, ev("Métricas de tamanho"))
                    add("X", e, ev("Métricas de tamanho"))
        # desfechos (RM-06): a tabela de erros é da feature e fica no primeiro processo; recusa só
        # indicada nos cenários vale um desfecho por mensagem (RI-12)
        desf = desfechos_n3(sec, fm, ev) if n == 0 else []
        if n == 0 and not desf and tem_mensagem:
            desf = [{"id": "RECUSA", "descricao": "recusa indicada nos cenários", "tipo": "recusa", "evidencia": [ev("Cenários")]}]
        movimentos = [{"tipo": t, "entidade": e, "evidencia": sorted(s)} for (t, e), s in
                      sorted(movs.items(), key=lambda kv: ("ERWX".index(kv[0][0]), kv[0][1]))]
        if not desf and not any(m["tipo"] in ("X", "W") for m in movimentos):
            # RI-04 T2: o N3 não declara saída nem gravação; o efeito existe, mas o extrator não o localiza
            movimentos.append({"tipo": "X", "entidade": principal, "inferido": True,
                               "justificativa": "efeito presumido: o N3 não declara saída nem gravação deste processo elementar (RI-04 T2)"})

        processos.append({
            "id": pid, "nome": pe["nome"] if n else titulo or pe["nome"],
            **({"desfechos": desf} if desf else {}),
            "disparadores": [{"usuario": UF[uf]["id"], "evento": evento}],
            "evidencia": [ev("Métricas de tamanho"), ev("API")],
            "apf": {"pf": pe["pf"] + (sum(a["pf"] for a in acessorios) if n == 0 else 0), "tipo": tipo_pe,
                    "pes": [pe["nome"]] + ([a["nome"] for a in acessorios] if n == 0 else [])},
            "n3": {"arquivo": rel, "estado": fm.get("estado", ""), "dominio": fm.get("dominio", ""), "feature_set": fm.get("feature_set", "")},
            "movimentos": movimentos,
        })
    return processos, {"principal": principal, "dominio": fm.get("dominio", ""), "arquivo": rel}


# ---------------------------------------------------------------------------
# produção (git) e mudança (versão anterior)
# ---------------------------------------------------------------------------

def modo_producao_git(raiz, rel):
    """RP-01 (heurística): modo pela proporção de commits do arquivo com coautoria de IA."""
    try:
        saida = subprocess.check_output(["git", "-C", raiz, "log", "--format=%H%x1f%an%x1f%b%x1e", "--", rel],
                                        text=True, stderr=subprocess.DEVNULL)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    commits = [c for c in saida.split("\x1e") if c.strip()]
    if not commits:
        return None
    ia = sum(1 for c in commits if re.search(r"co-authored-by:.*(claude|copilot|gpt|gemini|ai\b|bot)", c, re.I)
             or re.search(r"\x1f[^\x1f]*(claude|copilot|\[bot\])", c, re.I))
    frac = ia / len(commits)
    modo = "M0" if ia == 0 else ("M1" if frac < 0.5 else "M2")
    return {"modo": modo, "evidencia": [f"PROC:git log -- {rel} ({len(commits)} commits, {ia} com coautoria de IA)"],
            "nota": "Heurística: M2 quando a maioria dos commits do arquivo tem coautoria de IA; revisão humana presumida pelos gates do N3."}


def marcar_alterados(processos, raiz_depois, raiz_antes):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from pfc import bloco  # heurística de bloco por indentação
    cache = {}

    def texto(raiz, rel):
        k = (raiz, rel)
        if k not in cache:
            p = os.path.join(raiz, rel)
            cache[k] = open(p, encoding="utf-8").read() if os.path.isfile(p) else None
        return cache[k]

    for p in processos:
        for m in p["movimentos"] + p.get("desfechos", []):
            mudou = False
            for e in m.get("evidencia", []):
                _, loc = e.split(":", 1)
                rel, _, secao = loc.partition("#")
                a, d = texto(raiz_antes, rel), texto(raiz_depois, rel)
                if a is None:
                    continue  # arquivo novo: o movimento é incluído, não alterado
                sa, sd = secao_texto(a, secao), secao_texto(d, secao)
                if sa != sd:
                    mudou = True
            if mudou:
                m["alterado"] = True


def secao_texto(texto, titulo):
    if texto is None:
        return None
    linhas = texto.splitlines()
    for i, l in enumerate(linhas):
        if l.startswith("## ") and l[3:].strip() == titulo or l.startswith("### ") and l[4:].strip() == titulo:
            fim = i + 1
            nivel = 2 if l.startswith("## ") else 3
            while fim < len(linhas) and not (linhas[fim].startswith("## ") or (nivel == 3 and linhas[fim].startswith("### "))):
                fim += 1
            return "\n".join(x.strip() for x in linhas[i:fim] if x.strip())
    return None


# ---------------------------------------------------------------------------
# montagem do modelo
# ---------------------------------------------------------------------------

def extrair(raiz, escopos=(), git=False, antes=None):
    arquivos = sorted(os.path.join(dp, f) for dp, _, fs in os.walk(os.path.join(raiz, "modules")) for f in fs
                      if f.startswith("f-") and f.endswith(".md"))
    processos, entidades, dominios = [], {}, set()
    for caminho in arquivos:
        procs, info = extrair_feature(caminho, raiz)
        if escopos and not any(p["id"].startswith(e) for p in procs for e in escopos):
            continue
        if git:
            prod = modo_producao_git(raiz, info["arquivo"])
            if prod:
                for p in procs:
                    p["producao"] = prod
        for p in procs:
            for m in p["movimentos"]:
                if m["entidade"] != "DISPARO":
                    entidades.setdefault(m["entidade"], set()).add(f"DOC:{info['arquivo']}#{m['entidade']}")
        dominios.add(info["dominio"])
        processos.extend(procs)
    if antes:
        marcar_alterados(processos, raiz, antes)
    # evidência de entidade: fragmento do data-model quando a entidade aparece nele
    for ent in entidades:
        for dp, _, fs in os.walk(os.path.join(raiz, "global", "data-models")):
            for f in fs:
                rel = os.path.relpath(os.path.join(dp, f), raiz).replace(os.sep, "/")
                if ent in open(os.path.join(dp, f), encoding="utf-8").read():
                    entidades[ent] = {f"DOC:{rel}#{ent}"}
                    break
    ufs = sorted({d["usuario"] for p in processos for d in p["disparadores"]})
    try:
        versao = open(os.path.join(raiz, "VERSION"), encoding="utf-8").read().strip()
    except OSError:
        versao = ""
    try:
        commit = subprocess.check_output(["git", "-C", raiz, "rev-parse", "--short", "HEAD"], text=True, stderr=subprocess.DEVNULL).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        commit = ""
    modelo = {
        "pfc": "1.0",
        "software": os.path.basename(os.path.abspath(raiz)),
        "versao": versao,
        "proposito": "Medir o tamanho funcional especificado na documentação N3 (extração mecânica)",
        "escopo": "features " + (", ".join(escopos) if escopos else "de todos os domínios: " + ", ".join(sorted(d for d in dominios if d))),
        "nivel": "R",
        "agente": {"tipo": "ferramenta", "nome": f"extrair_n3.py {VERSAO_EXTRATOR}", "revisao_humana": False},
        "fontes": [
            {"id": "DOC", "tipo": "requisitos", "ref": f"{os.path.abspath(raiz)}" + (f"@{commit}" if commit else "")},
            {"id": "PROC", "tipo": "processo", "ref": "histórico git da instância"},
        ],
        "usuarios_funcionais": [UF[k] for k in ("pessoa", "sistema", "relogio") if UF[k]["id"] in ufs],
        "entidades": [{"id": e, "evidencia": sorted(evs)} for e, evs in sorted(entidades.items())],
        "processos": processos,
    }
    return modelo


def main(argv=None):
    ap = argparse.ArgumentParser(description="Extrai o MFC (PFC 1.0) da estrutura N3 do siesa-engine")
    ap.add_argument("raiz")
    ap.add_argument("-o", "--saida")
    ap.add_argument("--escopo", nargs="*", default=[])
    ap.add_argument("--git", action="store_true")
    ap.add_argument("--antes")
    args = ap.parse_args(argv)
    modelo = extrair(args.raiz, args.escopo, args.git, args.antes)
    texto = json.dumps(modelo, ensure_ascii=False, indent=2)
    if args.saida:
        with open(args.saida, "w", encoding="utf-8") as f:
            f.write(texto + "\n")
        print(f"{len(modelo['processos'])} processos, {len(modelo['entidades'])} entidades -> {args.saida}")
    else:
        print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
