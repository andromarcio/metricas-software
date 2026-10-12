# metricas-software

Métodos de medição de tamanho funcional de software, em português, em Markdown.

| Pasta | Conteúdo | Origem |
|---|---|---|
| [`APF/`](APF/README.md) | Manual de Práticas de Contagem de Pontos de Função (IFPUG CPM 4.3.1) | Conversão do PDF [`CPM-v4.3.1-Portuguese.pdf`](CPM-v4.3.1-Portuguese.pdf) |
| [`COSMIC/`](COSMIC/README.md) | Método COSMIC 3.0.1 — Manual de Medição | Conversão do PDF [`COSMIC_Method_v3.0.1_Measurement_Manual_Portuguese.pdf`](COSMIC_Method_v3.0.1_Measurement_Manual_Portuguese.pdf) |
| [`STI/`](STI/README.md) | Guia de Métricas da STI v1.3 (aplicação da APF em contratos) | Conversão do PDF [`GUIA_DE_METRICAS_STI_V1.3.pdf`](GUIA_DE_METRICAS_STI_V1.3.pdf) |
| [`PFC/`](PFC/README.md) | **PFC — Pontos de Função Caixa 1.0**: métrica proposta neste repositório, objetiva, independente de tecnologia e aplicável por IA; método e unidade levam o mesmo nome. Inclui especificação, esquema JSON, ferramenta de referência (contagem, mudança, concordância, impacto de diff e auditoria de evidências), medição da produção com IA, os desfechos de cada processo dentro do tamanho, estimativa por perfis calibráveis, prompts, exemplo completo em código e um exemplo real medido a partir da documentação do Aval (siesa-doc). | Proposta original |

## Site de documentação

A pasta [`docs/`](docs/README.md) publica este conteúdo como site no GitHub Pages, no padrão do `docqui-caixa-engine`. As páginas são geradas da fonte: `python3 scripts/gera-docs.py` (e `--check` para conferir que o site espelha os `.md`).
