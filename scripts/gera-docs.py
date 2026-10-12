#!/usr/bin/env python3
"""gera-docs.py — gera as páginas do site (docs/content/*.md) a partir da fonte Markdown.

A fonte é a especificação (PFC/*.md), o prompt de extração, os exemplos em Markdown
e os índices dos manuais de referência; as páginas em docs/content são derivadas e não
se editam à mão. O script reescreve os links: capítulo ou documento do PFC vira rota
`#/pagina` do site; arquivo que não é página vira link para o GitHub.

Uso, a partir da raiz do repositório:
  python3 scripts/gera-docs.py           # escreve docs/content/*.md
  python3 scripts/gera-docs.py --check   # não escreve; sai com 1 se o site está desatualizado

O --check também confere que toda página citada em docs/config.js existe e que a versão
do selo (config.js) é a do arquivo VERSION.
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONTENT = RAIZ / "docs" / "content"
CONFIG = RAIZ / "docs" / "config.js"
REPO = "https://github.com/andromarcio/metricas-software"
BRANCH = "main"

# Páginas com identificador próprio (as do menu). As demais páginas do PFC alcançadas
# por link recebem o identificador derivado do caminho (exemplos-aval-relatorio-aval-5.0.0).
PAGINAS = {
    "introducao": "PFC/README.md",
    "repositorio": "README.md",
    "prompt-extracao": "PFC/prompts/extracao-mfc.md",
    "exemplo-cartao": "PFC/exemplos/cartao/autorizacao-requisitos.md",
    "exemplo-codigo": "PFC/exemplos/codigo-biblioteca/README.md",
    "apf": "APF/README.md",
    "cosmic": "COSMIC/README.md",
    "sti": "STI/README.md",
}
for cap in sorted((RAIZ / "PFC").glob("[0-9][0-9]-*.md")):
    PAGINAS[cap.stem[3:]] = f"PFC/{cap.name}"

# Só os documentos do PFC entram no site por fechamento de links; os manuais de
# referência (APF, COSMIC, STI) ficam no GitHub, com o índice de cada um como página.
FECHAMENTO = re.compile(r"^PFC/.*\.md$")

LINK = re.compile(r"\]\(([^)\s]+)\)")
CERCA = re.compile(r"^\s*(```|~~~)")


def id_automatico(rel):
    return re.sub(r"[^a-z0-9.]+", "-", rel[:-3].lower()).strip("-")


def rel_de(src, alvo):
    """Caminho relativo à raiz do repositório para um link relativo ao arquivo fonte."""
    base = (RAIZ / src).parent
    try:
        return (base / alvo).resolve().relative_to(RAIZ).as_posix()
    except ValueError:
        return None


def gerar():
    """Devolve {id_pagina: conteudo} e a lista de avisos (links que não resolvem)."""
    por_fonte = {v: k for k, v in PAGINAS.items()}
    fila = list(PAGINAS.items())
    saida, avisos = {}, []
    while fila:
        pid, src = fila.pop(0)
        texto = (RAIZ / src).read_text(encoding="utf-8")
        linhas, em_cerca = [], False
        for linha in texto.splitlines():
            if CERCA.match(linha):
                em_cerca = not em_cerca
            if em_cerca:
                linhas.append(linha)
                continue

            def troca(m):
                alvo = m.group(1)
                if alvo.startswith(("http://", "https://", "mailto:", "#")):
                    return m.group(0)
                caminho, _, ancora = alvo.partition("#")
                rel = rel_de(src, caminho)
                if rel is None or not (RAIZ / rel).exists():
                    avisos.append(f"{src}: link para '{alvo}' não resolve")
                    return m.group(0)
                if (RAIZ / rel).is_dir():
                    return f"]({REPO}/tree/{BRANCH}/{rel})"
                if rel in por_fonte or FECHAMENTO.match(rel):
                    if rel not in por_fonte:
                        por_fonte[rel] = id_automatico(rel)
                        fila.append((por_fonte[rel], rel))
                    return f"](#/{por_fonte[rel]}" + (f"#{ancora}" if ancora else "") + ")"
                return f"]({REPO}/blob/{BRANCH}/{rel})"

            linhas.append(LINK.sub(troca, linha))
        cabecalho = f"<!-- Gerado por scripts/gera-docs.py a partir de {src}. Não edite: edite a fonte e gere de novo. -->\n"
        saida[pid] = cabecalho + "\n".join(linhas) + "\n"
    return saida, avisos


def paginas_do_config():
    cfg = CONFIG.read_text(encoding="utf-8")
    return set(p for p in re.findall(r'page:\s*"([^"]*)"', cfg) if p), re.search(r'version:\s*"([^"]+)"', cfg).group(1)


def main():
    checar = "--check" in sys.argv[1:]
    saida, avisos = gerar()
    for a in avisos:
        print(f"aviso: {a}")
    problemas = []
    if checar:
        for pid, conteudo in saida.items():
            arq = CONTENT / f"{pid}.md"
            if not arq.exists():
                problemas.append(f"falta docs/content/{pid}.md")
            elif arq.read_text(encoding="utf-8") != conteudo:
                problemas.append(f"docs/content/{pid}.md difere da fonte")
        for arq in CONTENT.glob("*.md"):
            if arq.stem not in saida:
                problemas.append(f"docs/content/{arq.name} não vem de nenhuma fonte (sobra)")
        paginas, versao = paginas_do_config()
        for p in sorted(paginas - set(saida)):
            problemas.append(f"docs/config.js cita a página '{p}', que não existe")
        v = (RAIZ / "VERSION").read_text(encoding="utf-8").strip()
        if v != versao:
            problemas.append(f"VERSION ({v}) difere de docs/config.js version ({versao})")
        for p in problemas:
            print(f"problema: {p}")
        print("site em dia" if not problemas else f"{len(problemas)} problema(s); rode: python3 scripts/gera-docs.py")
        sys.exit(1 if problemas else 0)
    CONTENT.mkdir(parents=True, exist_ok=True)
    for pid, conteudo in saida.items():
        (CONTENT / f"{pid}.md").write_text(conteudo, encoding="utf-8")
    print(f"{len(saida)} páginas geradas em docs/content ({len(avisos)} aviso(s))")
    print(json.dumps(sorted(saida), ensure_ascii=False))


if __name__ == "__main__":
    main()
