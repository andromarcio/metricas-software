<!-- Gerado por scripts/gera-docs.py a partir de PFC/exemplos/aval/impacto-aval-1.23.1-para-5.0.0.md. Não edite: edite a fonte e gere de novo. -->
# Impacto do diff — /home/user/siesa-doc: 10b547b → 49265a9 (modelo: Aval (siesa-doc) 1.23.1)

Arquivos alterados: 375 (M 225, A 142, D 8) · fonte de evidências: DOC

| Arquivo | Status | Linhas +/− | Processos e entidades que o citam |
|---|---|---|---|
| .claude/settings.json | M | +19/−2 | — |
| .claude/skills/analise-impacto/SKILL.md | A | +236/−0 | — |
| .claude/skills/analise-impacto/evals/evals.json | A | +26/−0 | — |
| .claude/skills/analise-impacto/evals/fixtures/ANALISE_SP06_novas_vs_alteradas.md | A | +52/−0 | — |
| .claude/skills/analise-impacto/references/dimensionamento-apf.md | A | +111/−0 | — |
| .claude/skills/analise-impacto/references/relatorio-html.md | A | +62/−0 | — |
| .claude/skills/analise-impacto/scripts/build-standalone.mjs | A | +91/−0 | — |
| .claude/skills/analise-impacto/scripts/checa-render.mjs | A | +178/−0 | — |
| .claude/skills/analista-requisitos/SKILL.md | M | +75/−100 | — |
| .claude/skills/analista-requisitos/references/dicionarios.md | M | +11/−13 | — |
| .claude/skills/analista-requisitos/references/estrutura-n3.md | M | +282/−139 | — |
| .claude/skills/analista-requisitos/references/speckit-export.md | M | +6/−14 | — |
| .claude/skills/apf-cpm/SKILL.md | M | +36/−5 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/00-Introducao/00-capa-e-creditos.md | A | +117/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/00-Introducao/01-conteudo.md | A | +52/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/00-Introducao/02-prefacio.md | A | +89/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/00-Introducao/03-introducao-ao-cpm.md | A | +166/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/00-indice.md | A | +26/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-1-FSM/00-conteudo.md | A | +42/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-1-FSM/01-prefacio.md | A | +15/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-1-FSM/02-introducao.md | A | +31/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-1-FSM/03-cap1-5-fsm.md | A | +909/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-1-FSM/04-anexo-a.md | A | +47/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/01-cap1-introducao.md | A | +87/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/02-cap2-visao-geral.md | A | +135/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/03-cap3-reunir-informacoes.md | A | +228/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/04-cap4-determinar-tipo-de-contagem.md | A | +64/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/05-cap5-escopo-e-fronteiras.md | A | +127/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/06-cap6-medir-funcoes-de-dados.md | A | +283/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/07-cap7-medir-funcoes-de-transacao.md | A | +562/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/08-indice.md | A | +189/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/00-introducao.md | A | +24/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/01-cap1-dados-de-codigo.md | A | +296/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/02-cap2-arquivos-logicos.md | A | +1020/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/03-cap3-dados-compartilhados.md | A | +440/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/04-cap4-projetos-de-melhoria.md | A | +532/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/05-cap5-conversao-de-dados.md | A | +57/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/06-indice.md | A | +258/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-4-Exemplos/00-introducao.md | A | +28/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-4-Exemplos/01-cap1-funcoes-de-dados.md | A | +1406/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-4-Exemplos/02-cap2-funcoes-de-transacao.md | A | +3256/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-4-Exemplos/03-indice.md | A | +162/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-5-Apendices-e-Glossario/01-apendice-a-tabela-de-calculo.md | A | +38/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-5-Apendices-e-Glossario/02-apendice-b-mudanca-versao-anterior.md | A | +337/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-5-Apendices-e-Glossario/03-apendice-c-tamanho-funcional-ajustado.md | A | +1117/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-5-Apendices-e-Glossario/04-glossario.md | A | +503/−0 | — |
| .claude/skills/apf-cpm/references/cpm-4.3.1/README.md | A | +96/−0 | — |
| .claude/skills/apf-cpm/references/exemplos.md | M | +13/−28 | — |
| .claude/skills/apf-cpm/references/funcoes-dados.md | M | +10/−10 | — |
| .claude/skills/apf-cpm/references/funcoes-transacao.md | M | +6/−8 | — |
| .claude/skills/apf-cpm/references/glossario.md | M | +2/−0 | — |
| .claude/skills/prototype/SKILL.md | M | +12/−23 | — |
| .claude/skills/retro/SKILL.md | A | +58/−0 | — |
| .github/workflows/pages.yml | A | +48/−0 | — |
| .gitignore | M | +3/−0 | — |
| APROVACOES.md | M | +9/−46 | — |
| CLAUDE.md | M | +104/−12 | — |
| PENDENCIAS.md | A | +240/−0 | — |
| RECONCILIACAO-IMPL-DOC-2026-07-24.md | A | +122/−0 | — |
| VERSION | M | +1/−1 | — |
| _ENTREGA-DS.md | M | +4/−10 | — |
| arquitetura/agentes-llm.html | A | +283/−0 | — |
| arquitetura/conexao-github.html | A | +350/−0 | — |
| arquitetura/prompts-engine-produto.html | A | +264/−0 | — |
| assets/css/app.css | D | +0/−723 | — |
| assets/css/aval-theme.css | D | +0/−155 | — |
| assets/css/mapa.css | A | +139/−0 | — |
| assets/js/app.js | D | +0/−758 | — |
| assets/mapa-data.js | A | +2/−0 | — |
| assets/tree.js | M | +265/−179 | — |
| demandas/INDEX.md | A | +44/−0 | — |
| demandas/_template-demanda.md | M | +104/−0 | — |
| demandas/aval0000003.html | A | +281/−0 | — |
| demandas/aval0000003.md | A | +68/−0 | — |
| demandas/aval0000004.html | A | +272/−0 | — |
| demandas/aval0000004.md | A | +68/−0 | — |
| demandas/aval0000005.html | A | +269/−0 | — |
| demandas/aval0000005.md | A | +61/−0 | — |
| demandas/aval0000006.html | A | +267/−0 | — |
| demandas/aval0000006.md | A | +63/−0 | — |
| demandas/aval0000007.html | A | +263/−0 | — |
| demandas/aval0000007.md | A | +63/−0 | — |
| demandas/aval0000008.html | A | +310/−0 | — |
| demandas/aval0000008.md | A | +85/−0 | — |
| demandas/aval0000009.html | A | +291/−0 | — |
| demandas/aval0000009.md | A | +78/−0 | — |
| engine/FEATURE-DEFINITION.md | M | +86/−16 | — |
| engine/VERSIONING.md | M | +29/−8 | — |
| engine/brand/BRAND.md | A | +81/−0 | — |
| engine/brand/badge-specado.svg | A | +8/−0 | — |
| engine/brand/badge-versao.svg | A | +8/−0 | — |
| engine/brand/lockup.svg | A | +23/−0 | — |
| engine/brand/logotipo-grifo.svg | A | +17/−0 | — |
| engine/brand/logotipo.svg | A | +14/−0 | — |
| engine/brand/proposta-v1.html | A | +626/−0 | — |
| engine/brand/simbolo-16.svg | A | +6/−0 | — |
| engine/brand/simbolo-negativo.svg | A | +8/−0 | — |
| engine/brand/simbolo.svg | A | +8/−0 | — |
| engine/brand/social-card.svg | A | +48/−0 | — |
| engine/prompts/PROMPT_0_EXTRACTION.md | M | +2/−2 | — |
| engine/prompts/PROMPT_1A_N1_negocio.md | M | +14/−13 | — |
| engine/prompts/PROMPT_1B_N1_tecnico.md | M | +1/−1 | — |
| engine/prompts/PROMPT_2A_N2_negocio.md | M | +31/−21 | — |
| engine/prompts/PROMPT_3A_N3_negocio.md | M | +261/−100 | — |
| engine/prompts/PROMPT_3A_N3_negocio_transcricao.md | M | +20/−10 | — |
| engine/prompts/PROMPT_3B_N3_tecnico.md | M | +183/−74 | — |
| engine/prompts/PROMPT_4A_N3_UPDATE_negocio.md | M | +52/−24 | — |
| engine/prompts/PROMPT_4B_N3_UPDATE_tecnico.md | M | +34/−14 | — |
| engine/prompts/PROMPT_AIM.md | A | +411/−0 | — |
| engine/prompts/PROMPT_AUDIT_RULES_DEDUP.md | M | +4/−1 | — |
| engine/prompts/PROMPT_AUDIT_TRACE_LINKS.md | M | +66/−57 | — |
| engine/prompts/PROMPT_BACKLOG.md | D | +0/−214 | — |
| engine/prompts/PROMPT_CONTAGEM.md | M | +134/−19 | — |
| engine/prompts/PROMPT_CONVERSION.md | M | +40/−14 | — |
| engine/prompts/PROMPT_CRUD.md | M | +92/−44 | — |
| engine/prompts/PROMPT_DATA_MODEL_FROM_SQL.md | M | +8/−4 | — |
| engine/prompts/PROMPT_DATA_MODEL_negocio.md | M | +121/−16 | — |
| engine/prompts/PROMPT_IMPACTO.md | D | +0/−106 | — |
| engine/prompts/PROMPT_MENU.md | M | +37/−14 | — |
| engine/prompts/PROMPT_N0_VISAO.md | M | +13/−11 | — |
| engine/prompts/PROMPT_N3_TO_N1.md | M | +15/−8 | — |
| engine/prompts/PROMPT_N3_TO_N2.md | M | +10/−5 | — |
| engine/prompts/PROMPT_PENDENCIAS.md | M | +22/−20 | — |
| engine/prompts/PROMPT_PROTOTYPE_FLOW_COMPONENT.md | M | +6/−1 | — |
| engine/prompts/PROMPT_PROTOTYPE_FLOW_FULL.md | M | +5/−2 | — |
| engine/prompts/PROMPT_PROTOTYPE_SCREEN_COMPONENT.md | M | +6/−1 | — |
| engine/prompts/PROMPT_PROTOTYPE_SCREEN_FULL.md | M | +6/−1 | — |
| engine/prompts/PROMPT_REVERSE_ENGINEERING.md | M | +455/−104 | — |
| engine/prompts/PROMPT_REVIEW.md | M | +7/−6 | — |
| engine/prompts/PROMPT_SDD.md | M | +132/−9 | — |
| engine/prompts/PROMPT_SPECKIT_EXPORT.md | M | +1/−1 | — |
| engine/prompts/PROMPT_TRANSCRICAO_REUNIAO.md | M | +46/−20 | — |
| engine/prompts/PROMPT_TRIAGEM.md | M | +10/−9 | — |
| engine/prompts/PROMPT_WIZARD.md | M | +59/−29 | — |
| engine/prompts/SYSTEM_PROMPT_analista_requisitos.md | M | +55/−34 | — |
| engine/templates/.claude/settings.json | A | +19/−0 | — |
| engine/templates/.github/CODEOWNERS | M | +1/−1 | — |
| engine/templates/.github/README.md | M | +3/−3 | — |
| engine/templates/.github/pull_request_template.md | M | +1/−1 | — |
| engine/templates/analise-impacto/_TEMPLATE_AIM.md | A | +198/−0 | — |
| engine/templates/analise-impacto/_TEMPLATE_AIM_SPRINT.md | A | +74/−0 | — |
| engine/templates/ci/spec-guard.yml | M | +13/−6 | — |
| engine/templates/ci/valida-artefatos-previstos.yml | A | +45/−0 | — |
| engine/templates/global/ALI-AIE-MAP.md | M | +1/−1 | — |
| engine/templates/global/API-PATTERNS.md | M | +1/−1 | — |
| engine/templates/global/AUTHZ.md | M | +1/−1 | — |
| engine/templates/global/CLAUDE.md | M | +9/−4 | — |
| engine/templates/global/CONTAGEM-PF.md | M | +49/−7 | — |
| engine/templates/global/DATA-MODEL.md | M | +2/−2 | — |
| engine/templates/global/DESIGN-SYSTEM.md | M | +1/−1 | — |
| engine/templates/global/ERROR-DICTIONARY.md | M | +1/−1 | — |
| engine/templates/global/FIELD-DICTIONARY.md | M | +1/−1 | — |
| engine/templates/global/MASTER.md | M | +89/−32 | — |
| engine/templates/global/MESSAGE-DICTIONARY.md | M | +1/−1 | — |
| engine/templates/global/N0_PRODUCT_VISION.md | M | +6/−3 | — |
| engine/templates/global/NFR.md | M | +2/−2 | — |
| engine/templates/global/PATTERNS.md | M | +1/−1 | — |
| engine/templates/global/RULES-DICTIONARY.md | M | +28/−23 | — |
| engine/templates/global/SIZING.md | M | +84/−18 | — |
| engine/templates/global/VOCABULARY-OVERRIDES.md | M | +1/−1 | — |
| engine/templates/global/data-models/_template-artefatos.md | M | +1/−1 | — |
| engine/templates/global/data-models/_template-dominio-negocio.md | M | +2/−2 | — |
| engine/templates/global/data-models/_template-dominio.md | M | +1/−1 | — |
| engine/templates/impactos/_TEMPLATE_IMPACTO.md | D | +0/−52 | — |
| engine/templates/modules/INDEX.md | M | +25/−13 | — |
| engine/templates/modules/_base-conhecimento/_template-base-conhecimento.md | M | +3/−3 | — |
| engine/templates/modules/_template-dominio/README.md | M | +6/−6 | — |
| engine/templates/modules/_template-dominio/_template-feature-set/README.md | M | +4/−4 | — |
| engine/templates/modules/_template-dominio/_template-feature-set/_template-feature.md | M | +264/−77 | — |
| engine/templates/prototypes/INDEX.md | M | +3/−2 | — |
| engine/templates/prototypes/_biblioteca-ds/README.md | M | +1/−1 | — |
| engine/templates/prototypes/_template/_template-dominio/README.md | A | +19/−0 | — |
| engine/templates/prototypes/_template/_template-dominio/_template-feature-set/README.md | M | +46/−0 | — |
| engine/templates/prototypes/_template/_template-dominio/_template-feature-set/_template-feature/README.md | M | +65/−0 | — |
| engine/templates/repos/_template-repo.md | M | +1/−1 | — |
| engine/templates/scripts/gates.py | D | +0/−553 | — |
| frontend-aval/README.md | M | +4/−18 | — |
| global/ALI-AIE-MAP.md | M | +3/−5 | — |
| global/API-PATTERNS.md | M | +10/−24 | — |
| global/CONTAGEM-PF.md | M | +138/−51 | — |
| global/DATA-MODEL.md | M | +36/−38 | — |
| global/DESIGN-SYSTEM.md | M | +6/−22 | — |
| global/DIAGRAMA-ER.md | A | +252/−0 | — |
| global/ERROR-DICTIONARY.md | M | +27/−4 | — |
| global/FIELD-DICTIONARY.md | M | +1/−2 | — |
| global/MASTER.md | M | +21/−33 | — |
| global/NFR.md | M | +94/−164 | — |
| global/PATTERNS.md | M | +1/−4 | — |
| global/PLANO-IMPLEMENTACAO.md | M | +67/−1 | — |
| global/RULES-DICTIONARY.md | M | +1/−2 | — |
| global/SIZING.md | M | +50/−43 | — |
| global/VOCABULARY-OVERRIDES.md | A | +28/−0 | — |
| global/data-models/administracao.md | M | +63/−39 | entidade Conta, entidade Convite, entidade EventoAuditoria, entidade Funcionalidade, entidade GitHub, entidade Perfil, entidade Usuario |
| global/data-models/agentes.md | M | +25/−12 | entidade ExecucaoAgente |
| global/data-models/demandas.md | M | +17/−14 | — |
| global/data-models/esteira.md | M | +28/−25 | entidade EsteiraExecucao, entidade EtapaExecucao, entidade PendenciaAprovacao, entidade RegistroImpacto |
| global/data-models/sistemas.md | M | +39/−23 | entidade Demanda, entidade FerramentaDemandas, entidade Sistema |
| identidade-visual/README.md | M | +4/−9 | — |
| index.html | M | +3515/−106 | — |
| modules/INDEX.md | M | +88/−74 | — |
| modules/_backlog/.gitkeep | D | +0/−0 | — |
| modules/administracao/README.md | M | +43/−15 | — |
| modules/administracao/auditoria/README.md | M | +6/−5 | — |
| modules/administracao/auditoria/f-pesquisar-auditoria.md | M | +45/−29 | ADM-AUD-01 |
| modules/administracao/conta/README.md | M | +20/−16 | — |
| modules/administracao/conta/f-autenticar-usuario.md | M | +118/−37 | ADM-CTA-02 |
| modules/administracao/conta/f-criar-conta.md | M | +70/−34 | ADM-CTA-01 |
| modules/administracao/conta/f-recuperar-senha.md | M | +91/−39 | ADM-CTA-03, ADM-CTA-03.2 |
| modules/administracao/conta/f-trocar-conta.md | A | +306/−0 | — |
| modules/administracao/integracoes/README.md | M | +6/−5 | — |
| modules/administracao/integracoes/f-configurar-conexao-github.md | M | +81/−33 | ADM-INT-01, ADM-INT-01.2 |
| modules/administracao/modelos-ia/README.md | A | +78/−0 | — |
| modules/administracao/modelos-ia/f-configurar-modelo-por-etapa.md | A | +309/−0 | — |
| modules/administracao/organizacao/README.md | M | +8/−7 | — |
| modules/administracao/organizacao/f-alterar-organizacao.md | M | +119/−28 | ADM-ORG-03 |
| modules/administracao/organizacao/f-criar-organizacao.md | M | +137/−28 | ADM-ORG-01 |
| modules/administracao/organizacao/f-visualizar-organizacao.md | M | +117/−25 | ADM-ORG-02 |
| modules/administracao/perfis/README.md | M | +24/−19 | — |
| modules/administracao/perfis/f-ativar-funcionalidade.md | M | +48/−25 | ADM-PER-05 |
| modules/administracao/perfis/f-conceder-funcionalidade.md | M | +50/−25 | ADM-PER-02 |
| modules/administracao/perfis/f-criar-perfil.md | M | +49/−26 | ADM-PER-01 |
| modules/administracao/perfis/f-desativar-funcionalidade.md | M | +48/−25 | ADM-PER-04 |
| modules/administracao/perfis/f-revogar-funcionalidade.md | M | +50/−25 | ADM-PER-03 |
| modules/administracao/perfis/f-visualizar-matriz-de-perfis.md | A | +287/−0 | — |
| modules/administracao/usuarios/README.md | M | +13/−12 | — |
| modules/administracao/usuarios/f-aceitar-convite.md | M | +182/−30 | ADM-USR-06 |
| modules/administracao/usuarios/f-alterar-perfil-do-usuario.md | M | +131/−27 | ADM-USR-03 |
| modules/administracao/usuarios/f-convidar-usuario.md | M | +168/−30 | ADM-USR-02 |
| modules/administracao/usuarios/f-desativar-usuario.md | M | +115/−27 | ADM-USR-04 |
| modules/administracao/usuarios/f-pesquisar-usuarios.md | M | +122/−25 | ADM-USR-01 |
| modules/administracao/usuarios/f-reativar-usuario.md | M | +112/−27 | ADM-USR-05 |
| modules/agentes/README.md | M | +13/−9 | — |
| modules/agentes/execucao/README.md | M | +19/−15 | — |
| modules/agentes/execucao/f-detalhar-requisitos.md | M | +81/−20 | AGT-EXE-02 |
| modules/agentes/execucao/f-executar-testes-do-sistema.md | M | +26/−11 | AGT-EXE-07 |
| modules/agentes/execucao/f-gerar-analise-impacto.md | M | +37/−21 | AGT-EXE-10 |
| modules/agentes/execucao/f-gerar-casos-de-teste.md | M | +46/−19 | AGT-EXE-04 |
| modules/agentes/execucao/f-gerar-codigo.md | M | +53/−27 | AGT-EXE-06 |
| modules/agentes/execucao/f-gerar-modelo-de-dados.md | M | +40/−19 | AGT-EXE-03 |
| modules/agentes/execucao/f-gerar-plano-de-implementacao.md | M | +32/−22 | AGT-EXE-05 |
| modules/agentes/execucao/f-gerar-preparacao-do-sistema.md | M | +107/−22 | AGT-EXE-09 |
| modules/agentes/execucao/f-gerar-prototipo.md | A | +268/−0 | — |
| modules/agentes/execucao/f-preparar-implantacao.md | M | +16/−13 | AGT-EXE-08 |
| modules/agentes/execucao/f-processar-triagem.md | M | +17/−13 | AGT-EXE-01 |
| modules/demandas/README.md | M | +12/−10 | — |
| modules/demandas/intake/README.md | M | +16/−12 | — |
| modules/demandas/intake/f-iniciar-esteira.md | M | +56/−25 | DEM-INT-02 |
| modules/demandas/intake/f-iniciar-execucao-do-acervo.md | A | +286/−0 | — |
| modules/demandas/intake/f-registrar-demanda.md | M | +16/−13 | DEM-INT-01 |
| modules/demandas/painel/README.md | M | +15/−12 | — |
| modules/demandas/painel/f-cancelar-demanda.md | A | +282/−0 | — |
| modules/demandas/painel/f-pesquisar-demandas.md | M | +42/−16 | DEM-PAI-01, DEM-PAI-01.2 |
| modules/esteira/README.md | M | +13/−10 | — |
| modules/esteira/acompanhamento/README.md | M | +14/−10 | — |
| modules/esteira/acompanhamento/f-acompanhar-esteira.md | M | +92/−33 | EST-ACO-01 |
| modules/esteira/acompanhamento/f-consultar-consumo-de-ia.md | A | +274/−0 | — |
| modules/esteira/acompanhamento/f-consultar-saude-das-esteiras.md | A | +272/−0 | — |
| modules/esteira/acompanhamento/f-visualizar-analise-impacto.md | M | +94/−29 | EST-ACO-08 |
| modules/esteira/acompanhamento/f-visualizar-casos-de-teste.md | M | +63/−25 | EST-ACO-04 |
| modules/esteira/acompanhamento/f-visualizar-codificacao.md | M | +117/−31 | EST-ACO-05 |
| modules/esteira/acompanhamento/f-visualizar-implantacao.md | M | +17/−14 | EST-ACO-07 |
| modules/esteira/acompanhamento/f-visualizar-modelo-de-dados.md | M | +96/−29 | EST-ACO-03 |
| modules/esteira/acompanhamento/f-visualizar-prototipo.md | A | +271/−0 | — |
| modules/esteira/acompanhamento/f-visualizar-requisitos.md | M | +81/−28 | EST-ACO-02 |
| modules/esteira/acompanhamento/f-visualizar-testes-do-sistema.md | M | +40/−18 | EST-ACO-06 |
| modules/esteira/aprovacoes/README.md | M | +23/−20 | — |
| modules/esteira/aprovacoes/f-aprovar-escopo.md | M | +61/−20 | EST-APR-09 |
| modules/esteira/aprovacoes/f-aprovar-etapa.md | M | +15/−12 | EST-APR-01 |
| modules/esteira/aprovacoes/f-aprovar-feature.md | M | +15/−12 | EST-APR-03 |
| modules/esteira/aprovacoes/f-aprovar-historia.md | M | +17/−13 | EST-APR-04 |
| modules/esteira/aprovacoes/f-autorizar-implantacao.md | M | +16/−13 | EST-APR-07 |
| modules/esteira/aprovacoes/f-homologar-entrega.md | M | +16/−13 | EST-APR-06 |
| modules/esteira/aprovacoes/f-listar-pendencias.md | M | +15/−12 | EST-APR-08 |
| modules/esteira/aprovacoes/f-reprovar-testes-do-sistema.md | M | +16/−13 | EST-APR-05 |
| modules/esteira/aprovacoes/f-responder-esclarecimentos.md | A | +287/−0 | — |
| modules/esteira/aprovacoes/f-solicitar-ajustes.md | M | +15/−12 | EST-APR-02 |
| modules/operacao/README.md | A | +76/−0 | — |
| modules/operacao/gestao-contas/README.md | A | +85/−0 | — |
| modules/operacao/gestao-contas/f-criar-organizacao-operador.md | A | +263/−0 | — |
| modules/operacao/gestao-contas/f-definir-limites-de-consumo.md | A | +261/−0 | — |
| modules/operacao/gestao-contas/f-editar-organizacao-operador.md | A | +258/−0 | — |
| modules/operacao/gestao-contas/f-entrar-como.md | A | +250/−0 | — |
| modules/operacao/gestao-contas/f-listar-contas.md | A | +291/−0 | — |
| modules/operacao/gestao-contas/f-reativar-conta.md | A | +254/−0 | — |
| modules/operacao/gestao-contas/f-suspender-conta.md | A | +280/−0 | — |
| modules/sistemas/README.md | M | +15/−10 | — |
| modules/sistemas/acervo/README.md | A | +78/−0 | — |
| modules/sistemas/acervo/f-visualizar-catalogo-de-features.md | A | +298/−0 | — |
| modules/sistemas/acervo/f-visualizar-mapa-de-features.md | A | +312/−0 | — |
| modules/sistemas/cadastro/README.md | M | +8/−8 | — |
| modules/sistemas/cadastro/f-alterar-sistema.md | M | +20/−15 | SIS-CAD-04 |
| modules/sistemas/cadastro/f-cadastrar-sistema.md | M | +20/−14 | SIS-CAD-01 |
| modules/sistemas/cadastro/f-definir-sistema-ativo.md | M | +15/−12 | SIS-CAD-02 |
| modules/sistemas/cadastro/f-preparar-sistema.md | M | +164/−28 | SIS-CAD-05 |
| modules/sistemas/cadastro/f-transferir-sistema.md | M | +108/−20 | SIS-CAD-03 |
| modules/sistemas/configuracoes/README.md | M | +6/−6 | — |
| modules/sistemas/configuracoes/f-configurar-aprovadores.md | M | +20/−15 | SIS-CFG-02 |
| modules/sistemas/configuracoes/f-configurar-estrategia.md | M | +101/−22 | SIS-CFG-03 |
| modules/sistemas/configuracoes/f-configurar-ferramenta-de-demandas.md | M | +120/−21 | SIS-CFG-04 |
| modules/sistemas/configuracoes/f-configurar-repositorios.md | M | +16/−13 | SIS-CFG-01 |
| pending_changes.md | M | +52/−274 | — |
| prototypes/_biblioteca-ds/README.md | M | +2/−9 | — |
| prototypes/_gerados/README.md | A | +9/−0 | — |
| prototypes/aval/README.md | M | +24/−52 | — |
| prototypes/aval/adm-modelos-ia.html | A | +273/−0 | — |
| prototypes/aval/app-mobile.html | M | +1/−1 | — |
| prototypes/aval/catalogo-features.html | A | +320/−0 | — |
| prototypes/aval/configuracoes.html | M | +2/−0 | — |
| prototypes/aval/console-siesa-conta.html | A | +212/−0 | — |
| prototypes/aval/console-siesa.html | A | +281/−0 | — |
| prototypes/aval/esteira-reajuste.html | M | +1/−0 | — |
| prototypes/aval/esteira.html | M | +64/−1 | — |
| prototypes/aval/etapa-casos-teste.html | M | +1/−0 | — |
| prototypes/aval/etapa-codificacao-reajuste.html | M | +1/−0 | — |
| prototypes/aval/etapa-codificacao.html | M | +1/−0 | — |
| prototypes/aval/etapa-impacto.html | M | +1/−0 | — |
| prototypes/aval/etapa-implantacao.html | M | +1/−0 | — |
| prototypes/aval/etapa-modelo-dados.html | M | +9/−8 | — |
| prototypes/aval/etapa-prototipo.html | A | +255/−0 | — |
| prototypes/aval/etapa-requisitos-esclarecimentos.html | A | +649/−0 | — |
| prototypes/aval/etapa-requisitos.html | M | +1/−0 | — |
| prototypes/aval/etapa-testes-sistema-reexecucao.html | M | +1/−0 | — |
| prototypes/aval/etapa-testes-sistema-reprovado.html | M | +1/−0 | — |
| prototypes/aval/etapa-testes-sistema.html | M | +1/−0 | — |
| prototypes/aval/mapa-features.html | A | +374/−0 | — |
| prototypes/aval/nova-demanda.html | M | +26/−2 | — |
| prototypes/aval/painel.html | M | +74/−8 | — |
| prototypes/aval/preparar-sistema-chat.html | M | +6/−0 | — |
| prototypes/aval/preparar-sistema-hibrido.html | M | +6/−0 | — |
| prototypes/aval/preparar-sistema.html | M | +6/−0 | — |
| prototypes/aval/telas.js | M | +7/−0 | — |
| prototypes/editor-analista/README.md | A | +22/−0 | — |
| prototypes/editor-analista/index.html | A | +1147/−0 | — |
| rastreabilidade/data.js | A | +2422/−0 | — |
| rastreabilidade/graph.js | A | +676/−0 | — |
| rastreabilidade/index.html | A | +119/−0 | — |
| rastreabilidade/styles.css | A | +220/−0 | — |
| repos/INDEX.md | M | +1/−3 | — |
| scripts/atualiza-pages.mjs | A | +137/−0 | — |
| scripts/audit-trace-links.mjs | M | +32/−18 | — |
| scripts/build-trace-data.mjs | M | +66/−18 | — |
| scripts/delta-n3.mjs | A | +188/−0 | — |
| scripts/gates.py | M | +72/−11 | — |
| scripts/generate-impact-draft.mjs | M | +211/−159 | — |
| scripts/generate-trace-index.mjs | M | +27/−28 | — |
| scripts/generate-usage-index.mjs | M | +13/−5 | — |
| scripts/gera-aprovacoes.mjs | M | +1/−1 | — |
| scripts/gera-diagrama-er.mjs | A | +131/−0 | — |
| scripts/gera-html-impacto.mjs | A | +445/−0 | — |
| scripts/gera-mapa-features.mjs | A | +515/−0 | — |
| scripts/gera-pendencias.mjs | A | +145/−0 | — |
| scripts/gera-planilha-contagem.py | A | +898/−0 | — |
| scripts/hooks/spec-guard.mjs | M | +129/−15 | — |
| scripts/lib/front-matter.mjs | A | +80/−0 | — |
| scripts/lib/mapa-codigo.mjs | A | +160/−0 | — |
| scripts/lib/pe.mjs | A | +95/−0 | — |
| scripts/lib/trace-index.mjs | M | +108/−43 | — |
| scripts/migra-aim.mjs | A | +829/−0 | — |
| scripts/migra-enumeracao.py | A | +449/−0 | — |
| scripts/pendencias-ids.json | A | +1505/−0 | — |
| scripts/preflight-spec.mjs | M | +8/−7 | — |
| scripts/regen.sh | A | +83/−0 | — |
| scripts/resolve-refs.mjs | A | +243/−0 | — |
| scripts/stamp.sh | M | +10/−7 | — |
| scripts/suspect-links.mjs | M | +9/−14 | — |
| scripts/valida-acessorio-tela.mjs | A | +291/−0 | — |
| scripts/valida-artefatos-previstos.mjs | A | +187/−0 | — |
| scripts/valida-citacoes-dicionario.mjs | A | +168/−0 | — |
| scripts/valida-contagem-consolidada.mjs | A | +305/−0 | — |
| scripts/valida-enumeracao-contagem.mjs | A | +160/−0 | — |
| scripts/valida-fluxo-principal.mjs | A | +153/−0 | — |
| scripts/validate-doc.mjs | M | +39/−27 | — |
| scripts/validate-feature-semantics.mjs | M | +496/−7 | — |
| scripts/validate-impact.mjs | M | +366/−107 | — |
| scripts/verifica-texto-corrido.mjs | M | +13/−2 | — |

