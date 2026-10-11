# Site de documentação (GitHub Pages)

Site estático (HTML/CSS/JS, sem build) no padrão do `docqui-caixa-engine`: barra lateral
com navegação, busca, tema claro/escuro, conteúdo em **Markdown** renderizado no
navegador. As páginas são **geradas da fonte** (a especificação em `MFO/`, o prompt, os
exemplos e os índices dos manuais de referência) por `scripts/gera-docs.py`; não se
editam à mão.

## Estrutura

```text
docs/
├── index.html            # casca da página (sidebar + topbar + conteúdo)
├── config.js             # ÚNICO arquivo de configuração: nome, repo, versão e navegação
├── .nojekyll             # desliga o Jekyll no GitHub Pages
├── content/              # as páginas, em Markdown (GERADAS: python3 scripts/gera-docs.py)
└── assets/
    ├── css/styles.css    # tema base (tokens claro/escuro), do template docqui
    ├── css/mfo.css       # paleta azul e layout de página desta documentação
    ├── js/app.js         # navegação, rotas (#/pagina), render de Markdown, tema
    ├── vendor/marked.min.js
    └── img/              # logo e favicon
```

## Gerar as páginas

```bash
python3 scripts/gera-docs.py           # escreve docs/content/*.md a partir da fonte
python3 scripts/gera-docs.py --check   # acusa página desatualizada, sobrando ou citada e inexistente
```

O gerador reescreve os links: capítulo ou documento da MFO vira rota `#/pagina`; arquivo
que não é página (JSON, Python, relatório gerado, manual de referência) vira link para o
GitHub. O workflow de publicação roda o `--check` e recusa publicar um site que não
espelha a fonte. Mudou um capítulo: gere de novo e commite `docs/content/` junto.

## Pré-visualizar localmente

O site carrega o Markdown via `fetch`, então **não** funciona abrindo o arquivo direto
(`file://`). Sirva a pasta por HTTP:

```bash
python3 -m http.server -d docs 8080
# abra http://localhost:8080
```

## Publicar no GitHub Pages

1. Em **Settings → Pages → Build and deployment → Source**, selecione **GitHub Actions**.
2. Faça merge na branch `main`. O workflow
   [`.github/workflows/pages.yml`](../.github/workflows/pages.yml) publica a pasta `docs/`.
3. A URL aparece ao final do job (algo como `https://<usuário>.github.io/metricas-software/`).

> Alternativa sem Actions: **Settings → Pages → Source: Deploy from a branch**, branch
> `main`, pasta `/docs`. Nesse modo o `--check` não roda; rode-o antes do merge.

Enquanto o repositório for privado, os links para arquivos do GitHub (exemplos em JSON,
ferramentas, manuais) só abrem para quem tem acesso; o site em si fica completo porque
toda página é servida de `content/`.

## Personalizar

| Quero mudar… | Edite |
|---|---|
| Nome, repositório, itens do menu | `config.js` |
| Versão no selo do topo | `config.js` → `version`, igual ao `VERSION` da raiz (o `--check` confere) |
| Texto das páginas | a fonte (`MFO/*.md`, `README.md`…) e gere de novo |
| Quais arquivos viram página, e com que nome | `PAGINAS` em `scripts/gera-docs.py` |
| Página inicial | `homeHtml()` em `assets/js/app.js` |
| Cores, fontes, espaçamentos | `assets/css/styles.css` (base) e `assets/css/mfo.css` (paleta e layout) |
| Logo / favicon | `assets/img/logo.svg`, `assets/img/favicon.svg` |

### Adicionar uma página

1. Registre a fonte em `PAGINAS` (`scripts/gera-docs.py`): `"minha-pagina": "caminho/da/fonte.md"`.
2. Aponte para ela em `config.js`: `{ title: "Minha página", page: "minha-pagina", icon: "file" }`.
3. Gere: `python3 scripts/gera-docs.py`.

Links internos entre páginas usam o formato de rota `#/minha-pagina`; um documento da
MFO alcançado por link vira página automaticamente, com o nome derivado do caminho.

### Renomear uma página

Troque o identificador em `PAGINAS` e em `config.js` e registre o nome antigo em
`redirects` do `config.js`: `redirects: { "nome-antigo": "nome-novo" }`.

## Recursos

- Rotas por hash (`#/pagina`), sem `404.html`; página renomeada redireciona pelo `redirects`.
- `config.js`, `app.js` e os CSS carregados sem cache, e o conteúdo revalidado a cada visita.
- Markdown (GFM) via [marked](https://marked.js.org/) servido localmente; realce de sintaxe
  via [highlight.js](https://highlightjs.org/) por CDN, com degradação suave.
- Tema claro/escuro/sistema persistido em `localStorage`.
- Botão de copiar nos blocos de código, busca que filtra o menu (atalho <kbd>/</kbd>) e
  navegação anterior/próximo na ordem dos capítulos.
- Responsivo: a barra lateral vira gaveta no mobile; no desktop é redimensionável.
