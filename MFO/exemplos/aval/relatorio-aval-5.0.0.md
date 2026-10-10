# Relatório MFO — Aval (siesa-doc) 5.0.0

**Rótulo:** 492 PFO · MFO 1.0 · nível R · evidência 100% · agente: ferramenta (extrair_n3.py 1.0); sem revisão humana · escopo: Aval (siesa-doc) 5.0.0, features de todos os domínios: ADM, AGT, DEM, EST, OPE, SIS

**Produção:** M2 IA dirigida 492 PFO (100%)

**Propósito:** Medir o tamanho funcional especificado na documentação N3 (extração mecânica)

## Perfil funcional

| Indicador | Valor |
|---|---|
| PFO | **492** |
| NP (processos) | 85 |
| NE (entidades) | 20 |
| E / X / R / W | 101 / 158 / 157 / 76 |
| Densidade (PFO/NP) | 5,79 |
| Persistência ((R+W)/PFO) | 0,47 |
| Interface ((E+X)/PFO) | 0,53 |
| Entidades por processo (NE/NP) | 0,24 |
| Evidência | 100% (0 inferidos) |
| D (derivação, RC-05) | 0 de 0 (85 n/d) |

## Processos

| ID | Processo | E | X | R | W | PFO | Deriv. | Evid. | Modo | Aceite |
|---|---|---|---|---|---|---|---|---|---|---|
| ADM-AUD-01 | Pesquisar auditoria | 1 | 3 | 2 | 0 | **6** | n/d | 6/6 | M2 | — |
| ADM-CTA-02 | Autenticar usuário | 2 | 2 | 4 | 2 | **10** | n/d | 10/10 | M2 | — |
| ADM-CTA-01 | Criar conta | 2 | 2 | 2 | 3 | **9** | n/d | 9/9 | M2 | — |
| ADM-CTA-03 | Recuperar senha | 1 | 2 | 1 | 2 | **6** | n/d | 6/6 | M2 | — |
| ADM-CTA-03.2 | Redefinir a senha | 1 | 2 | 1 | 1 | **5** | n/d | 5/5 | M2 | — |
| ADM-CTA-04 | Trocar de conta | 1 | 4 | 2 | 1 | **8** | n/d | 8/8 | M2 | — |
| ADM-INT-01 | Configurar conexão GitHub | 1 | 3 | 3 | 2 | **9** | n/d | 9/9 | M2 | — |
| ADM-INT-01.2 | Processar revogação (webhook do GitHub) | 1 | 2 | 1 | 1 | **5** | n/d | 5/5 | M2 | — |
| ADM-MOD-01 | Configurar modelo por etapa | 1 | 3 | 1 | 1 | **6** | n/d | 6/6 | M2 | — |
| ADM-ORG-03 | Alterar organização | 1 | 2 | 0 | 1 | **4** | n/d | 4/4 | M2 | — |
| ADM-ORG-01 | Criar organização | 1 | 2 | 1 | 3 | **7** | n/d | 7/7 | M2 | — |
| ADM-ORG-02 | Visualizar organização | 1 | 2 | 4 | 0 | **7** | n/d | 7/7 | M2 | — |
| ADM-PER-05 | Ativar funcionalidade | 1 | 2 | 1 | 2 | **6** | n/d | 6/6 | M2 | — |
| ADM-PER-02 | Conceder funcionalidade | 1 | 2 | 3 | 3 | **9** | n/d | 9/9 | M2 | — |
| ADM-PER-01 | Criar perfil | 1 | 2 | 1 | 2 | **6** | n/d | 6/6 | M2 | — |
| ADM-PER-04 | Desativar funcionalidade | 1 | 2 | 1 | 2 | **6** | n/d | 6/6 | M2 | — |
| ADM-PER-03 | Revogar funcionalidade | 1 | 2 | 3 | 2 | **8** | n/d | 8/8 | M2 | — |
| ADM-PER-06 | Visualizar matriz de perfis e funcionalidades | 1 | 2 | 2 | 0 | **5** | n/d | 5/5 | M2 | — |
| ADM-USR-06 | Aceitar convite | 1 | 3 | 4 | 2 | **10** | n/d | 10/10 | M2 | — |
| ADM-USR-03 | Alterar perfil do usuário | 1 | 3 | 1 | 1 | **6** | n/d | 6/6 | M2 | — |
| ADM-USR-02 | Convidar usuário | 1 | 3 | 1 | 2 | **7** | n/d | 7/7 | M2 | — |
| ADM-USR-04 | Desativar usuário | 1 | 2 | 0 | 1 | **4** | n/d | 4/4 | M2 | — |
| ADM-USR-01 | Pesquisar usuários | 1 | 3 | 2 | 0 | **6** | n/d | 6/6 | M2 | — |
| ADM-USR-05 | Reativar usuário | 1 | 2 | 0 | 1 | **4** | n/d | 4/4 | M2 | — |
| AGT-EXE-02 | Detalhar requisitos | 2 | 0 | 2 | 1 | **5** | n/d | 5/5 | M2 | — |
| AGT-EXE-07 | Executar testes do sistema | 2 | 1 | 1 | 2 | **6** | n/d | 6/6 | M2 | — |
| AGT-EXE-10 | Gerar análise de impacto | 2 | 0 | 2 | 1 | **5** | n/d | 5/5 | M2 | — |
| AGT-EXE-04 | Gerar casos de teste | 2 | 0 | 2 | 1 | **5** | n/d | 5/5 | M2 | — |
| AGT-EXE-06 | Gerar código | 2 | 0 | 2 | 1 | **5** | n/d | 5/5 | M2 | — |
| AGT-EXE-03 | Gerar modelo de dados | 2 | 0 | 2 | 1 | **5** | n/d | 5/5 | M2 | — |
| AGT-EXE-05 | Gerar plano de implementação | 2 | 0 | 2 | 1 | **5** | n/d | 5/5 | M2 | — |
| AGT-EXE-09 | Gerar preparação do sistema | 1 | 0 | 2 | 2 | **5** | n/d | 5/5 | M2 | — |
| AGT-EXE-09.2 | Materializar preparação aprovada (agente) | 1 | 1 | 0 | 0 | **2** | n/d | 2/2 | M2 | — |
| AGT-EXE-11 | Gerar protótipo | 2 | 2 | 2 | 1 | **7** | n/d | 7/7 | M2 | — |
| AGT-EXE-08 | Preparar implantação | 2 | 0 | 1 | 2 | **5** | n/d | 5/5 | M2 | — |
| AGT-EXE-01 | Processar triagem | 2 | 0 | 1 | 1 | **4** | n/d | 4/4 | M2 | — |
| DEM-INT-02 | Iniciar esteira | 1 | 2 | 2 | 2 | **7** | n/d | 7/7 | M2 | — |
| DEM-INT-03 | Iniciar execução do acervo | 1 | 2 | 1 | 2 | **6** | n/d | 6/6 | M2 | — |
| DEM-INT-01 | Registrar demanda | 1 | 2 | 1 | 2 | **6** | n/d | 6/6 | M2 | — |
| DEM-PAI-02 | Cancelar demanda | 1 | 2 | 3 | 1 | **7** | n/d | 7/7 | M2 | — |
| DEM-PAI-01 | Pesquisar demandas | 1 | 2 | 2 | 0 | **5** | n/d | 5/5 | M2 | — |
| DEM-PAI-01.2 | Consultar resumo do painel (contadores) | 1 | 2 | 0 | 0 | **3** | n/d | 3/3 | M2 | — |
| EST-ACO-01 | Acompanhar esteira | 1 | 2 | 3 | 0 | **6** | n/d | 6/6 | M2 | — |
| EST-ACO-10 | Consultar consumo de IA | 1 | 2 | 3 | 0 | **6** | n/d | 6/6 | M2 | — |
| EST-ACO-09 | Consultar saúde das esteiras | 1 | 2 | 3 | 0 | **6** | n/d | 6/6 | M2 | — |
| EST-ACO-08 | Visualizar análise de impacto | 1 | 2 | 3 | 0 | **6** | n/d | 6/6 | M2 | — |
| EST-ACO-04 | Visualizar casos de teste | 1 | 2 | 3 | 0 | **6** | n/d | 6/6 | M2 | — |
| EST-ACO-05 | Visualizar codificação | 1 | 2 | 3 | 0 | **6** | n/d | 6/6 | M2 | — |
| EST-ACO-07 | Visualizar implantação | 1 | 2 | 3 | 0 | **6** | n/d | 6/6 | M2 | — |
| EST-ACO-03 | Visualizar modelo de dados | 1 | 2 | 4 | 0 | **7** | n/d | 7/7 | M2 | — |
| EST-ACO-11 | Visualizar protótipo | 2 | 2 | 1 | 0 | **5** | n/d | 5/5 | M2 | — |
| EST-ACO-02 | Visualizar requisitos | 1 | 2 | 3 | 0 | **6** | n/d | 6/6 | M2 | — |
| EST-ACO-06 | Visualizar testes do sistema | 1 | 2 | 3 | 0 | **6** | n/d | 6/6 | M2 | — |
| EST-APR-09 | Aprovar escopo de impacto | 1 | 2 | 2 | 1 | **6** | n/d | 6/6 | M2 | — |
| EST-APR-01 | Aprovar etapa | 1 | 2 | 3 | 1 | **7** | n/d | 7/7 | M2 | — |
| EST-APR-03 | Aprovar feature | 1 | 2 | 1 | 1 | **5** | n/d | 5/5 | M2 | — |
| EST-APR-04 | Aprovar história | 1 | 2 | 2 | 1 | **6** | n/d | 6/6 | M2 | — |
| EST-APR-07 | Autorizar implantação | 2 | 2 | 4 | 0 | **8** | n/d | 8/8 | M2 | — |
| EST-APR-06 | Homologar entrega | 1 | 2 | 2 | 1 | **6** | n/d | 6/6 | M2 | — |
| EST-APR-08 | Listar pendências | 1 | 2 | 3 | 0 | **6** | n/d | 6/6 | M2 | — |
| EST-APR-05 | Reprovar testes do sistema | 1 | 2 | 4 | 0 | **7** | n/d | 7/7 | M2 | — |
| EST-APR-10 | Responder esclarecimentos | 1 | 2 | 3 | 1 | **7** | n/d | 7/7 | M2 | — |
| EST-APR-02 | Solicitar ajustes | 1 | 2 | 2 | 1 | **6** | n/d | 6/6 | M2 | — |
| OPE-GCO-02 | Criar organização | 1 | 2 | 3 | 1 | **7** | n/d | 7/7 | M2 | — |
| OPE-GCO-06 | Definir limites de consumo | 1 | 2 | 1 | 1 | **5** | n/d | 5/5 | M2 | — |
| OPE-GCO-03 | Editar organização | 1 | 2 | 1 | 1 | **5** | n/d | 5/5 | M2 | — |
| OPE-GCO-07 | Entrar como | 1 | 2 | 1 | 1 | **5** | n/d | 5/5 | M2 | — |
| OPE-GCO-01 | Listar contas | 1 | 2 | 5 | 0 | **8** | n/d | 8/8 | M2 | — |
| OPE-GCO-01.2 | Consultar resumo da plataforma | 1 | 2 | 0 | 0 | **3** | n/d | 3/3 | M2 | — |
| OPE-GCO-05 | Reativar conta | 1 | 2 | 1 | 1 | **5** | n/d | 5/5 | M2 | — |
| OPE-GCO-04 | Suspender conta | 1 | 2 | 1 | 1 | **5** | n/d | 5/5 | M2 | — |
| SIS-ACE-01 | Visualizar catálogo de features | 1 | 2 | 3 | 0 | **6** | n/d | 6/6 | M2 | — |
| SIS-ACE-02 | Visualizar mapa de features | 1 | 2 | 2 | 0 | **5** | n/d | 5/5 | M2 | — |
| SIS-CAD-04 | Alterar sistema | 1 | 2 | 1 | 1 | **5** | n/d | 5/5 | M2 | — |
| SIS-CAD-01 | Cadastrar sistema | 1 | 2 | 1 | 1 | **5** | n/d | 5/5 | M2 | — |
| SIS-CAD-02 | Definir sistema ativo | 1 | 1 | 1 | 0 | **3** | n/d | 3/3 | M2 | — |
| SIS-CAD-05 | Preparar sistema | 1 | 2 | 3 | 1 | **7** | n/d | 7/7 | M2 | — |
| SIS-CAD-05.2 | Acompanhar preparação e proposta | 1 | 2 | 0 | 0 | **3** | n/d | 3/3 | M2 | — |
| SIS-CAD-05.3 | Aprovar proposta de preparação | 1 | 2 | 0 | 0 | **3** | n/d | 3/3 | M2 | — |
| SIS-CAD-05.4 | Solicitar ajustes na proposta | 1 | 2 | 0 | 0 | **3** | n/d | 3/3 | M2 | — |
| SIS-CAD-03 | Transferir sistema | 1 | 2 | 2 | 1 | **6** | n/d | 6/6 | M2 | — |
| SIS-CFG-02 | Configurar aprovadores | 1 | 2 | 2 | 1 | **6** | n/d | 6/6 | M2 | — |
| SIS-CFG-03 | Configurar estratégia | 1 | 2 | 0 | 1 | **4** | n/d | 4/4 | M2 | — |
| SIS-CFG-04 | Configurar ferramenta de demandas | 1 | 2 | 1 | 0 | **4** | n/d | 4/4 | M2 | — |
| SIS-CFG-01 | Configurar repositórios | 3 | 2 | 1 | 1 | **7** | n/d | 7/7 | M2 | — |
| | **Total** | 101 | 158 | 157 | 76 | **492** | | | | |