## Processos

| Processo | Situação | Trechos citados com mudança | Movimentos candidatos a 'alterado' |
|---|---|---|---|
| ADM-AUD-01 Pesquisar auditoria | afetado (trecho) | modules/administracao/auditoria/f-pesquisar-auditoria.md#Memória de cálculo (alterado) | R EventoAuditoria (alterado); R Usuario (alterado); X Usuario (alterado) |
| ADM-CTA-02 Autenticar usuário | afetado (trecho) | modules/administracao/conta/f-autenticar-usuario.md#Memória de cálculo (alterado) | R Conta (alterado); R EventoAuditoria (alterado); R Perfil (alterado); W Usuario (alterado) |
| ADM-CTA-01 Criar conta | afetado (trecho) | modules/administracao/conta/f-criar-conta.md#Memória de cálculo (alterado) | R EventoAuditoria (alterado); W Conta (alterado); W Usuario (alterado) |
| ADM-CTA-03 Recuperar senha | afetado (trecho) | modules/administracao/conta/f-recuperar-senha.md#Memória de cálculo (alterado) | R EventoAuditoria (alterado); W Usuario (alterado) |
| ADM-CTA-03.2 Redefinir a senha | afetado (arquivo) | — | — |
| ADM-INT-01 Configurar conexão GitHub | afetado (trecho) | modules/administracao/integracoes/f-configurar-conexao-github.md#API (alterado); modules/administracao/integracoes/f-configurar-conexao-github.md#Memória de cálculo (alterado) | D CONEXAO_GITHUB_INACTIVE (alterado); D CONEXAO_GITHUB_INSTALL_FAILED (alterado); E GitHub (alterado); R EventoAuditoria (alterado); W Conta (alterado); X GitHub (alterado) |
| ADM-INT-01.2 Processar revogação (webhook do GitHub) | afetado (trecho) | modules/administracao/integracoes/f-configurar-conexao-github.md#API (alterado) | X GitHub (alterado) |
| ADM-ORG-03 Alterar organização | afetado (arquivo) | — | — |
| ADM-ORG-01 Criar organização | afetado (arquivo) | — | — |
| ADM-ORG-02 Visualizar organização | afetado (arquivo) | — | — |
| ADM-PER-05 Ativar funcionalidade | afetado (trecho) | modules/administracao/perfis/f-ativar-funcionalidade.md#Memória de cálculo (alterado) | R EventoAuditoria (alterado); W Funcionalidade (alterado) |
| ADM-PER-02 Conceder funcionalidade | afetado (trecho) | modules/administracao/perfis/f-conceder-funcionalidade.md#Memória de cálculo (alterado) | R EventoAuditoria (alterado); R Funcionalidade (alterado); R Perfil (alterado); W Funcionalidade (alterado); W Perfil (alterado) |
| ADM-PER-01 Criar perfil | afetado (trecho) | modules/administracao/perfis/f-criar-perfil.md#Memória de cálculo (alterado) | R EventoAuditoria (alterado); W Perfil (alterado) |
| ADM-PER-04 Desativar funcionalidade | afetado (trecho) | modules/administracao/perfis/f-desativar-funcionalidade.md#Memória de cálculo (alterado) | R EventoAuditoria (alterado); W Funcionalidade (alterado) |
| ADM-PER-03 Revogar funcionalidade | afetado (trecho) | modules/administracao/perfis/f-revogar-funcionalidade.md#Memória de cálculo (alterado) | R EventoAuditoria (alterado); R Funcionalidade (alterado); R Perfil (alterado); W Funcionalidade (alterado) |
| ADM-USR-06 Aceitar convite | afetado (arquivo) | — | — |
| ADM-USR-03 Alterar perfil do usuário | afetado (arquivo) | — | — |
| ADM-USR-02 Convidar usuário | afetado (arquivo) | — | — |
| ADM-USR-04 Desativar usuário | afetado (arquivo) | — | — |
| ADM-USR-01 Pesquisar usuários | afetado (trecho) | modules/administracao/usuarios/f-pesquisar-usuarios.md#API (alterado) | — |
| ADM-USR-05 Reativar usuário | afetado (arquivo) | — | — |
| AGT-EXE-02 Detalhar requisitos | afetado (arquivo) | — | — |
| AGT-EXE-07 Executar testes do sistema | afetado (arquivo) | — | — |
| AGT-EXE-10 Gerar análise de impacto | afetado (arquivo) | — | — |
| AGT-EXE-04 Gerar casos de teste | afetado (arquivo) | — | — |
| AGT-EXE-06 Gerar código | afetado (arquivo) | — | — |
| AGT-EXE-03 Gerar modelo de dados | afetado (arquivo) | — | — |
| AGT-EXE-05 Gerar plano de implementação | afetado (arquivo) | — | — |
| AGT-EXE-09 Gerar preparação do sistema | afetado (trecho) | modules/agentes/execucao/f-gerar-preparacao-do-sistema.md#API (alterado) | — |
| AGT-EXE-08 Preparar implantação | afetado (arquivo) | — | — |
| AGT-EXE-01 Processar triagem | afetado (arquivo) | — | — |
| DEM-INT-02 Iniciar esteira | afetado (arquivo) | — | — |
| DEM-INT-01 Registrar demanda | afetado (arquivo) | — | — |
| DEM-PAI-01 Pesquisar demandas | afetado (arquivo) | — | — |
| DEM-PAI-01.2 Consultar resumo do painel (contadores) | afetado (arquivo) | — | — |
| EST-ACO-01 Acompanhar esteira | afetado (arquivo) | — | — |
| EST-ACO-08 Visualizar análise de impacto | afetado (arquivo) | — | — |
| EST-ACO-04 Visualizar casos de teste | afetado (arquivo) | — | — |
| EST-ACO-05 Visualizar codificação | afetado (trecho) | modules/esteira/acompanhamento/f-visualizar-codificacao.md#API (alterado) | D RESOURCE_NOT_FOUND (alterado); X EtapaExecucao (alterado) |
| EST-ACO-07 Visualizar implantação | afetado (arquivo) | — | — |
| EST-ACO-03 Visualizar modelo de dados | afetado (arquivo) | — | — |
| EST-ACO-02 Visualizar requisitos | afetado (arquivo) | — | — |
| EST-ACO-06 Visualizar testes do sistema | afetado (arquivo) | — | — |
| EST-APR-09 Aprovar escopo de impacto | afetado (arquivo) | — | — |
| EST-APR-01 Aprovar etapa | afetado (arquivo) | — | — |
| EST-APR-03 Aprovar feature | afetado (arquivo) | — | — |
| EST-APR-04 Aprovar história | afetado (arquivo) | — | — |
| EST-APR-07 Autorizar implantação | afetado (arquivo) | — | — |
| EST-APR-06 Homologar entrega | afetado (arquivo) | — | — |
| EST-APR-08 Listar pendências | afetado (arquivo) | — | — |
| EST-APR-05 Reprovar testes do sistema | afetado (arquivo) | — | — |
| EST-APR-02 Solicitar ajustes | afetado (arquivo) | — | — |
| SIS-CAD-04 Alterar sistema | afetado (arquivo) | — | — |
| SIS-CAD-01 Cadastrar sistema | afetado (arquivo) | — | — |
| SIS-CAD-02 Definir sistema ativo | afetado (arquivo) | — | — |
| SIS-CAD-05 Preparar sistema | afetado (arquivo) | — | — |
| SIS-CAD-03 Transferir sistema | afetado (arquivo) | — | — |
| SIS-CFG-02 Configurar aprovadores | afetado (arquivo) | — | — |
| SIS-CFG-03 Configurar estratégia | afetado (arquivo) | — | — |
| SIS-CFG-04 Configurar ferramenta de demandas | afetado (arquivo) | — | — |
| SIS-CFG-01 Configurar repositórios | afetado (arquivo) | — | — |

