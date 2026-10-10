#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mfo.py — ferramenta de referência do método MFO (Medição Funcional Objetiva) 1.0.

Subcomandos:
  validar       <modelo.json>                      valida o Modelo Funcional Canônico (V-01 a V-10)
  contar        <modelo.json> [--json]             PFO, perfil funcional, suplemento D, produção e rótulo
  mudanca       <antes.json> <depois.json> [--json] tamanho de uma mudança (RC-03), por modo de produção
  concordancia  <a.json> <b.json> [--json]         índice de concordância entre duas medições (seção 4.4)
  impacto       <modelo.json> --dirs A B | --git REPO A B   processos afetados por um diff de código (capítulo 8)
  auditar       <modelo.json> --raiz DIR [--fonte COD]     confere se cada evidência existe no código (RD-03)
  perfis        <modelos.json...> [-o perfis.json]         PFO típico por tipo de processo a partir de modelos medidos (RE-02)
  estimar       <backlog.json> [--perfis P] [-o modelo]    estimativa E0/E1 a partir de um backlog (RE-01, RE-03)

Sem dependências externas. Python 3.8 ou superior.
A contagem é definida apenas para modelos válidos: 'contar', 'mudanca' e 'concordancia'
recusam modelos com erros de validação.
"""
import argparse
import difflib
import json
import os
import statistics
import subprocess
import sys
import unicodedata
from collections import Counter

VERSAO_METODO = "1.0"
TIPOS = ("E", "X", "R", "W")
RESERVADAS = {"MENSAGEM": "X", "DISPARO": "E"}
NIVEIS = ("R", "C", "RC")
TIPOS_UF = ("pessoa", "sistema", "dispositivo", "relogio")
TIPOS_AGENTE = ("humano", "ia", "ferramenta")
TIPOS_FONTE = ("requisitos", "prototipo", "api", "codigo", "banco", "sistema", "testes", "processo", "outro")
CAMPOS_OBRIGATORIOS = (
    "mfo", "software", "proposito", "escopo", "nivel", "agente",
    "fontes", "usuarios_funcionais", "entidades", "processos",
)
# produção com IA (capítulo 8)
MODOS = ("M0", "M1", "M2", "M3")
MODO_ND = "nd"
NOME_MODO = {"M0": "M0 humano", "M1": "M1 IA assistida", "M2": "M2 IA dirigida", "M3": "M3 IA autônoma", "nd": "não declarado"}
STATUS_ACEITE = ("aceito", "pendente", "rejeitado")
ABRANGE = ("software", "mudanca")


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


def eh_numero(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


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
# validação (V-01 a V-10)
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
        if f.get("tipo") not in TIPOS_FONTE:
            avisos.append(f"V-01: fonte '{f['id']}' com tipo '{f.get('tipo')}' fora de {TIPOS_FONTE}")
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
    com_modo = 0
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

        # V-10 produção e aceite do processo (capítulo 8)
        prod = p.get("producao")
        if prod is not None:
            if not isinstance(prod, dict) or prod.get("modo") not in MODOS:
                erros.append(f"V-10: processo '{pid}' tem 'producao.modo' inválido (use M0, M1, M2 ou M3)")
            elif situacao_evidencia(prod, fontes) is None:
                erros.append(f"V-10: processo '{pid}': 'producao' sem evidência válida (ou 'inferido': true com 'justificativa')")
            else:
                com_modo += 1
        ac = p.get("aceite")
        if ac is not None:
            if not isinstance(ac, dict) or ac.get("status") not in STATUS_ACEITE:
                erros.append(f"V-10: processo '{pid}' tem 'aceite.status' inválido (use aceito, pendente ou rejeitado)")
            elif situacao_evidencia(ac, fontes) is None:
                erros.append(f"V-10: processo '{pid}': 'aceite' sem evidência válida (ou 'inferido': true com 'justificativa')")

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

    # V-10: produção no nível do modelo
    pm = modelo.get("producao")
    if pm is not None:
        if not isinstance(pm, dict) or pm.get("abrange") not in ABRANGE:
            erros.append("V-10: 'producao' do modelo deve ser objeto com 'abrange' em ('software', 'mudanca')")
        else:
            for c in ("horas_humanas", "custo_humano", "custo_ia"):
                v = pm.get(c)
                if v is not None and (not eh_numero(v) or v < 0):
                    erros.append(f"V-10: 'producao.{c}' deve ser número não negativo")
            if com_modo == 0:
                avisos.append("V-10: 'producao' declarada no modelo, mas nenhum processo tem 'producao.modo'")

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


def modo_de(p):
    prod = p.get("producao")
    return prod["modo"] if isinstance(prod, dict) and prod.get("modo") in MODOS else MODO_ND


def status_aceite_de(p):
    ac = p.get("aceite")
    return ac["status"] if isinstance(ac, dict) and ac.get("status") in STATUS_ACEITE else None


def resumo_producao(modelo, pfo_por_processo):
    """PFO por modo de produção e por status de aceite (RP-01, RP-03).
    pfo_por_processo: {pid: PFO atribuído ao processo} (total em 'contar', chaves mudadas em 'mudanca')."""
    procs = {p["id"]: p for p in modelo["processos"]}
    por_modo = {m: {"processos": 0, "pfo": 0} for m in list(MODOS) + [MODO_ND]}
    aceite = {s: 0 for s in list(STATUS_ACEITE) + ["sem_aceite"]}
    declarado = False
    for pid, pfo in pfo_por_processo.items():
        p = procs.get(pid)
        if p is None:
            por_modo[MODO_ND]["processos"] += 1
            por_modo[MODO_ND]["pfo"] += pfo
            aceite["sem_aceite"] += pfo
            continue
        if p.get("producao") is not None or p.get("aceite") is not None:
            declarado = True
        m = modo_de(p)
        por_modo[m]["processos"] += 1
        por_modo[m]["pfo"] += pfo
        s = status_aceite_de(p)
        aceite[s if s else "sem_aceite"] += pfo
    total = sum(pfo_por_processo.values())
    return {"declarado": declarado, "total": total, "por_modo": por_modo, "aceite": aceite}


def indicadores_producao(pm, pfo_produzidos):
    """RP-02: alavancagem humana e custos por PFO a partir do bloco 'producao' do modelo."""
    if not isinstance(pm, dict):
        return None
    horas = pm.get("horas_humanas")
    ch, ci = pm.get("custo_humano"), pm.get("custo_ia")
    ind = {"abrange": pm.get("abrange"), "periodo": pm.get("periodo"), "moeda": pm.get("moeda", ""),
           "pfo_produzidos": pfo_produzidos, "horas_humanas": horas, "custo_humano": ch, "custo_ia": ci,
           "alavancagem": None, "custo_total": None, "custo_por_pfo": None, "custo_ia_por_pfo": None,
           "participacao_ia": None}
    if eh_numero(horas) and horas > 0:
        ind["alavancagem"] = pfo_produzidos / horas
    if eh_numero(ch) or eh_numero(ci):
        total = (ch if eh_numero(ch) else 0) + (ci if eh_numero(ci) else 0)
        ind["custo_total"] = total
        if pfo_produzidos:
            ind["custo_por_pfo"] = total / pfo_produzidos
            if eh_numero(ci):
                ind["custo_ia_por_pfo"] = ci / pfo_produzidos
        if total > 0 and eh_numero(ci):
            ind["participacao_ia"] = ci / total
    return ind


def contar(modelo):
    fontes = fontes_do(modelo)
    linhas = []
    total_tipos = Counter()
    evidenciados = 0
    inferidos = 0
    d_sim, d_nd = 0, 0
    pfo_por_processo = {}
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
            "modo": modo_de(p), "aceite": status_aceite_de(p),
        })
        pfo_por_processo[p["id"]] = pfo
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
    producao = resumo_producao(modelo, pfo_por_processo)
    pm = modelo.get("producao")
    indicadores = indicadores_producao(pm, pfo) if isinstance(pm, dict) and pm.get("abrange") == "software" else None
    return {
        "software": modelo["software"], "versao": modelo.get("versao", ""),
        "mfo": modelo["mfo"], "nivel": modelo["nivel"], "escopo": modelo["escopo"],
        "proposito": modelo["proposito"], "agente": modelo["agente"],
        "rotulo": rotulo(modelo, pfo, perfil["evidencia_pct"]),
        "perfil": perfil, "processos": linhas,
        "producao": producao, "indicadores_producao": indicadores,
        "producao_abrange": pm.get("abrange") if isinstance(pm, dict) else None,
        "estimativa": modelo.get("estimativa"),
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
    est = modelo.get("estimativa")
    if prefixo is None and isinstance(est, dict):
        cabeca = f"≈ {est.get('pfo_calibrado', pfo)} PFO (estimativa {est.get('nivel', '?')}, {est.get('pfo_min', '?')} a {est.get('pfo_max', '?')})"
    return (f"{cabeca} · MFO {modelo['mfo']} · nível {modelo['nivel']} · evidência {evid_pct:.0f}% · "
            f"agente: {descrever_agente(modelo['agente'])} · escopo: {escopo}")


def linha_producao(prod):
    """Resumo de uma linha: 'M0 humano 35 PFO (65%) · M2 IA dirigida 15 PFO (28%) · aceitos 54/54'."""
    total = prod["total"]
    partes = [f"{NOME_MODO[m]} {v['pfo']} PFO ({pct(v['pfo'], total):.0f}%)"
              for m, v in prod["por_modo"].items() if v["pfo"]]
    ac = prod["aceite"]
    if total - ac["sem_aceite"] > 0:
        partes.append(f"aceitos {ac['aceito']}/{total}")
    return " · ".join(partes)


def md_producao(prod, indicadores, abrange, unidade="PFO"):
    out = ["## Produção\n"]
    out.append(f"| Modo de produção | Processos | {unidade} | % |\n|---|---|---|---|")
    total = prod["total"]
    for m, v in prod["por_modo"].items():
        if v["pfo"] or m != MODO_ND:
            out.append(f"| {NOME_MODO[m]} | {v['processos']} | {v['pfo']} | {pct(v['pfo'], total):.0f}% |")
    ac = prod["aceite"]
    if total - ac["sem_aceite"] > 0:
        out.append(f"\nAceite: **{ac['aceito']} {unidade} aceitos** ({pct(ac['aceito'], total):.0f}%) · "
                   f"{ac['pendente']} pendentes · {ac['rejeitado']} rejeitados · {ac['sem_aceite']} sem registro")
    if indicadores:
        moeda = indicadores["moeda"] or "unid."
        out.append(f"\n### Indicadores de produção (abrange: {'o software' if indicadores['abrange'] == 'software' else 'a mudança'}"
                   + (f", período {indicadores['periodo']}" if indicadores.get("periodo") else "") + ")\n")
        out.append("| Indicador | Valor |\n|---|---|")
        out.append(f"| {unidade} produzidos | {indicadores['pfo_produzidos']} |")
        if indicadores["horas_humanas"] is not None:
            out.append(f"| Horas humanas (todo o ciclo) | {fmt_num(indicadores['horas_humanas'], 1)} |")
        if indicadores["alavancagem"] is not None:
            out.append(f"| Alavancagem humana ({unidade} por hora humana) | {fmt_num(indicadores['alavancagem'])} |")
        if indicadores["custo_total"] is not None:
            out.append(f"| Custo total ({moeda}) | {fmt_num(indicadores['custo_total'])} |")
        if indicadores["custo_por_pfo"] is not None:
            out.append(f"| Custo por {unidade} ({moeda}) | {fmt_num(indicadores['custo_por_pfo'])} |")
        if indicadores["custo_ia_por_pfo"] is not None:
            out.append(f"| Custo de IA por {unidade} ({moeda}) | {fmt_num(indicadores['custo_ia_por_pfo'])} |")
        if indicadores["participacao_ia"] is not None:
            out.append(f"| Participação da IA no custo | {100 * indicadores['participacao_ia']:.0f}% |")
    elif abrange == "mudanca" and unidade == "PFO":
        out.append("\nOs dados de produção deste modelo abrangem a mudança em relação à versão anterior; "
                   "os indicadores são calculados por `mudanca`.")
    elif abrange == "software" and unidade != "PFO":
        out.append("\nOs dados de produção deste modelo abrangem o software inteiro; "
                   "os indicadores são calculados por `contar`.")
    return "\n".join(out) + "\n"


def relatorio_md(rel):
    p = rel["perfil"]
    out = []
    titulo = rel["software"] + (f" {rel['versao']}" if rel["versao"] else "")
    out.append(f"# Relatório MFO — {titulo}\n")
    out.append(f"**Rótulo:** {rel['rotulo']}\n")
    if rel["producao"]["declarado"]:
        out.append(f"**Produção:** {linha_producao(rel['producao'])}\n")
    if rel.get("estimativa"):
        e = rel["estimativa"]
        out.append(f"**Estimativa:** nível {e.get('nivel')} · {e.get('pfo_min')} a {e.get('pfo_max')} PFO · base: {e.get('base')}\n")
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
    com_prod = rel["producao"]["declarado"]
    cab = "| ID | Processo | E | X | R | W | PFO | Deriv. | Evid. |" + (" Modo | Aceite |" if com_prod else "")
    out.append(cab + "\n|---|---|---|---|---|---|---|---|---|" + ("---|---|" if com_prod else ""))
    for l in rel["processos"]:
        d = {True: "sim", False: "não", None: "n/d"}[l["derivacao"]]
        linha = f"| {l['id']} | {l['nome']} | {l['E']} | {l['X']} | {l['R']} | {l['W']} | **{l['pfo']}** | {d} | {l['evidenciados']}/{l['pfo']} |"
        if com_prod:
            linha += f" {l['modo']} | {l['aceite'] or '—'} |"
        out.append(linha)
    out.append(f"| | **Total** | {p['E']} | {p['X']} | {p['R']} | {p['W']} | **{p['PFO']}** | | |" + (" | |" if com_prod else ""))
    if com_prod:
        out.append("")
        out.append(md_producao(rel["producao"], rel["indicadores_producao"], rel["producao_abrange"]))
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
    # produção da mudança: modo do processo no modelo posterior; processos removidos ficam 'nd'
    pfo_mud_por_processo = Counter()
    for (pid, _, _) in incluidos + alterados + excluidos:
        pfo_mud_por_processo[pid] += 1
    producao = resumo_producao(depois, dict(pfo_mud_por_processo))
    pm = depois.get("producao")
    indicadores = indicadores_producao(pm, total) if isinstance(pm, dict) and pm.get("abrange") == "mudanca" else None
    return {
        "de": f"{antes['software']} {antes.get('versao', '')}".strip(),
        "para": f"{depois['software']} {depois.get('versao', '')}".strip(),
        "niveis": f"{antes['nivel']} → {depois['nivel']}",
        "pfo_mudanca": total,
        "incluidos": incluidos, "alterados": alterados, "excluidos": excluidos,
        "processos_novos": sorted(pb - pa), "processos_removidos": sorted(pa - pb),
        "pfo_antes": len(ka), "pfo_depois": len(kb),
        "rotulo": rotulo(depois, total, pct(evid, total) if total else 100.0, prefixo=prefixo),
        "producao": producao, "indicadores_producao": indicadores,
        "producao_abrange": pm.get("abrange") if isinstance(pm, dict) else None,
    }


def mudanca_md(r):
    out = [f"# Mudança MFO — {r['de']} → {r['para']}\n", f"**Rótulo:** {r['rotulo']}\n"]
    if r["producao"]["declarado"]:
        out.append(f"**Produção da mudança:** {linha_producao(r['producao'])}\n")
    out.append(f"Tamanho anterior: {r['pfo_antes']} PFO · tamanho posterior: {r['pfo_depois']} PFO · níveis: {r['niveis']}\n")
    for titulo, chaves in (("Incluídos", r["incluidos"]), ("Alterados", r["alterados"]), ("Excluídos", r["excluidos"])):
        out.append(f"## {titulo} ({len(chaves)})\n")
        out.extend(f"- {pid} · {t} {e}" for pid, t, e in chaves)
        if not chaves:
            out.append("- (nenhum)")
        out.append("")
    if r["processos_novos"] or r["processos_removidos"]:
        out.append(f"Processos novos: {', '.join(r['processos_novos']) or '—'} · processos removidos: {', '.join(r['processos_removidos']) or '—'}\n")
    if r["producao"]["declarado"]:
        out.append(md_producao(r["producao"], r["indicadores_producao"], r["producao_abrange"], unidade="PFO de mudança"))
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
# código e diff (capítulo 8): impacto e auditoria de evidências
# ---------------------------------------------------------------------------

def _separar_evidencia(ev):
    """'FONTE:caminho#trecho@versao' -> (fonte, caminho, trecho). '@versao' é ignorado."""
    fonte, loc = ev.split(":", 1)
    loc = loc.split("@", 1)[0]
    caminho, _, trecho = loc.partition("#")
    return fonte, caminho.strip(), trecho.strip()


def _elementos_com_evidencia(modelo):
    """Gera (rotulo_do_elemento, elemento) para tudo que pode carregar 'evidencia'."""
    for e in modelo.get("entidades") or []:
        yield f"entidade {e.get('id')}", e
    for p in modelo.get("processos") or []:
        pid = p.get("id")
        yield f"{pid}", p
        for m in p.get("movimentos") or []:
            yield f"{pid} · {m.get('tipo')} {m.get('entidade')}", m
        if isinstance(p.get("producao"), dict):
            yield f"{pid} · produção", p["producao"]
        if isinstance(p.get("aceite"), dict):
            yield f"{pid} · aceite", p["aceite"]
    if isinstance(modelo.get("producao"), dict):
        yield "produção do modelo", modelo["producao"]


def auditar(modelo, raiz, fontes_verificaveis):
    """RD-03: cada evidência 'FONTE:caminho#trecho' das fontes indicadas deve apontar para um arquivo
    existente sob 'raiz' que contenha o trecho. Devolve o resultado por evidência."""
    verificadas, nao_encontradas, ignoradas = [], [], 0
    for rotulo, elem in _elementos_com_evidencia(modelo):
        for ev in elem.get("evidencia") or []:
            if not isinstance(ev, str) or ":" not in ev:
                continue
            fonte, caminho, trecho = _separar_evidencia(ev)
            if fonte not in fontes_verificaveis:
                ignoradas += 1
                continue
            arquivo = os.path.join(raiz, caminho)
            if not os.path.isfile(arquivo):
                nao_encontradas.append((rotulo, ev, "arquivo inexistente"))
                continue
            if trecho:
                with open(arquivo, encoding="utf-8", errors="replace") as f:
                    if trecho not in f.read():
                        nao_encontradas.append((rotulo, ev, "trecho não encontrado no arquivo"))
                        continue
            verificadas.append((rotulo, ev))
    total = len(verificadas) + len(nao_encontradas)
    return {"raiz": raiz, "fontes": sorted(fontes_verificaveis), "total": total, "verificadas": len(verificadas),
            "nao_encontradas": nao_encontradas, "ignoradas": ignoradas,
            "taxa": (len(verificadas) / total) if total else None}


def auditar_md(r, nome_modelo):
    out = [f"# Auditoria de evidências — {nome_modelo}\n"]
    out.append(f"Raiz: `{r['raiz']}` · fontes verificadas: {', '.join(r['fontes'])} · evidências de outras fontes ignoradas: {r['ignoradas']}\n")
    if r["total"] == 0:
        out.append("Nenhuma evidência das fontes indicadas no modelo.\n")
        return "\n".join(out)
    out.append(f"**{r['verificadas']} de {r['total']} evidências verificadas ({100 * r['taxa']:.0f}%)**\n")
    if r["nao_encontradas"]:
        out.append("## Não encontradas\n")
        out.extend(f"- {rot}: `{ev}` — {motivo}" for rot, ev, motivo in r["nao_encontradas"])
        out.append("")
    return "\n".join(out)


def _arvore(diretorio):
    out = {}
    for root, dirs, files in os.walk(diretorio):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
        for f in files:
            if f.endswith((".pyc", ".pyo")):
                continue
            caminho = os.path.join(root, f)
            out[os.path.relpath(caminho, diretorio).replace(os.sep, "/")] = caminho
    return out


def _ler(caminho):
    with open(caminho, encoding="utf-8", errors="replace") as f:
        return f.read()


def diff_dirs(a, b):
    """{caminho relativo: (status A/D/M, conteudo_antes, conteudo_depois)} entre dois diretórios."""
    ta, tb = _arvore(a), _arvore(b)
    mud = {}
    for rel in sorted(set(ta) | set(tb)):
        if rel not in ta:
            mud[rel] = ("A", None, _ler(tb[rel]))
        elif rel not in tb:
            mud[rel] = ("D", _ler(ta[rel]), None)
        else:
            ca, cb = _ler(ta[rel]), _ler(tb[rel])
            if ca != cb:
                mud[rel] = ("M", ca, cb)
    return mud


def diff_git(repo, ref_a, ref_b):
    """Mesma estrutura de diff_dirs, a partir de 'git diff --name-status'."""
    saida = subprocess.check_output(["git", "-C", repo, "diff", "--name-status", ref_a, ref_b], text=True)

    def mostrar(ref, rel):
        try:
            return subprocess.check_output(["git", "-C", repo, "show", f"{ref}:{rel}"], text=True, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            return None

    mud = {}
    for linha in saida.splitlines():
        partes = linha.split("\t")
        if len(partes) < 2:
            continue
        st, rel = partes[0][0], partes[-1]
        if st == "A":
            mud[rel] = ("A", None, mostrar(ref_b, rel))
        elif st == "D":
            mud[rel] = ("D", mostrar(ref_a, rel), None)
        else:
            mud[rel] = ("M", mostrar(ref_a, rel), mostrar(ref_b, rel))
    return mud


def bloco(texto, trecho):
    """Bloco de código iniciado na primeira linha que contém o trecho, delimitado por indentação
    (heurística independente de linguagem). Devolve o texto normalizado ou None."""
    if texto is None:
        return None
    linhas = texto.splitlines()
    for i, l in enumerate(linhas):
        if trecho in l:
            ind = len(l) - len(l.lstrip())
            abre_bloco = l.rstrip().endswith(("{", "(", "["))  # linguagens com chaves: inclui a linha de fechamento
            fim = i + 1
            while fim < len(linhas):
                m = linhas[fim]
                if m.strip():
                    if len(m) - len(m.lstrip()) <= ind:
                        if abre_bloco and m.strip().startswith(("}", ")", "]", "end")):
                            fim += 1
                        break
                fim += 1
            return "\n".join(x.strip() for x in linhas[i:fim] if x.strip())
    return None


def _contar_linhas_diff(antes, depois):
    mais = menos = 0
    for l in difflib.unified_diff((antes or "").splitlines(), (depois or "").splitlines(), lineterm="", n=0):
        if l.startswith("+") and not l.startswith("+++"):
            mais += 1
        elif l.startswith("-") and not l.startswith("---"):
            menos += 1
    return mais, menos


def impacto(modelo, mudancas, fonte, prefixos=()):
    """Cruza as evidências de código do modelo com os arquivos alterados em um diff.
    Classifica cada processo como 'não afetado', 'afetado (arquivo)' ou 'afetado (trecho)'."""

    def normalizar_caminho(c):
        for pre in prefixos:
            if pre and c.startswith(pre.rstrip("/") + "/"):
                return c[len(pre.rstrip("/")) + 1:]
        return c

    citacoes = {rel: set() for rel in mudancas}
    for e in modelo.get("entidades") or []:
        for ev in e.get("evidencia") or []:
            if isinstance(ev, str) and ":" in ev:
                f, caminho, _ = _separar_evidencia(ev)
                rel = normalizar_caminho(caminho)
                if f == fonte and rel in mudancas:
                    citacoes[rel].add(f"entidade {e['id']}")
    processos = []
    for p in modelo["processos"]:
        situacao, trechos, candidatos = "não afetado", [], []

        def avaliar(elem, rotulo):
            nonlocal situacao
            for ev in elem.get("evidencia") or []:
                if not isinstance(ev, str) or ":" not in ev:
                    continue
                f, caminho, trecho = _separar_evidencia(ev)
                if f != fonte:
                    continue
                rel = normalizar_caminho(caminho)
                if rel not in mudancas:
                    continue
                citacoes[rel].add(p["id"])
                st, antes, depois = mudancas[rel]
                if trecho and st == "M":
                    ba, bd = bloco(antes, trecho), bloco(depois, trecho)
                    if ba == bd:
                        if situacao == "não afetado":
                            situacao = "afetado (arquivo)"
                        continue
                    situacao = "afetado (trecho)"
                    estado = "novo" if ba is None else ("removido" if bd is None else "alterado")
                    trechos.append(f"{rel}#{trecho} ({estado})")
                    if rotulo:
                        candidatos.append(f"{rotulo} ({estado})")
                else:
                    if situacao == "não afetado":
                        situacao = "afetado (arquivo)"
                    if st in ("A", "D"):
                        situacao = "afetado (trecho)"
                        trechos.append(f"{rel} (arquivo {'novo' if st == 'A' else 'removido'})")

        avaliar(p, "")
        for m in p.get("movimentos") or []:
            avaliar(m, f"{m.get('tipo')} {m.get('entidade')}")
        processos.append({"id": p["id"], "nome": p.get("nome", ""), "situacao": situacao,
                          "trechos": sorted(set(trechos)), "candidatos": sorted(set(candidatos))})
    arquivos = []
    for rel, (st, antes, depois) in mudancas.items():
        mais, menos = _contar_linhas_diff(antes, depois)
        arquivos.append({"arquivo": rel, "status": st, "mais": mais, "menos": menos, "processos": sorted(citacoes[rel])})
    return {"fonte": fonte, "arquivos": arquivos, "processos": processos,
            "sem_processo": [a["arquivo"] for a in arquivos if not a["processos"]]}


def impacto_md(r, titulo):
    out = [f"# Impacto do diff — {titulo}\n"]
    st = Counter(a["status"] for a in r["arquivos"])
    out.append(f"Arquivos alterados: {len(r['arquivos'])} (M {st['M']}, A {st['A']}, D {st['D']}) · fonte de evidências: {r['fonte']}\n")
    out.append("| Arquivo | Status | Linhas +/− | Processos e entidades que o citam |\n|---|---|---|---|")
    for a in r["arquivos"]:
        out.append(f"| {a['arquivo']} | {a['status']} | +{a['mais']}/−{a['menos']} | {', '.join(a['processos']) or '—'} |")
    out.append("\n## Processos\n")
    out.append("| Processo | Situação | Trechos citados com mudança | Movimentos candidatos a 'alterado' |\n|---|---|---|---|")
    for p in r["processos"]:
        out.append(f"| {p['id']} {p['nome']} | {p['situacao']} | {'; '.join(p['trechos']) or '—'} | {'; '.join(p['candidatos']) or '—'} |")
    afetados = [p["id"] for p in r["processos"] if p["situacao"] != "não afetado"]
    fortes = [p["id"] for p in r["processos"] if p["situacao"] == "afetado (trecho)"]
    out.append("\n## Resumo\n")
    out.append(f"- Re-extrair e marcar movimentos conforme RD-01: {', '.join(fortes) or 'nenhum'}")
    out.append(f"- Afetados apenas por arquivo (confirmar na extração): {', '.join(sorted(set(afetados) - set(fortes))) or 'nenhum'}")
    out.append(f"- Arquivos alterados sem processo nem entidade associados (procurar pontos de entrada novos): {', '.join(r['sem_processo']) or 'nenhum'}")
    out.append("- Pontos de entrada novos não aparecem aqui: são identificados na extração da versão posterior (RD-02).\n")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# estimativa (capítulo 11): perfis típicos por tipo de processo e estimativa a partir de backlog
# ---------------------------------------------------------------------------

TIPOS_PROCESSO = ("criar", "alterar", "excluir", "estado", "consultar", "relatorio", "processar", "integrar", "outro")
VERBOS = {
    "criar": "cadastrar criar registrar incluir convidar abrir emitir lancar solicitar importar adicionar inserir",
    "alterar": "alterar editar atualizar configurar definir trocar redefinir transferir conceder revogar preparar conduzir ajustar",
    "excluir": "excluir remover apagar",
    "estado": "cancelar desativar reativar ativar aprovar reprovar homologar autorizar suspender encerrar concluir iniciar aceitar responder bloquear desbloquear",
    "consultar": "pesquisar consultar listar buscar visualizar acompanhar exibir detalhar carregar ver",
    "relatorio": "relatorio exportar imprimir",
    "processar": "processar gerar executar calcular notificar enviar sincronizar materializar recuperar validar",
    "integrar": "receber publicar consumir integrar",
}
INTERVALO_PADRAO = {"E0": 40, "E1": 25, "E2": 10}  # ±% quando não há perfis calibrados (RE-03)


def tipo_processo(p):
    """Tipo declarado em 'tipo_processo' ou inferido pelo verbo que abre o nome (RE-01)."""
    t = p.get("tipo_processo")
    if t in TIPOS_PROCESSO:
        return t
    palavras = normalizar(p.get("nome", "")).split()
    verbo = palavras[0] if palavras else ""
    for tipo, verbos in VERBOS.items():
        if verbo in verbos.split():
            return tipo
    return "outro"


def movimentos_tipicos(tipo, principal, extras):
    """RE-01: movimentos do perfil típico (capítulo 2, casos frequentes) para um processo
    com entidade principal e entidades adicionais tocadas."""
    P = principal
    if tipo in ("criar", "alterar", "estado", "integrar", "outro"):
        base = [("E", P), ("R", P), ("W", P), ("X", "MENSAGEM")]
        extra = [("R", e) for e in extras]
    elif tipo == "excluir":
        base = [("E", P), ("W", P), ("X", "MENSAGEM")]
        extra = [("R", e) for e in extras]           # dependentes verificados
    elif tipo == "consultar":
        base = [("E", P), ("R", P), ("X", P), ("X", "MENSAGEM")]
        extra = [m for e in extras for m in (("R", e), ("X", e))]
    elif tipo == "relatorio":
        base = [("E", "DISPARO"), ("R", P), ("X", P), ("X", "MENSAGEM")]
        extra = [m for e in extras for m in (("R", e), ("X", e))]
    else:  # processar: automação disparada por evento ou relógio
        base = [("E", "DISPARO"), ("R", P), ("W", P)]
        extra = [("R", e) for e in extras]
    vistos, out = set(), []
    for m in base + extra:
        if m not in vistos:
            vistos.add(m)
            out.append(m)
    return out


def perfis(modelos):
    """RE-02: PFO por tipo de processo (n, mediana, p25, p75, média) a partir de modelos medidos."""
    por_tipo = {}
    for nome, modelo in modelos:
        for p in modelo["processos"]:
            por_tipo.setdefault(tipo_processo(p), []).append(len(p["movimentos"]))
    saida = {}
    todos = []
    for tipo, valores in por_tipo.items():
        v = sorted(valores)
        todos += v
        q = statistics.quantiles(v, n=4) if len(v) >= 2 else [v[0], v[0], v[0]]
        saida[tipo] = {"n": len(v), "mediana": statistics.median(v), "p25": q[0], "p75": q[2],
                       "media": statistics.mean(v), "min": v[0], "max": v[-1]}
    v = sorted(todos)
    q = statistics.quantiles(v, n=4) if len(v) >= 2 else [v[0], v[0], v[0]]
    return {"origem": [nome for nome, _ in modelos], "n_processos": len(v),
            "geral": {"n": len(v), "mediana": statistics.median(v), "p25": q[0], "p75": q[2],
                      "media": statistics.mean(v), "min": v[0], "max": v[-1]},
            "perfis": dict(sorted(saida.items()))}


def perfis_md(r):
    out = [f"# Perfis típicos — {len(r['origem'])} modelo(s), {r['n_processos']} processos\n"]
    out.append("| Tipo de processo | n | Mediana | P25 | P75 | Média | Mín | Máx |\n|---|---|---|---|---|---|---|---|")
    for tipo, v in r["perfis"].items():
        out.append(f"| {tipo} | {v['n']} | {fmt_num(v['mediana'], 1)} | {fmt_num(v['p25'], 1)} | {fmt_num(v['p75'], 1)} | {fmt_num(v['media'], 1)} | {v['min']} | {v['max']} |")
    g = r["geral"]
    out.append(f"| **geral** | {g['n']} | {fmt_num(g['mediana'], 1)} | {fmt_num(g['p25'], 1)} | {fmt_num(g['p75'], 1)} | {fmt_num(g['media'], 1)} | {g['min']} | {g['max']} |")
    out.append("\nOrigem: " + ", ".join(r["origem"]) + "\n")
    return "\n".join(out)


def _expandir_itens(itens):
    """Item com 'crud': true vira os quatro processos de manutenção da entidade (E0)."""
    out = []
    for i, item in enumerate(itens, 1):
        if item.get("crud"):
            ent = item.get("entidade") or (item.get("entidades") or ["Entidade"])[0]
            base_id = item.get("id") or ent
            for sufixo, tipo, verbo in (("C", "criar", "Cadastrar"), ("A", "alterar", "Alterar"), ("E", "excluir", "Excluir"), ("L", "consultar", "Consultar")):
                out.append({"id": f"{base_id}-{sufixo}", "nome": f"{verbo} {ent}", "tipo": tipo,
                            "entidades": [ent] + list(item.get("extras") or [])})
        else:
            item = dict(item)
            item.setdefault("id", f"I{i:02d}")
            out.append(item)
    return out


def estimar(backlog, perfis_calibrados=None):
    """RE-01 e RE-03: modelo estimado (movimentos inferidos pelo perfil típico) a partir de um backlog."""
    nivel = backlog.get("nivel_estimativa", "E1")
    fonte = backlog.get("fonte") or {"id": "BKL", "tipo": "requisitos", "ref": "backlog"}
    itens = _expandir_itens(backlog.get("itens") or [])
    entidades, processos = {}, []
    for item in itens:
        ents = list(item.get("entidades") or [])
        principal = ents[0] if ents else f"Entidade-{item['id']}"
        extras = ents[1:]
        p = {"id": item["id"], "nome": item.get("nome") or item["id"]}
        tipo = item.get("tipo") if item.get("tipo") in TIPOS_PROCESSO else tipo_processo(p)
        uf = "UF-RELOGIO" if tipo == "processar" else ("UF-SISTEMA" if tipo == "integrar" else "UF-PESSOA")
        movs = []
        for t, e in movimentos_tipicos(tipo, principal, extras):
            movs.append({"tipo": t, "entidade": e, "inferido": True,
                         "justificativa": f"perfil típico '{tipo}' ({nivel}); confirmar na extração"})
            if e not in RESERVADAS:
                entidades.setdefault(e, []).append(item["id"])
        processos.append({"id": item["id"], "nome": p["nome"], "tipo_processo": tipo,
                          "disparadores": [{"usuario": uf, "evento": item.get("evento") or f"item de backlog {item['id']}"}],
                          "evidencia": [f"{fonte['id']}:{item.get('ref') or item['id']}"],
                          "movimentos": movs})
    for ent in backlog.get("entidades") or []:
        entidades.setdefault(ent, [])
    ufs = sorted({d["usuario"] for p in processos for d in p["disparadores"]})
    modelo = {
        "mfo": VERSAO_METODO,
        "software": backlog.get("software", "software"),
        "versao": backlog.get("versao", ""),
        "proposito": backlog.get("proposito", "Estimar o tamanho funcional a partir do backlog"),
        "escopo": backlog.get("escopo", f"{len(processos)} itens de backlog"),
        "nivel": "R",
        "agente": backlog.get("agente") or {"tipo": "ferramenta", "nome": f"mfo.py estimar {VERSAO_METODO}", "revisao_humana": False},
        "fontes": [fonte],
        "usuarios_funcionais": [UF_ESTIMATIVA[k] for k in ("UF-PESSOA", "UF-SISTEMA", "UF-RELOGIO") if k in ufs],
        "entidades": [{"id": e, "inferido": True, "justificativa": "citada no backlog" if not itens_ids else f"itens {', '.join(itens_ids)}"}
                      for e, itens_ids in sorted(entidades.items())],
        "processos": processos,
    }
    # entidades não referenciadas por movimento violariam V-04: só entram as tocadas
    tocadas = {m["entidade"] for p in processos for m in p["movimentos"]}
    modelo["entidades"] = [e for e in modelo["entidades"] if e["id"] in tocadas]
    pfo = sum(len(p["movimentos"]) for p in processos)
    est = {"nivel": nivel, "pfo_modelo": pfo, "fator_calibracao": 1.0, "pfo_calibrado": pfo}
    if perfis_calibrados:
        tipos = [p["tipo_processo"] for p in processos]
        pf = perfis_calibrados["perfis"]
        g = perfis_calibrados["geral"]
        med = sum(pf.get(t, g)["mediana"] for t in tipos)
        lo = sum(pf.get(t, g)["p25"] for t in tipos)
        hi = sum(pf.get(t, g)["p75"] for t in tipos)
        est.update({"fator_calibracao": (med / pfo) if pfo else 1.0, "pfo_calibrado": round(med),
                    "pfo_min": round(lo), "pfo_max": round(hi),
                    "base": f"perfis de {perfis_calibrados['n_processos']} processos medidos ({', '.join(perfis_calibrados['origem'])})"})
    else:
        pct = INTERVALO_PADRAO.get(nivel, 25)
        est.update({"intervalo_pct": pct, "pfo_min": round(pfo * (1 - pct / 100)), "pfo_max": round(pfo * (1 + pct / 100)),
                    "base": "perfis padrão do capítulo 11 (sem calibração local)"})
    modelo["estimativa"] = est
    return modelo


UF_ESTIMATIVA = {
    "UF-PESSOA": {"id": "UF-PESSOA", "nome": "Usuário (pessoa)", "tipo": "pessoa"},
    "UF-SISTEMA": {"id": "UF-SISTEMA", "nome": "Sistema externo", "tipo": "sistema"},
    "UF-RELOGIO": {"id": "UF-RELOGIO", "nome": "Agendador ou evento", "tipo": "relogio"},
}


def estimativa_md(modelo, medido=None):
    e = modelo["estimativa"]
    out = [f"# Estimativa MFO — {modelo['software']} {modelo.get('versao', '')}".rstrip() + "\n"]
    out.append(f"**Rótulo:** {rotulo(modelo, e['pfo_calibrado'], 0.0)}\n")
    out.append("| Indicador | Valor |\n|---|---|")
    out.append(f"| Nível da estimativa | {e['nivel']} |")
    out.append(f"| Processos estimados | {len(modelo['processos'])} |")
    out.append(f"| PFO do modelo (perfis típicos) | {e['pfo_modelo']} |")
    if e.get("fator_calibracao", 1.0) != 1.0:
        out.append(f"| Fator de calibração | {fmt_num(e['fator_calibracao'])} |")
        out.append(f"| PFO calibrado | **{e['pfo_calibrado']}** |")
    out.append(f"| Intervalo | {e['pfo_min']} a {e['pfo_max']} PFO |")
    out.append(f"| Base | {e['base']} |")
    if medido is not None:
        erro = abs(e["pfo_calibrado"] - medido) / medido if medido else 0
        out.append(f"| Medido (para conferência) | {medido} PFO · erro relativo {100 * erro:.0f}% |")
    out.append("\n## Itens\n")
    out.append("| ID | Processo | Tipo | Entidades | PFO |\n|---|---|---|---|---|")
    for p in modelo["processos"]:
        ents = sorted({m["entidade"] for m in p["movimentos"] if m["entidade"] not in RESERVADAS})
        out.append(f"| {p['id']} | {p['nome']} | {p['tipo_processo']} | {', '.join(ents)} | {len(p['movimentos'])} |")
    out.append("\nTodos os movimentos estão marcados como inferidos (evidência 0%); a extração substitui cada um por evidência conforme os artefatos surgem.\n")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# linha de comando
# ---------------------------------------------------------------------------

def _listas(d, *campos):
    d = dict(d)
    for c in campos:
        d[c] = [list(k) for k in d[c]]
    return d


def main(argv=None):
    ap = argparse.ArgumentParser(prog="mfo.py", description="Ferramenta de referência do método MFO 1.0")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("validar", help="valida um Modelo Funcional Canônico (V-01 a V-10)")
    s.add_argument("modelo")

    s = sub.add_parser("contar", help="calcula PFO, perfil funcional, produção e rótulo")
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

    s = sub.add_parser("impacto", help="processos afetados por um diff de código (capítulo 8)")
    s.add_argument("modelo")
    g = s.add_mutually_exclusive_group(required=True)
    g.add_argument("--dirs", nargs=2, metavar=("ANTES", "DEPOIS"), help="dois diretórios com as versões")
    g.add_argument("--git", nargs=3, metavar=("REPO", "REF_ANTES", "REF_DEPOIS"), help="repositório git e duas referências")
    s.add_argument("--fonte", default="COD", help="prefixo das evidências de código (padrão: COD)")
    s.add_argument("--json", action="store_true")

    s = sub.add_parser("auditar", help="confere se cada evidência de código existe (RD-03)")
    s.add_argument("modelo")
    s.add_argument("--raiz", required=True, help="diretório base dos caminhos das evidências")
    s.add_argument("--fonte", action="append", help="prefixo de fonte a verificar (repetível; padrão: COD)")
    s.add_argument("--json", action="store_true")

    s = sub.add_parser("perfis", help="PFO típico por tipo de processo a partir de modelos medidos (RE-02)")
    s.add_argument("modelos", nargs="+")
    s.add_argument("-o", "--saida", help="grava os perfis em JSON para uso em 'estimar --perfis'")
    s.add_argument("--json", action="store_true")

    s = sub.add_parser("estimar", help="estimativa E0/E1 a partir de um backlog (RE-01, RE-03)")
    s.add_argument("backlog")
    s.add_argument("--perfis", help="perfis calibrados gerados por 'perfis -o'")
    s.add_argument("--medido", help="modelo medido do mesmo escopo, para calcular o erro da estimativa")
    s.add_argument("-o", "--saida", help="grava o modelo estimado (MFC com movimentos inferidos)")
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
            print(json.dumps(_listas(r, "incluidos", "alterados", "excluidos"), ensure_ascii=False, indent=2))
        else:
            print(mudanca_md(r))
        return 0

    if args.cmd == "concordancia":
        a, b = carregar(args.a), carregar(args.b)
        exigir_valido(a, args.a)
        exigir_valido(b, args.b)
        r = concordancia(a, b)
        if args.json:
            print(json.dumps(_listas(r, "so_em_a", "so_em_b"), ensure_ascii=False, indent=2))
        else:
            print(concordancia_md(r, args.a, args.b))
        return 0

    if args.cmd == "impacto":
        modelo = carregar(args.modelo)
        exigir_valido(modelo, args.modelo)
        if args.dirs:
            antes, depois = args.dirs
            mud = diff_dirs(antes, depois)
            prefixos = (os.path.basename(os.path.normpath(depois)), os.path.basename(os.path.normpath(antes)))
            titulo = f"{antes} → {depois}"
        else:
            repo, ra, rb = args.git
            mud = diff_git(repo, ra, rb)
            prefixos = ()
            titulo = f"{repo}: {ra} → {rb}"
        r = impacto(modelo, mud, args.fonte, prefixos)
        if args.json:
            print(json.dumps(r, ensure_ascii=False, indent=2))
        else:
            print(impacto_md(r, f"{titulo} (modelo: {modelo['software']} {modelo.get('versao', '')})"))
        return 0

    if args.cmd == "auditar":
        modelo = carregar(args.modelo)
        exigir_valido(modelo, args.modelo)
        r = auditar(modelo, args.raiz, set(args.fonte or ["COD"]))
        if args.json:
            print(json.dumps(r, ensure_ascii=False, indent=2))
        else:
            print(auditar_md(r, f"{modelo['software']} {modelo.get('versao', '')}"))
        return 1 if r["nao_encontradas"] else 0

    if args.cmd == "perfis":
        modelos = []
        for caminho in args.modelos:
            m = carregar(caminho)
            exigir_valido(m, caminho)
            modelos.append((os.path.basename(caminho), m))
        r = perfis(modelos)
        if args.saida:
            with open(args.saida, "w", encoding="utf-8") as f:
                json.dump(r, f, ensure_ascii=False, indent=2)
        if args.json:
            print(json.dumps(r, ensure_ascii=False, indent=2))
        else:
            print(perfis_md(r))
        return 0

    if args.cmd == "estimar":
        backlog = carregar(args.backlog)
        pc = carregar(args.perfis) if args.perfis else None
        modelo = estimar(backlog, pc)
        erros, _ = validar(modelo)
        if erros:
            print("Backlog produziu modelo inválido:", file=sys.stderr)
            for e in erros:
                print(f"  - {e}", file=sys.stderr)
            return 1
        medido = None
        if args.medido:
            mm = carregar(args.medido)
            exigir_valido(mm, args.medido)
            medido = sum(len(p["movimentos"]) for p in mm["processos"])
        if args.saida:
            with open(args.saida, "w", encoding="utf-8") as f:
                json.dump(modelo, f, ensure_ascii=False, indent=2)
        if args.json:
            print(json.dumps(dict(modelo["estimativa"], medido=medido), ensure_ascii=False, indent=2))
        else:
            print(estimativa_md(modelo, medido))
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
