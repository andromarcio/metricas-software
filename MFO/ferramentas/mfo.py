#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mfo.py — ferramenta de referência do método MFO (Medição Funcional Objetiva) 1.0.

Subcomandos:
  validar       <modelo.json>                      valida o Modelo Funcional Canônico (V-01 a V-09)
  contar        <modelo.json> [--json]             PFO, perfil funcional, suplemento D e rótulo (RC-01, RC-02, RC-05, RC-06)
  mudanca       <antes.json> <depois.json> [--json] tamanho de uma mudança (RC-03)
  concordancia  <a.json> <b.json> [--json]         índice de concordância entre duas medições (seção 4.4)

Sem dependências externas. Python 3.8 ou superior.
A contagem é definida apenas para modelos válidos: 'contar', 'mudanca' e 'concordancia'
recusam modelos com erros de validação.
"""
import argparse
import json
import sys
import unicodedata
from collections import Counter

VERSAO_METODO = "1.0"
TIPOS = ("E", "X", "R", "W")
RESERVADAS = {"MENSAGEM": "X", "DISPARO": "E"}
NIVEIS = ("R", "C", "RC")
TIPOS_UF = ("pessoa", "sistema", "dispositivo", "relogio")
TIPOS_AGENTE = ("humano", "ia")
CAMPOS_OBRIGATORIOS = (
    "mfo", "software", "proposito", "escopo", "nivel", "agente",
    "fontes", "usuarios_funcionais", "entidades", "processos",
)


# ---------------------------------------------------------------------------
# utilidades
# ---------------------------------------------------------------------------

def normalizar(texto):
    """Minúsculas, sem acentos, espaços simples. Usado para parear nomes e ids."""
    if texto is None:
        return ""
    t = unicodedata.normalize("NFKD", str(texto))
    t = "".join(c for c in t if not unicodedata.combining(c))
    return " ".join(t.lower().split())


def carregar(caminho):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def fmt_num(x, casas=2):
    """Número com vírgula decimal (pt-BR)."""
    if x is None:
        return "n/d"
    s = f"{x:.{casas}f}"
    return s.replace(".", ",")


def pct(num, den):
    return 0.0 if not den else 100.0 * num / den


# ---------------------------------------------------------------------------
# evidência (RI-11)
# ---------------------------------------------------------------------------

def evidencia_valida(elem, fontes):
    """True se o elemento tem lista não vazia de evidências 'FONTE:localizador' com FONTE declarada."""
    ev = elem.get("evidencia")
    if not isinstance(ev, list) or not ev:
        return False
    for e in ev:
        if not isinstance(e, str) or ":" not in e:
            return False
        prefixo, loc = e.split(":", 1)
        if prefixo not in fontes or not loc.strip():
            return False
    return True


def situacao_evidencia(elem, fontes):
    """'evidenciado', 'inferido' (RI-11 b) ou None (inválido)."""
    if evidencia_valida(elem, fontes):
        return "evidenciado"
    if elem.get("inferido") is True and str(elem.get("justificativa", "")).strip():
        return "inferido"
    return None


# ---------------------------------------------------------------------------
# validação (V-01 a V-09)
# ---------------------------------------------------------------------------

def validar(modelo):
    """Retorna (erros, avisos). Um modelo com erros não pode ser contado."""
    erros, avisos = [], []

    if not isinstance(modelo, dict):
        return ["V-01: o modelo deve ser um objeto JSON"], []
    for c in CAMPOS_OBRIGATORIOS:
        if c not in modelo:
            erros.append(f"V-01: campo obrigatório ausente: '{c}'")
    if erros:
        return erros, avisos

    if str(modelo.get("mfo")) != VERSAO_METODO:
        avisos.append(f"V-01: versão do método '{modelo.get('mfo')}' difere da ferramenta ({VERSAO_METODO})")
    for c in ("software", "proposito", "escopo"):
        if not str(modelo.get(c, "")).strip():
            erros.append(f"V-01: '{c}' não pode ser vazio")
    if modelo.get("nivel") not in NIVEIS:
        erros.append(f"V-01: 'nivel' deve ser um de {NIVEIS}; recebido '{modelo.get('nivel')}'")

    agente = modelo.get("agente")
    if not isinstance(agente, dict) or agente.get("tipo") not in TIPOS_AGENTE:
        erros.append(f"V-01: 'agente' deve ser objeto com 'tipo' em {TIPOS_AGENTE}")

    # fontes
    fontes = {}
    for i, f in enumerate(modelo.get("fontes") or []):
        if not isinstance(f, dict) or not str(f.get("id", "")).strip() or not str(f.get("ref", "")).strip():
            erros.append(f"V-01: fonte #{i + 1} precisa de 'id' e 'ref'")
            continue
        if f["id"] in fontes:
            erros.append(f"V-01: fonte duplicada '{f['id']}'")
        fontes[f["id"]] = f
    if not fontes:
        erros.append("V-01: pelo menos uma fonte deve ser declarada")

    # usuários funcionais
    ufs = {}
    for i, u in enumerate(modelo.get("usuarios_funcionais") or []):
        if not isinstance(u, dict) or not str(u.get("id", "")).strip():
            erros.append(f"V-01: usuário funcional #{i + 1} precisa de 'id'")
            continue
        if u["id"] in ufs:
            erros.append(f"V-01: usuário funcional duplicado '{u['id']}'")
        if u.get("tipo") not in TIPOS_UF:
            erros.append(f"V-01: usuário funcional '{u['id']}' deve ter 'tipo' em {TIPOS_UF}")
        ufs[u["id"]] = u
    if not ufs:
        erros.append("V-01: pelo menos um usuário funcional deve ser declarado")

    # entidades
    entidades = {}
    for i, e in enumerate(modelo.get("entidades") or []):
        if not isinstance(e, dict) or not str(e.get("id", "")).strip():
            erros.append(f"V-01: entidade #{i + 1} precisa de 'id'")
            continue
        if e["id"] in RESERVADAS:
            erros.append(f"V-05: '{e['id']}' é entidade reservada e não deve ser declarada")
        if e["id"] in entidades:
            erros.append(f"V-01: entidade duplicada '{e['id']}'")
        entidades[e["id"]] = e
        if situacao_evidencia(e, fontes) is None:
            avisos.append(f"RI-11: entidade '{e['id']}' sem evidência válida nem marcação de inferência")

    # processos
    referenciadas = set()
    assinaturas = {}
    ids_proc = set()
    for i, p in enumerate(modelo.get("processos") or []):
        if not isinstance(p, dict) or not str(p.get("id", "")).strip():
            erros.append(f"V-01: processo #{i + 1} precisa de 'id'")
            continue
        pid = p["id"]
        if pid in ids_proc:
            erros.append(f"V-01: processo duplicado '{pid}'")
        ids_proc.add(pid)
        if not str(p.get("nome", "")).strip():
            erros.append(f"V-01: processo '{pid}' precisa de 'nome'")

        # V-08 disparadores
        disps = p.get("disparadores")
        if not isinstance(disps, list) or not disps:
            erros.append(f"V-08: processo '{pid}' sem disparador")
        else:
            for d in disps:
                if not isinstance(d, dict) or d.get("usuario") not in ufs:
                    erros.append(f"V-08: processo '{pid}' tem disparador com usuário funcional não declarado: {d!r}")

        # V-07 evidência do processo
        if situacao_evidencia(p, fontes) is None:
            erros.append(f"V-07: processo '{pid}' sem evidência válida (ou 'inferido': true com 'justificativa')")

        movs = p.get("movimentos")
        if not isinstance(movs, list) or not movs:
            erros.append(f"V-02: processo '{pid}' sem movimentos")
            continue

        chaves = set()
        tipos = Counter()
        n_mensagem = 0
        for j, m in enumerate(movs):
            rot = f"processo '{pid}', movimento #{j + 1}"
            if not isinstance(m, dict):
                erros.append(f"V-01: {rot} deve ser objeto")
                continue
            tipo, ent = m.get("tipo"), m.get("entidade")
            if tipo not in TIPOS:
                erros.append(f"V-01: {rot} tem 'tipo' inválido '{tipo}' (use E, X, R ou W)")
                continue
            if not isinstance(ent, str) or not ent.strip():
                erros.append(f"V-04: {rot} sem 'entidade'")
                continue
            if ent in RESERVADAS:
                if tipo != RESERVADAS[ent]:
                    erros.append(f"V-05: {rot}: '{ent}' só pode ser usada em movimentos {RESERVADAS[ent]}")
                if ent == "MENSAGEM":
                    n_mensagem += 1
            elif ent not in entidades:
                erros.append(f"V-04: {rot} referencia entidade não declarada '{ent}'")
            else:
                referenciadas.add(ent)
            if (tipo, ent) in chaves:
                erros.append(f"V-06: {rot} repete a chave ({tipo}, {ent})")
            chaves.add((tipo, ent))
            tipos[tipo] += 1
            if situacao_evidencia(m, fontes) is None:
                erros.append(f"V-07: {rot} ({tipo} {ent}) sem evidência válida (ou 'inferido': true com 'justificativa')")
            if m.get("usuario") is not None and m.get("usuario") not in ufs:
                erros.append(f"V-08: {rot} referencia usuário funcional não declarado '{m.get('usuario')}'")

        if n_mensagem > 1:
            erros.append(f"V-05: processo '{pid}' tem {n_mensagem} movimentos X MENSAGEM (máximo 1)")
        if tipos["E"] == 0:
            erros.append(f"V-02: processo '{pid}' não tem movimento E")
        if tipos["X"] == 0 and tipos["W"] == 0:
            erros.append(f"V-03: processo '{pid}' não tem movimento X nem W")

        # V-09 assinatura: chaves + atributos (quando informados)
        attrs = []
        for m in movs:
            if isinstance(m, dict) and isinstance(m.get("atributos"), list):
                attrs.append((m.get("tipo"), m.get("entidade"), tuple(sorted(normalizar(a) for a in m["atributos"]))))
        assinatura = (frozenset(chaves), frozenset(attrs))
        if assinatura in assinaturas:
            avisos.append(f"V-09: processos '{assinaturas[assinatura]}' e '{pid}' têm a mesma assinatura; verifique RI-04 b")
        else:
            assinaturas[assinatura] = pid

    if not ids_proc:
        erros.append("V-01: pelo menos um processo deve ser declarado")

    # V-04 (parte 2): entidades declaradas e não referenciadas
    for eid in entidades:
        if eid not in referenciadas:
            erros.append(f"V-04: entidade '{eid}' declarada mas não referenciada por nenhum movimento")

    return erros, avisos


def exigir_valido(modelo, rotulo):
    erros, _ = validar(modelo)
    if erros:
        print(f"Modelo '{rotulo}' inválido; corrija antes de contar:", file=sys.stderr)
        for e in erros:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# contagem (RC-01, RC-02, RC-05, RC-06)
# ---------------------------------------------------------------------------

def derivacao(p):
    """RC-05. True/False quando todos os movimentos não reservados declaram 'atributos'; None caso contrário."""
    entradas, saidas = set(), set()
    for m in p["movimentos"]:
        if m["entidade"] in RESERVADAS:
            continue
        attrs = m.get("atributos")
        if not isinstance(attrs, list):
            return None
        alvo = entradas if m["tipo"] in ("E", "R") else saidas
        alvo.update(normalizar(a) for a in attrs)
    return bool(saidas - entradas)


def fontes_do(modelo):
    return {f["id"] for f in modelo["fontes"]}


def contar(modelo):
    fontes = fontes_do(modelo)
    linhas = []
    total_tipos = Counter()
    evidenciados = 0
    inferidos = 0
    d_sim, d_nd = 0, 0
    for p in modelo["processos"]:
        tipos = Counter(m["tipo"] for m in p["movimentos"])
        pfo = len(p["movimentos"])  # modelo válido: chaves únicas (V-06)
        ev = sum(1 for m in p["movimentos"] if situacao_evidencia(m, fontes) == "evidenciado")
        inf = pfo - ev
        d = derivacao(p)
        if d is True:
            d_sim += 1
        elif d is None:
            d_nd += 1
        linhas.append({
            "id": p["id"], "nome": p.get("nome", ""),
            "E": tipos["E"], "X": tipos["X"], "R": tipos["R"], "W": tipos["W"],
            "pfo": pfo, "derivacao": d, "evidenciados": ev, "inferidos": inf,
        })
        total_tipos.update(tipos)
        evidenciados += ev
        inferidos += inf

    pfo = sum(l["pfo"] for l in linhas)
    np_ = len(linhas)
    ne = len(modelo["entidades"])
    perfil = {
        "PFO": pfo, "NP": np_, "NE": ne,
        "E": total_tipos["E"], "X": total_tipos["X"], "R": total_tipos["R"], "W": total_tipos["W"],
        "densidade": (pfo / np_) if np_ else None,
        "persistencia": ((total_tipos["R"] + total_tipos["W"]) / pfo) if pfo else None,
        "interface": ((total_tipos["E"] + total_tipos["X"]) / pfo) if pfo else None,
        "entidades_por_processo": (ne / np_) if np_ else None,
        "evidencia_pct": pct(evidenciados, pfo),
        "evidenciados": evidenciados, "inferidos": inferidos,
        "D": d_sim, "D_nd": d_nd,
    }
    return {
        "software": modelo["software"], "versao": modelo.get("versao", ""),
        "mfo": modelo["mfo"], "nivel": modelo["nivel"], "escopo": modelo["escopo"],
        "proposito": modelo["proposito"], "agente": modelo["agente"],
        "rotulo": rotulo(modelo, pfo, perfil["evidencia_pct"]),
        "perfil": perfil, "processos": linhas,
    }


def descrever_agente(agente):
    s = agente.get("tipo", "")
    if agente.get("nome"):
        s += f" ({agente['nome']})"
    if "revisao_humana" in agente:
        s += " + revisão humana" if agente["revisao_humana"] else "; sem revisão humana"
    return s


def rotulo(modelo, pfo, evid_pct, prefixo=None):
    escopo = modelo["software"]
    if modelo.get("versao"):
        escopo += f" {modelo['versao']}"
    escopo += f", {modelo['escopo']}"
    cabeca = prefixo if prefixo is not None else f"{pfo} PFO"
    return (f"{cabeca} · MFO {modelo['mfo']} · nível {modelo['nivel']} · evidência {evid_pct:.0f}% · "
            f"agente: {descrever_agente(modelo['agente'])} · escopo: {escopo}")


def relatorio_md(rel):
    p = rel["perfil"]
    out = []
    titulo = rel["software"] + (f" {rel['versao']}" if rel["versao"] else "")
    out.append(f"# Relatório MFO — {titulo}\n")
    out.append(f"**Rótulo:** {rel['rotulo']}\n")
    out.append(f"**Propósito:** {rel['proposito']}\n")
    out.append("## Perfil funcional\n")
    out.append("| Indicador | Valor |\n|---|---|")
    out.append(f"| PFO | **{p['PFO']}** |")
    out.append(f"| NP (processos) | {p['NP']} |")
    out.append(f"| NE (entidades) | {p['NE']} |")
    out.append(f"| E / X / R / W | {p['E']} / {p['X']} / {p['R']} / {p['W']} |")
    out.append(f"| Densidade (PFO/NP) | {fmt_num(p['densidade'])} |")
    out.append(f"| Persistência ((R+W)/PFO) | {fmt_num(p['persistencia'])} |")
    out.append(f"| Interface ((E+X)/PFO) | {fmt_num(p['interface'])} |")
    out.append(f"| Entidades por processo (NE/NP) | {fmt_num(p['entidades_por_processo'])} |")
    out.append(f"| Evidência | {p['evidencia_pct']:.0f}% ({p['inferidos']} inferidos) |")
    d_txt = f"{p['D']} de {p['NP'] - p['D_nd']}" + (f" ({p['D_nd']} n/d)" if p["D_nd"] else "")
    out.append(f"| D (derivação, RC-05) | {d_txt} |")
    out.append("\n## Processos\n")
    out.append("| ID | Processo | E | X | R | W | PFO | Deriv. | Evid. |\n|---|---|---|---|---|---|---|---|---|")
    for l in rel["processos"]:
        d = {True: "sim", False: "não", None: "n/d"}[l["derivacao"]]
        out.append(f"| {l['id']} | {l['nome']} | {l['E']} | {l['X']} | {l['R']} | {l['W']} | **{l['pfo']}** | {d} | {l['evidenciados']}/{l['pfo']} |")
    out.append(f"| | **Total** | {p['E']} | {p['X']} | {p['R']} | {p['W']} | **{p['PFO']}** | | |")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# mudança (RC-03)
# ---------------------------------------------------------------------------

def chaves_modelo(modelo):
    """{(pid, tipo, entidade): movimento}"""
    out = {}
    for p in modelo["processos"]:
        for m in p["movimentos"]:
            out[(p["id"], m["tipo"], m["entidade"])] = m
    return out


def mudanca(antes, depois):
    ka, kb = chaves_modelo(antes), chaves_modelo(depois)
    incluidos = sorted(set(kb) - set(ka))
    excluidos = sorted(set(ka) - set(kb))
    alterados = sorted(k for k in set(ka) & set(kb) if kb[k].get("alterado") is True)
    pa = {p["id"] for p in antes["processos"]}
    pb = {p["id"] for p in depois["processos"]}
    total = len(incluidos) + len(alterados) + len(excluidos)
    evid = sum(1 for k in incluidos + alterados if situacao_evidencia(kb[k], fontes_do(depois)) == "evidenciado")
    evid += sum(1 for k in excluidos if situacao_evidencia(ka[k], fontes_do(antes)) == "evidenciado")
    prefixo = f"{total} PFO de mudança ({len(incluidos)} incluídos, {len(alterados)} alterados, {len(excluidos)} excluídos)"
    return {
        "de": f"{antes['software']} {antes.get('versao', '')}".strip(),
        "para": f"{depois['software']} {depois.get('versao', '')}".strip(),
        "pfo_mudanca": total,
        "incluidos": incluidos, "alterados": alterados, "excluidos": excluidos,
        "processos_novos": sorted(pb - pa), "processos_removidos": sorted(pa - pb),
        "pfo_antes": len(ka), "pfo_depois": len(kb),
        "rotulo": rotulo(depois, total, pct(evid, total) if total else 100.0, prefixo=prefixo),
    }


def mudanca_md(r):
    out = [f"# Mudança MFO — {r['de']} → {r['para']}\n", f"**Rótulo:** {r['rotulo']}\n"]
    out.append(f"Tamanho anterior: {r['pfo_antes']} PFO · tamanho posterior: {r['pfo_depois']} PFO\n")
    for titulo, chaves in (("Incluídos", r["incluidos"]), ("Alterados", r["alterados"]), ("Excluídos", r["excluidos"])):
        out.append(f"## {titulo} ({len(chaves)})\n")
        out.extend(f"- {pid} · {t} {e}" for pid, t, e in chaves)
        if not chaves:
            out.append("- (nenhum)")
        out.append("")
    if r["processos_novos"] or r["processos_removidos"]:
        out.append(f"Processos novos: {', '.join(r['processos_novos']) or '—'} · processos removidos: {', '.join(r['processos_removidos']) or '—'}\n")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# concordância (seção 4.4)
# ---------------------------------------------------------------------------

def parear_processos(a, b):
    """Mapeia id de processo de B -> id em A, por id igual ou por nome normalizado."""
    ids_a = {p["id"]: p for p in a["processos"]}
    nomes_a = {normalizar(p.get("nome")): p["id"] for p in a["processos"]}
    mapa = {}
    for p in b["processos"]:
        if p["id"] in ids_a:
            mapa[p["id"]] = p["id"]
        elif normalizar(p.get("nome")) in nomes_a:
            mapa[p["id"]] = nomes_a[normalizar(p.get("nome"))]
    return mapa


def concordancia(a, b):
    mapa = parear_processos(a, b)
    nomes = {}  # entidade normalizada -> nome original (A tem precedência)
    for modelo in (b, a):
        for (_, _, e) in chaves_modelo(modelo):
            nomes[normalizar(e)] = e
    ka = {(pid, t, normalizar(e)) for (pid, t, e) in chaves_modelo(a)}
    kb = set()
    for (pid, t, e) in chaves_modelo(b):
        kb.add((mapa.get(pid, "B:" + pid), t, normalizar(e)))
    comuns, uniao = ka & kb, ka | kb
    indice = (len(comuns) / len(uniao)) if uniao else 1.0
    so_a = sorted((pid, t, nomes[e]) for (pid, t, e) in ka - kb)
    so_b = sorted((pid, t, nomes[e]) for (pid, t, e) in kb - ka)
    nao_pareados_b = sorted(p["id"] for p in b["processos"] if p["id"] not in mapa)
    pareados = set(mapa.values())
    nao_pareados_a = sorted(p["id"] for p in a["processos"] if p["id"] not in pareados)
    return {
        "indice": indice, "comuns": len(comuns), "uniao": len(uniao),
        "pfo_a": len(ka), "pfo_b": len(kb),
        "so_em_a": so_a, "so_em_b": so_b,
        "processos_so_em_a": nao_pareados_a, "processos_so_em_b": nao_pareados_b,
    }


def concordancia_md(r, nome_a, nome_b):
    out = [f"# Concordância MFO — {nome_a} × {nome_b}\n"]
    out.append(f"**Índice de concordância:** {fmt_num(r['indice'], 3)} ({r['comuns']} chaves comuns de {r['uniao']})\n")
    out.append(f"PFO em A: {r['pfo_a']} · PFO em B: {r['pfo_b']}\n")
    if r["indice"] >= 0.90:
        leitura = "medições equivalentes: conciliar as divergências e rotular"
    elif r["indice"] >= 0.75:
        leitura = "divergência localizada: revisar os processos divergentes e o glossário de entidades"
    else:
        leitura = "interpretação diferente do escopo ou da fronteira: revisar a preparação antes de nova extração"
    out.append(f"Leitura: {leitura}\n")
    for titulo, chaves in (("Só em A", r["so_em_a"]), ("Só em B", r["so_em_b"])):
        out.append(f"## {titulo} ({len(chaves)})\n")
        out.extend(f"- {pid} · {t} {e}" for pid, t, e in chaves)
        if not chaves:
            out.append("- (nenhuma)")
        out.append("")
    if r["processos_so_em_a"] or r["processos_so_em_b"]:
        out.append(f"Processos não pareados — só em A: {', '.join(r['processos_so_em_a']) or '—'}; só em B: {', '.join(r['processos_so_em_b']) or '—'}\n")
    out.append("Cada divergência deve ser fechada citando a regra (RI-xx) e a evidência que decide.\n")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# linha de comando
# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(prog="mfo.py", description="Ferramenta de referência do método MFO 1.0")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("validar", help="valida um Modelo Funcional Canônico (V-01 a V-09)")
    s.add_argument("modelo")

    s = sub.add_parser("contar", help="calcula PFO, perfil funcional e rótulo")
    s.add_argument("modelo")
    s.add_argument("--json", action="store_true", help="saída em JSON em vez de Markdown")

    s = sub.add_parser("mudanca", help="tamanho de uma mudança entre dois modelos (RC-03)")
    s.add_argument("antes")
    s.add_argument("depois")
    s.add_argument("--json", action="store_true")

    s = sub.add_parser("concordancia", help="índice de concordância entre duas medições")
    s.add_argument("a")
    s.add_argument("b")
    s.add_argument("--json", action="store_true")

    args = ap.parse_args(argv)

    if args.cmd == "validar":
        modelo = carregar(args.modelo)
        erros, avisos = validar(modelo)
        for e in erros:
            print(f"ERRO   {e}")
        for a in avisos:
            print(f"AVISO  {a}")
        if erros:
            print(f"\nModelo inválido: {len(erros)} erro(s), {len(avisos)} aviso(s).")
            return 1
        print(f"Modelo válido ({len(avisos)} aviso(s)).")
        return 0

    if args.cmd == "contar":
        modelo = carregar(args.modelo)
        exigir_valido(modelo, args.modelo)
        rel = contar(modelo)
        _, avisos = validar(modelo)
        if args.json:
            rel["avisos"] = avisos
            print(json.dumps(rel, ensure_ascii=False, indent=2))
        else:
            print(relatorio_md(rel))
            if avisos:
                print("## Avisos\n")
                print("\n".join(f"- {a}" for a in avisos))
        return 0

    if args.cmd == "mudanca":
        antes, depois = carregar(args.antes), carregar(args.depois)
        exigir_valido(antes, args.antes)
        exigir_valido(depois, args.depois)
        r = mudanca(antes, depois)
        if args.json:
            r = dict(r, incluidos=[list(k) for k in r["incluidos"]], alterados=[list(k) for k in r["alterados"]],
                     excluidos=[list(k) for k in r["excluidos"]])
            print(json.dumps(r, ensure_ascii=False, indent=2))
        else:
            print(mudanca_md(r))
        return 0

    if args.cmd == "concordancia":
        a, b = carregar(args.a), carregar(args.b)
        exigir_valido(a, args.a)
        exigir_valido(b, args.b)
        r = concordancia(a, b)
        if args.json:
            r = dict(r, so_em_a=[list(k) for k in r["so_em_a"]], so_em_b=[list(k) for k in r["so_em_b"]])
            print(json.dumps(r, ensure_ascii=False, indent=2))
        else:
            print(concordancia_md(r, args.a, args.b))
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