## Produção

| Modo de produção | Processos | PFO | % |
|---|---|---|---|
| M0 humano | 0 | 0 | 0% |
| M1 IA assistida | 0 | 0 | 0% |
| M2 IA dirigida | 85 | 492 | 100% |
| M3 IA autônoma | 0 | 0 | 0% |


## Avisos

- V-09: processos 'ADM-PER-05' e 'ADM-PER-04' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'ADM-USR-04' e 'ADM-USR-05' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'AGT-EXE-02' e 'AGT-EXE-04' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'AGT-EXE-02' e 'AGT-EXE-06' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'AGT-EXE-02' e 'AGT-EXE-03' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'AGT-EXE-02' e 'AGT-EXE-05' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'EST-ACO-01' e 'EST-ACO-09' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'EST-ACO-04' e 'EST-ACO-05' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'EST-ACO-04' e 'EST-ACO-07' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'EST-ACO-04' e 'EST-ACO-02' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'EST-ACO-04' e 'EST-ACO-06' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'EST-APR-09' e 'EST-APR-04' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'EST-APR-09' e 'EST-APR-06' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'OPE-GCO-06' e 'OPE-GCO-03' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'OPE-GCO-06' e 'OPE-GCO-07' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'OPE-GCO-06' e 'OPE-GCO-05' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'OPE-GCO-06' e 'OPE-GCO-04' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'SIS-CAD-04' e 'SIS-CAD-01' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'SIS-CAD-05.2' e 'SIS-CAD-05.3' têm a mesma assinatura; verifique RI-04 b
- V-09: processos 'SIS-CAD-05.2' e 'SIS-CAD-05.4' têm a mesma assinatura; verifique RI-04 b