## Resumo

- Re-extrair e marcar movimentos conforme RD-01: ADM-AUD-01, ADM-CTA-02, ADM-CTA-01, ADM-CTA-03, ADM-INT-01, ADM-INT-01.2, ADM-PER-05, ADM-PER-02, ADM-PER-01, ADM-PER-04, ADM-PER-03, ADM-USR-01, AGT-EXE-09, EST-ACO-05
- Afetados apenas por arquivo (confirmar na extração): ADM-CTA-03.2, ADM-ORG-01, ADM-ORG-02, ADM-ORG-03, ADM-USR-02, ADM-USR-03, ADM-USR-04, ADM-USR-05, ADM-USR-06, AGT-EXE-01, AGT-EXE-02, AGT-EXE-03, AGT-EXE-04, AGT-EXE-05, AGT-EXE-06, AGT-EXE-07, AGT-EXE-08, AGT-EXE-10, DEM-INT-01, DEM-INT-02, DEM-PAI-01, DEM-PAI-01.2, EST-ACO-01, EST-ACO-02, EST-ACO-03, EST-ACO-04, EST-ACO-06, EST-ACO-07, EST-ACO-08, EST-APR-01, EST-APR-02, EST-APR-03, EST-APR-04, EST-APR-05, EST-APR-06, EST-APR-07, EST-APR-08, EST-APR-09, SIS-CAD-01, SIS-CAD-02, SIS-CAD-03, SIS-CAD-04, SIS-CAD-05, SIS-CFG-01, SIS-CFG-02, SIS-CFG-03, SIS-CFG-04
- Arquivos alterados sem processo nem entidade associados (procurar pontos de entrada novos): .claude/settings.json, .claude/skills/analise-impacto/SKILL.md, .claude/skills/analise-impacto/evals/evals.json, .claude/skills/analise-impacto/evals/fixtures/ANALISE_SP06_novas_vs_alteradas.md, .claude/skills/analise-impacto/references/dimensionamento-apf.md, .claude/skills/analise-impacto/references/relatorio-html.md, .claude/skills/analise-impacto/scripts/build-standalone.mjs, .claude/skills/analise-impacto/scripts/checa-render.mjs, .claude/skills/analista-requisitos/SKILL.md, .claude/skills/analista-requisitos/references/dicionarios.md, .claude/skills/analista-requisitos/references/estrutura-n3.md, .claude/skills/analista-requisitos/references/speckit-export.md, .claude/skills/apf-cpm/SKILL.md, .claude/skills/apf-cpm/references/cpm-4.3.1/00-Introducao/00-capa-e-creditos.md, .claude/skills/apf-cpm/references/cpm-4.3.1/00-Introducao/01-conteudo.md, .claude/skills/apf-cpm/references/cpm-4.3.1/00-Introducao/02-prefacio.md, .claude/skills/apf-cpm/references/cpm-4.3.1/00-Introducao/03-introducao-ao-cpm.md, .claude/skills/apf-cpm/references/cpm-4.3.1/00-indice.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-1-FSM/00-conteudo.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-1-FSM/01-prefacio.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-1-FSM/02-introducao.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-1-FSM/03-cap1-5-fsm.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-1-FSM/04-anexo-a.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/01-cap1-introducao.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/02-cap2-visao-geral.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/03-cap3-reunir-informacoes.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/04-cap4-determinar-tipo-de-contagem.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/05-cap5-escopo-e-fronteiras.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/06-cap6-medir-funcoes-de-dados.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/07-cap7-medir-funcoes-de-transacao.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-2-A-Transicao/08-indice.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/00-introducao.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/01-cap1-dados-de-codigo.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/02-cap2-arquivos-logicos.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/03-cap3-dados-compartilhados.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/04-cap4-projetos-de-melhoria.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/05-cap5-conversao-de-dados.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-3-Praticas-de-Contagem/06-indice.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-4-Exemplos/00-introducao.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-4-Exemplos/01-cap1-funcoes-de-dados.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-4-Exemplos/02-cap2-funcoes-de-transacao.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-4-Exemplos/03-indice.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-5-Apendices-e-Glossario/01-apendice-a-tabela-de-calculo.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-5-Apendices-e-Glossario/02-apendice-b-mudanca-versao-anterior.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-5-Apendices-e-Glossario/03-apendice-c-tamanho-funcional-ajustado.md, .claude/skills/apf-cpm/references/cpm-4.3.1/Parte-5-Apendices-e-Glossario/04-glossario.md, .claude/skills/apf-cpm/references/cpm-4.3.1/README.md, .claude/skills/apf-cpm/references/exemplos.md, .claude/skills/apf-cpm/references/funcoes-dados.md, .claude/skills/apf-cpm/references/funcoes-transacao.md, .claude/skills/apf-cpm/references/glossario.md, .claude/skills/prototype/SKILL.md, .claude/skills/retro/SKILL.md, .github/workflows/pages.yml, .gitignore, APROVACOES.md, CLAUDE.md, PENDENCIAS.md, RECONCILIACAO-IMPL-DOC-2026-07-24.md, VERSION, _ENTREGA-DS.md, arquitetura/agentes-llm.html, arquitetura/conexao-github.html, arquitetura/prompts-engine-produto.html, assets/css/app.css, assets/css/aval-theme.css, assets/css/mapa.css, assets/js/app.js, assets/mapa-data.js, assets/tree.js, demandas/INDEX.md, demandas/_template-demanda.md, demandas/aval0000003.html, demandas/aval0000003.md, demandas/aval0000004.html, demandas/aval0000004.md, demandas/aval0000005.html, demandas/aval0000005.md, demandas/aval0000006.html, demandas/aval0000006.md, demandas/aval0000007.html, demandas/aval0000007.md, demandas/aval0000008.html, demandas/aval0000008.md, demandas/aval0000009.html, demandas/aval0000009.md, engine/FEATURE-DEFINITION.md, engine/VERSIONING.md, engine/brand/BRAND.md, engine/brand/badge-specado.svg, engine/brand/badge-versao.svg, engine/brand/lockup.svg, engine/brand/logotipo-grifo.svg, engine/brand/logotipo.svg, engine/brand/proposta-v1.html, engine/brand/simbolo-16.svg, engine/brand/simbolo-negativo.svg, engine/brand/simbolo.svg, engine/brand/social-card.svg, engine/prompts/PROMPT_0_EXTRACTION.md, engine/prompts/PROMPT_1A_N1_negocio.md, engine/prompts/PROMPT_1B_N1_tecnico.md, engine/prompts/PROMPT_2A_N2_negocio.md, engine/prompts/PROMPT_3A_N3_negocio.md, engine/prompts/PROMPT_3A_N3_negocio_transcricao.md, engine/prompts/PROMPT_3B_N3_tecnico.md, engine/prompts/PROMPT_4A_N3_UPDATE_negocio.md, engine/prompts/PROMPT_4B_N3_UPDATE_tecnico.md, engine/prompts/PROMPT_AIM.md, engine/prompts/PROMPT_AUDIT_RULES_DEDUP.md, engine/prompts/PROMPT_AUDIT_TRACE_LINKS.md, engine/prompts/PROMPT_BACKLOG.md, engine/prompts/PROMPT_CONTAGEM.md, engine/prompts/PROMPT_CONVERSION.md, engine/prompts/PROMPT_CRUD.md, engine/prompts/PROMPT_DATA_MODEL_FROM_SQL.md, engine/prompts/PROMPT_DATA_MODEL_negocio.md, engine/prompts/PROMPT_IMPACTO.md, engine/prompts/PROMPT_MENU.md, engine/prompts/PROMPT_N0_VISAO.md, engine/prompts/PROMPT_N3_TO_N1.md, engine/prompts/PROMPT_N3_TO_N2.md, engine/prompts/PROMPT_PENDENCIAS.md, engine/prompts/PROMPT_PROTOTYPE_FLOW_COMPONENT.md, engine/prompts/PROMPT_PROTOTYPE_FLOW_FULL.md, engine/prompts/PROMPT_PROTOTYPE_SCREEN_COMPONENT.md, engine/prompts/PROMPT_PROTOTYPE_SCREEN_FULL.md, engine/prompts/PROMPT_REVERSE_ENGINEERING.md, engine/prompts/PROMPT_REVIEW.md, engine/prompts/PROMPT_SDD.md, engine/prompts/PROMPT_SPECKIT_EXPORT.md, engine/prompts/PROMPT_TRANSCRICAO_REUNIAO.md, engine/prompts/PROMPT_TRIAGEM.md, engine/prompts/PROMPT_WIZARD.md, engine/prompts/SYSTEM_PROMPT_analista_requisitos.md, engine/templates/.claude/settings.json, engine/templates/.github/CODEOWNERS, engine/templates/.github/README.md, engine/templates/.github/pull_request_template.md, engine/templates/analise-impacto/_TEMPLATE_AIM.md, engine/templates/analise-impacto/_TEMPLATE_AIM_SPRINT.md, engine/templates/ci/spec-guard.yml, engine/templates/ci/valida-artefatos-previstos.yml, engine/templates/global/ALI-AIE-MAP.md, engine/templates/global/API-PATTERNS.md, engine/templates/global/AUTHZ.md, engine/templates/global/CLAUDE.md, engine/templates/global/CONTAGEM-PF.md, engine/templates/global/DATA-MODEL.md, engine/templates/global/DESIGN-SYSTEM.md, engine/templates/global/ERROR-DICTIONARY.md, engine/templates/global/FIELD-DICTIONARY.md, engine/templates/global/MASTER.md, engine/templates/global/MESSAGE-DICTIONARY.md, engine/templates/global/N0_PRODUCT_VISION.md, engine/templates/global/NFR.md, engine/templates/global/PATTERNS.md, engine/templates/global/RULES-DICTIONARY.md, engine/templates/global/SIZING.md, engine/templates/global/VOCABULARY-OVERRIDES.md, engine/templates/global/data-models/_template-artefatos.md, engine/templates/global/data-models/_template-dominio-negocio.md, engine/templates/global/data-models/_template-dominio.md, engine/templates/impactos/_TEMPLATE_IMPACTO.md, engine/templates/modules/INDEX.md, engine/templates/modules/_base-conhecimento/_template-base-conhecimento.md, engine/templates/modules/_template-dominio/README.md, engine/templates/modules/_template-dominio/_template-feature-set/README.md, engine/templates/modules/_template-dominio/_template-feature-set/_template-feature.md, engine/templates/prototypes/INDEX.md, engine/templates/prototypes/_biblioteca-ds/README.md, engine/templates/prototypes/_template/_template-dominio/README.md, engine/templates/prototypes/_template/_template-dominio/_template-feature-set/README.md, engine/templates/prototypes/_template/_template-dominio/_template-feature-set/_template-feature/README.md, engine/templates/repos/_template-repo.md, engine/templates/scripts/gates.py, frontend-aval/README.md, global/ALI-AIE-MAP.md, global/API-PATTERNS.md, global/CONTAGEM-PF.md, global/DATA-MODEL.md, global/DESIGN-SYSTEM.md, global/DIAGRAMA-ER.md, global/ERROR-DICTIONARY.md, global/FIELD-DICTIONARY.md, global/MASTER.md, global/NFR.md, global/PATTERNS.md, global/PLANO-IMPLEMENTACAO.md, global/RULES-DICTIONARY.md, global/SIZING.md, global/VOCABULARY-OVERRIDES.md, global/data-models/demandas.md, identidade-visual/README.md, index.html, modules/INDEX.md, modules/_backlog/.gitkeep, modules/administracao/README.md, modules/administracao/auditoria/README.md, modules/administracao/conta/README.md, modules/administracao/conta/f-trocar-conta.md, modules/administracao/integracoes/README.md, modules/administracao/modelos-ia/README.md, modules/administracao/modelos-ia/f-configurar-modelo-por-etapa.md, modules/administracao/organizacao/README.md, modules/administracao/perfis/README.md, modules/administracao/perfis/f-visualizar-matriz-de-perfis.md, modules/administracao/usuarios/README.md, modules/agentes/README.md, modules/agentes/execucao/README.md, modules/agentes/execucao/f-gerar-prototipo.md, modules/demandas/README.md, modules/demandas/intake/README.md, modules/demandas/intake/f-iniciar-execucao-do-acervo.md, modules/demandas/painel/README.md, modules/demandas/painel/f-cancelar-demanda.md, modules/esteira/README.md, modules/esteira/acompanhamento/README.md, modules/esteira/acompanhamento/f-consultar-consumo-de-ia.md, modules/esteira/acompanhamento/f-consultar-saude-das-esteiras.md, modules/esteira/acompanhamento/f-visualizar-prototipo.md, modules/esteira/aprovacoes/README.md, modules/esteira/aprovacoes/f-responder-esclarecimentos.md, modules/operacao/README.md, modules/operacao/gestao-contas/README.md, modules/operacao/gestao-contas/f-criar-organizacao-operador.md, modules/operacao/gestao-contas/f-definir-limites-de-consumo.md, modules/operacao/gestao-contas/f-editar-organizacao-operador.md, modules/operacao/gestao-contas/f-entrar-como.md, modules/operacao/gestao-contas/f-listar-contas.md, modules/operacao/gestao-contas/f-reativar-conta.md, modules/operacao/gestao-contas/f-suspender-conta.md, modules/sistemas/README.md, modules/sistemas/acervo/README.md, modules/sistemas/acervo/f-visualizar-catalogo-de-features.md, modules/sistemas/acervo/f-visualizar-mapa-de-features.md, modules/sistemas/cadastro/README.md, modules/sistemas/configuracoes/README.md, pending_changes.md, prototypes/_biblioteca-ds/README.md, prototypes/_gerados/README.md, prototypes/aval/README.md, prototypes/aval/adm-modelos-ia.html, prototypes/aval/app-mobile.html, prototypes/aval/catalogo-features.html, prototypes/aval/configuracoes.html, prototypes/aval/console-siesa-conta.html, prototypes/aval/console-siesa.html, prototypes/aval/esteira-reajuste.html, prototypes/aval/esteira.html, prototypes/aval/etapa-casos-teste.html, prototypes/aval/etapa-codificacao-reajuste.html, prototypes/aval/etapa-codificacao.html, prototypes/aval/etapa-impacto.html, prototypes/aval/etapa-implantacao.html, prototypes/aval/etapa-modelo-dados.html, prototypes/aval/etapa-prototipo.html, prototypes/aval/etapa-requisitos-esclarecimentos.html, prototypes/aval/etapa-requisitos.html, prototypes/aval/etapa-testes-sistema-reexecucao.html, prototypes/aval/etapa-testes-sistema-reprovado.html, prototypes/aval/etapa-testes-sistema.html, prototypes/aval/mapa-features.html, prototypes/aval/nova-demanda.html, prototypes/aval/painel.html, prototypes/aval/preparar-sistema-chat.html, prototypes/aval/preparar-sistema-hibrido.html, prototypes/aval/preparar-sistema.html, prototypes/aval/telas.js, prototypes/editor-analista/README.md, prototypes/editor-analista/index.html, rastreabilidade/data.js, rastreabilidade/graph.js, rastreabilidade/index.html, rastreabilidade/styles.css, repos/INDEX.md, scripts/atualiza-pages.mjs, scripts/audit-trace-links.mjs, scripts/build-trace-data.mjs, scripts/delta-n3.mjs, scripts/gates.py, scripts/generate-impact-draft.mjs, scripts/generate-trace-index.mjs, scripts/generate-usage-index.mjs, scripts/gera-aprovacoes.mjs, scripts/gera-diagrama-er.mjs, scripts/gera-html-impacto.mjs, scripts/gera-mapa-features.mjs, scripts/gera-pendencias.mjs, scripts/gera-planilha-contagem.py, scripts/hooks/spec-guard.mjs, scripts/lib/front-matter.mjs, scripts/lib/mapa-codigo.mjs, scripts/lib/pe.mjs, scripts/lib/trace-index.mjs, scripts/migra-aim.mjs, scripts/migra-enumeracao.py, scripts/pendencias-ids.json, scripts/preflight-spec.mjs, scripts/regen.sh, scripts/resolve-refs.mjs, scripts/stamp.sh, scripts/suspect-links.mjs, scripts/valida-acessorio-tela.mjs, scripts/valida-artefatos-previstos.mjs, scripts/valida-citacoes-dicionario.mjs, scripts/valida-contagem-consolidada.mjs, scripts/valida-enumeracao-contagem.mjs, scripts/valida-fluxo-principal.mjs, scripts/validate-doc.mjs, scripts/validate-feature-semantics.mjs, scripts/validate-impact.mjs, scripts/verifica-texto-corrido.mjs
- Pontos de entrada novos não aparecem aqui: são identificados na extração da versão posterior (RD-02).

