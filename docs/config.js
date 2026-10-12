/* =========================================================================
   Configuração do site — PFC (Pontos de Função Caixa)
   -------------------------------------------------------------------------
   Único arquivo a editar para adaptar o site: nome, repositório e árvore de
   navegação. Cada item aponta para um arquivo Markdown em /content (sem a
   extensão .md), ou usa href para uma página HTML relativa à raiz do site.
   As páginas de /content são GERADAS da fonte por scripts/gera-docs.py.
   ========================================================================= */
window.DOKU_CONFIG = {
  /* Identidade do site */
  name: "PFC · Pontos de Função Caixa",
  fullName: "PFC — Pontos de Função Caixa",
  repo: "https://github.com/andromarcio/metricas-software",
  branch: "main",
  defaultPage: "introducao",

  /* Versão do PFC, no selo ao lado do nome (toda página) e na página inicial.
     Espelha o VERSION da raiz, que o site, servido só de docs/, não alcança.
     Troque os dois no mesmo commit: `python3 scripts/gera-docs.py --check` acusa a divergência. */
  version: "1.0",

  /* Páginas renomeadas: o endereço antigo (link, favorito) leva ao novo. */
  redirects: {
    "mfo-exemplos-aval-concordancia-adm-usr": "pfc-exemplos-aval-concordancia-adm-usr",
    "mfo-exemplos-aval-impacto-aval-1.23.1-para-5.0.0": "pfc-exemplos-aval-impacto-aval-1.23.1-para-5.0.0",
    "mfo-exemplos-aval-mudanca-aval-1.23.1-para-5.0.0": "pfc-exemplos-aval-mudanca-aval-1.23.1-para-5.0.0",
    "mfo-exemplos-aval-perfis-calibrados": "pfc-exemplos-aval-perfis-calibrados",
    "mfo-exemplos-aval-pfo-vs-pf-aval-5.0.0": "pfc-exemplos-aval-pfc-vs-pf-aval-5.0.0",
    "mfo-exemplos-aval-relatorio-aval-5.0.0": "pfc-exemplos-aval-relatorio-aval-5.0.0",
  },

  /* Ícones opcionais por item (chaves definidas em assets/js/app.js → ICONS) */
  nav: [
    {
      section: "Comece aqui",
      items: [
        { title: "Início", page: "", icon: "home" },
        { title: "Visão geral", page: "introducao", icon: "book" },
        { title: "O repositório", page: "repositorio", icon: "folder" },
      ],
    },
    {
      section: "A especificação PFC 1.0",
      items: [
        { title: "1. Motivação e princípios", page: "motivacao-e-principios", icon: "rocket" },
        { title: "2. Modelo funcional canônico", page: "modelo-funcional-canonico", icon: "layers" },
        { title: "3. Regras de contagem", page: "regras-de-contagem", icon: "doc" },
        { title: "4. Medição assistida por IA", page: "medicao-assistida-por-ia", icon: "terminal" },
        { title: "5. Comparação entre softwares", page: "comparacao-entre-softwares", icon: "split" },
        { title: "6. Exemplo completo: biblioteca", page: "exemplo-completo", icon: "file" },
        { title: "7. Glossário", page: "glossario", icon: "book" },
        { title: "8. Código e diff", page: "medicao-a-partir-do-codigo-e-do-diff", icon: "git" },
        { title: "9. Produção com IA", page: "producao-com-ia", icon: "flow" },
        { title: "10. Exemplo real: Aval", page: "exemplo-real-aval", icon: "search" },
        { title: "11. Estimativa", page: "estimativa", icon: "ticket" },
        { title: "12. Desfechos: a decisão no tamanho", page: "decisoes", icon: "link" },
      ],
    },
    {
      section: "Apoio",
      items: [
        { title: "Prompt de extração", page: "prompt-extracao", icon: "terminal" },
        { title: "Exemplo: autorizador de cartão", page: "exemplo-cartao", icon: "ticket" },
        { title: "Exemplo: código da biblioteca", page: "exemplo-codigo", icon: "git" },
      ],
    },
    {
      section: "Outros métodos",
      items: [
        { title: "APF — IFPUG CPM 4.3.1", page: "apf", icon: "layers" },
        { title: "COSMIC 3.0.1", page: "cosmic", icon: "layers" },
        { title: "Guia de Métricas da STI 1.3", page: "sti", icon: "layers" },
      ],
    },
  ],
};
