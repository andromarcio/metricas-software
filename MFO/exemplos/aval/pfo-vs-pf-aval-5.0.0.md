# PFO (extração mecânica) × PF (memória de cálculo dos N3) — Aval 5.0.0

> PFO: `extrair_n3.py` sobre siesa-doc@49265a9 (piso mecânico, sem revisão). PF: soma da tabela `## Métricas de tamanho` de cada N3, como registrada pela equipe.

## Por domínio

| Domínio | Processos | PFO | PF | PFO/PF |
|---|---|---|---|---|
| ADM | 24 | 159 | 117 | 1.36 |
| AGT | 12 | 59 | 68 | 0.87 |
| DEM | 6 | 34 | 31 | 1.10 |
| EST | 21 | 130 | 106 | 1.23 |
| OPE | 8 | 43 | 31 | 1.39 |
| SIS | 14 | 67 | 69 | 0.97 |
| **Total** | **85** | **492** | **422** | **1.17** |

## Por feature set

| Feature set | Processos | PFO | PF | PFO/PF |
|---|---|---|---|---|
| ADM-AUD | 1 | 6 | 4 | 1.50 |
| ADM-CTA | 5 | 38 | 29 | 1.31 |
| ADM-INT | 2 | 14 | 11 | 1.27 |
| ADM-MOD | 1 | 6 | 3 | 2.00 |
| ADM-ORG | 3 | 18 | 16 | 1.12 |
| ADM-PER | 6 | 40 | 20 | 2.00 |
| ADM-USR | 6 | 37 | 34 | 1.09 |
| AGT-EXE | 12 | 59 | 68 | 0.87 |
| DEM-INT | 3 | 19 | 16 | 1.19 |
| DEM-PAI | 3 | 15 | 15 | 1.00 |
| EST-ACO | 11 | 66 | 59 | 1.12 |
| EST-APR | 10 | 64 | 47 | 1.36 |
| OPE-GCO | 8 | 43 | 31 | 1.39 |
| SIS-ACE | 2 | 11 | 10 | 1.10 |
| SIS-CAD | 8 | 35 | 36 | 0.97 |
| SIS-CFG | 4 | 21 | 23 | 0.91 |

## Por processo

| Processo | Nome | Tipo APF | PF | PFO | Movimentos |
|---|---|---|---|---|---|
| ADM-AUD-01 | Pesquisar auditoria | CE | 4 | 6 | E EventoAuditoria · R EventoAuditoria · R Usuario · X EventoAuditoria · X MENSAGEM · X Usuario |
| ADM-CTA-02 | Autenticar usuário | EE | 6 | 10 | E Identidade Google · E Pessoa · R Conta · R EventoAuditoria · R Identidade Google · R Perfil · W EventoAuditoria · W Usuario · X MENSAGEM · X Usuario |
| ADM-CTA-01 | Criar conta | EE | 6 | 9 | E Identidade Google · E Pessoa · R EventoAuditoria · R Identidade Google · W Conta · W EventoAuditoria · W Usuario · X MENSAGEM · X Pessoa |
| ADM-CTA-03 | Recuperar senha | EE | 3 | 6 | E Pessoa · R EventoAuditoria · W EventoAuditoria · W Usuario · X MENSAGEM · X Usuario |
| ADM-CTA-03.2 | Redefinir a senha | EE | 4 | 5 | E Usuario · R EventoAuditoria · W Usuario · X MENSAGEM · X Usuario |
| ADM-CTA-04 | Trocar de conta | EE | 10 | 8 | E Pessoa · R Conta · R Usuario · W Pessoa · X Conta · X MENSAGEM · X Pessoa · X Usuario |
| ADM-INT-01 | Configurar conexão GitHub | EE | 8 | 9 | E GitHub · R Conta · R EventoAuditoria · R GitHub · W Conta · W EventoAuditoria · X Conta · X GitHub · X MENSAGEM |
| ADM-INT-01.2 | Processar revogação (webhook do GitHub) | EE | 3 | 5 | E GitHub · R EventoAuditoria · W Conta · X GitHub · X MENSAGEM |
| ADM-MOD-01 | Configurar modelo por etapa | EE | 3 | 6 | E ModeloEtapa · R Conta · W Conta · X Conta · X MENSAGEM · X ModeloEtapa |
| ADM-ORG-03 | Alterar organização | EE | 3 | 4 | E Conta · W Conta · X Conta · X MENSAGEM |
| ADM-ORG-01 | Criar organização | EE | 6 | 7 | E Conta · R Perfil · W Conta · W Perfil · W Usuario · X Conta · X MENSAGEM |
| ADM-ORG-02 | Visualizar organização | SE | 7 | 7 | E DISPARO · R Conta · R Perfil · R Sistema · R Usuario · X Conta · X MENSAGEM |
| ADM-PER-05 | Ativar funcionalidade | EE | 3 | 6 | E Funcionalidade · R EventoAuditoria · W EventoAuditoria · W Funcionalidade · X Funcionalidade · X MENSAGEM |
| ADM-PER-02 | Conceder funcionalidade | EE | 3 | 9 | E PerfilFuncionalidade · R EventoAuditoria · R Funcionalidade · R Perfil · W EventoAuditoria · W Funcionalidade · W Perfil · X Funcionalidade · X MENSAGEM |
| ADM-PER-01 | Criar perfil | EE | 4 | 6 | E Perfil · R EventoAuditoria · W EventoAuditoria · W Perfil · X MENSAGEM · X Perfil |
| ADM-PER-04 | Desativar funcionalidade | EE | 3 | 6 | E Funcionalidade · R EventoAuditoria · W EventoAuditoria · W Funcionalidade · X Funcionalidade · X MENSAGEM |
| ADM-PER-03 | Revogar funcionalidade | EE | 3 | 8 | E PerfilFuncionalidade · R EventoAuditoria · R Funcionalidade · R Perfil · W EventoAuditoria · W Funcionalidade · X Funcionalidade · X MENSAGEM |
| ADM-PER-06 | Visualizar matriz de perfis e funcionalidades | CE | 4 | 5 | E Funcionalidade · R Funcionalidade · R Perfil · X Funcionalidade · X MENSAGEM |
| ADM-USR-06 | Aceitar convite | EE | 10 | 10 | E Pessoa · R Conta · R Convite · R Perfil · R Usuario · W Convite · W Usuario · X Conta · X Convite · X MENSAGEM |
| ADM-USR-03 | Alterar perfil do usuário | EE | 4 | 6 | E Usuario · R Perfil · W Usuario · X MENSAGEM · X Perfil · X Usuario |
| ADM-USR-02 | Convidar usuário | EE | 9 | 7 | E Convite · R Perfil · W Convite · W Usuario · X Convite · X MENSAGEM · X Perfil |
| ADM-USR-04 | Desativar usuário | EE | 3 | 4 | E Usuario · W Usuario · X MENSAGEM · X Usuario |
| ADM-USR-01 | Pesquisar usuários | SE | 5 | 6 | E Usuario · R Perfil · R Usuario · X MENSAGEM · X Perfil · X Usuario |
| ADM-USR-05 | Reativar usuário | EE | 3 | 4 | E Usuario · W Usuario · X MENSAGEM · X Usuario |
| AGT-EXE-02 | Detalhar requisitos | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-07 | Executar testes do sistema | EE | 6 | 6 | E DISPARO · E GitHub · R Demanda · W EsteiraExecucao · W ExecucaoAgente · X MENSAGEM |
| AGT-EXE-10 | Gerar análise de impacto | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R ExecucaoAgente · W EsteiraExecucao |
| AGT-EXE-04 | Gerar casos de teste | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-06 | Gerar código | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-03 | Gerar modelo de dados | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-05 | Gerar plano de implementação | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-09 | Gerar preparação do sistema | EE | 4 | 5 | E ExecucaoAgente · R Conta · R Sistema · W ExecucaoAgente · W Sistema |
| AGT-EXE-09.2 | Materializar preparação aprovada (agente) | EE | 6 | 2 | E ExecucaoAgente · X MENSAGEM |
| AGT-EXE-11 | Gerar protótipo | EE | 6 | 7 | E DISPARO · E GitHub · R Demanda · R ExecucaoAgente · W EsteiraExecucao · X EtapaExecucao · X MENSAGEM |
| AGT-EXE-08 | Preparar implantação | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · W EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-01 | Processar triagem | EE | 4 | 4 | E DISPARO · E GitHub · R Demanda · W ExecucaoAgente |
| DEM-INT-02 | Iniciar esteira | EE | 6 | 7 | E Demanda · R EventoAuditoria · R Sistema · W Demanda · W EsteiraExecucao · X Demanda · X MENSAGEM |
| DEM-INT-03 | Iniciar execução do acervo | EE | 6 | 6 | E Demanda · R Sistema · W Demanda · W EsteiraExecucao · X Demanda · X MENSAGEM |
| DEM-INT-01 | Registrar demanda | EE | 4 | 6 | E Demanda · R Sistema · W Demanda · W EventoAuditoria · X Demanda · X MENSAGEM |
| DEM-PAI-02 | Cancelar demanda | EE | 6 | 7 | E Demanda · R EsteiraExecucao · R EventoAuditoria · R ExecucaoAgente · W Demanda · X Demanda · X MENSAGEM |
| DEM-PAI-01 | Pesquisar demandas | SE | 5 | 5 | E Demanda · R EsteiraExecucao · R Perfil · X Demanda · X MENSAGEM |
| DEM-PAI-01.2 | Consultar resumo do painel (contadores) | CE | 4 | 3 | E Demanda · X Demanda · X MENSAGEM |
| EST-ACO-01 | Acompanhar esteira | SE | 7 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EsteiraExecucao · X MENSAGEM |
| EST-ACO-10 | Consultar consumo de IA | SE | 5 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X ExecucaoAgente · X MENSAGEM |
| EST-ACO-09 | Consultar saúde das esteiras | SE | 5 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EsteiraExecucao · X MENSAGEM |
| EST-ACO-08 | Visualizar análise de impacto | CE | 6 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X MENSAGEM · X RegistroImpacto |
| EST-ACO-04 | Visualizar casos de teste | CE | 6 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EtapaExecucao · X MENSAGEM |
| EST-ACO-05 | Visualizar codificação | CE | 6 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EtapaExecucao · X MENSAGEM |
| EST-ACO-07 | Visualizar implantação | CE | 4 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EtapaExecucao · X MENSAGEM |
| EST-ACO-03 | Visualizar modelo de dados | CE | 6 | 7 | E DISPARO · R Demanda · R EsteiraExecucao · R EventoAgente · R ExecucaoAgente · X EtapaExecucao · X MENSAGEM |
| EST-ACO-11 | Visualizar protótipo | CE | 4 | 5 | E DISPARO · E GitHub · R EtapaExecucao · X EtapaExecucao · X MENSAGEM |
| EST-ACO-02 | Visualizar requisitos | CE | 6 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EtapaExecucao · X MENSAGEM |
| EST-ACO-06 | Visualizar testes do sistema | CE | 4 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EtapaExecucao · X MENSAGEM |
| EST-APR-09 | Aprovar escopo de impacto | EE | 4 | 6 | E PendenciaAprovacao · R EventoAuditoria · R Sistema · W EsteiraExecucao · X MENSAGEM · X PendenciaAprovacao |
| EST-APR-01 | Aprovar etapa | EE | 6 | 7 | E PendenciaAprovacao · R EventoAuditoria · R Perfil · R Sistema · W EsteiraExecucao · X MENSAGEM · X PendenciaAprovacao |
| EST-APR-03 | Aprovar feature | EE | 4 | 5 | E PendenciaAprovacao · R EventoAuditoria · W EsteiraExecucao · X MENSAGEM · X PendenciaAprovacao |
| EST-APR-04 | Aprovar história | EE | 4 | 6 | E PendenciaAprovacao · R EventoAuditoria · R Sistema · W EsteiraExecucao · X MENSAGEM · X PendenciaAprovacao |
| EST-APR-07 | Autorizar implantação | EE | 6 | 8 | E GitHub · E PendenciaAprovacao · R EsteiraExecucao · R EventoAuditoria · R Perfil · R Sistema · X MENSAGEM · X PendenciaAprovacao |
| EST-APR-06 | Homologar entrega | EE | 4 | 6 | E PendenciaAprovacao · R EventoAuditoria · R Sistema · W EsteiraExecucao · X MENSAGEM · X PendenciaAprovacao |
| EST-APR-08 | Listar pendências | SE | 5 | 6 | E PendenciaAprovacao · R Demanda · R EsteiraExecucao · R Perfil · X MENSAGEM · X PendenciaAprovacao |
| EST-APR-05 | Reprovar testes do sistema | EE | 6 | 7 | E PendenciaAprovacao · R EsteiraExecucao · R EventoAuditoria · R Perfil · R Sistema · X MENSAGEM · X PendenciaAprovacao |
| EST-APR-10 | Responder esclarecimentos | EE | 4 | 7 | E PendenciaAprovacao · R EsteiraExecucao · R EventoAuditoria · R ExecucaoAgente · W ExecucaoAgente · X MENSAGEM · X PendenciaAprovacao |
| EST-APR-02 | Solicitar ajustes | EE | 4 | 6 | E PendenciaAprovacao · R EventoAuditoria · R ExecucaoAgente · W EsteiraExecucao · X MENSAGEM · X PendenciaAprovacao |
| OPE-GCO-02 | Criar organização | EE | 6 | 7 | E Conta · R Convite · R EventoAuditoria · R Usuario · W Conta · X Conta · X MENSAGEM |
| OPE-GCO-06 | Definir limites de consumo | EE | 3 | 5 | E Conta · R EventoAuditoria · W Conta · X Conta · X MENSAGEM |
| OPE-GCO-03 | Editar organização | EE | 3 | 5 | E Conta · R EventoAuditoria · W Conta · X Conta · X MENSAGEM |
| OPE-GCO-07 | Entrar como | EE | 3 | 5 | E Conta · R EventoAuditoria · W Conta · X Conta · X MENSAGEM |
| OPE-GCO-01 | Listar contas | SE | 5 | 8 | E Conta · R Conta · R EsteiraExecucao · R ExecucaoAgente · R Sistema · R Usuario · X Conta · X MENSAGEM |
| OPE-GCO-01.2 | Consultar resumo da plataforma | CE | 4 | 3 | E Conta · X Conta · X MENSAGEM |
| OPE-GCO-05 | Reativar conta | EE | 3 | 5 | E Conta · R EventoAuditoria · W Conta · X Conta · X MENSAGEM |
| OPE-GCO-04 | Suspender conta | EE | 4 | 5 | E Conta · R EventoAuditoria · W Conta · X Conta · X MENSAGEM |
| SIS-ACE-01 | Visualizar catálogo de features | SE | 5 | 6 | E Sistema · R Demanda · R EsteiraExecucao · R Sistema · X MENSAGEM · X Sistema |
| SIS-ACE-02 | Visualizar mapa de features | SE | 5 | 5 | E DISPARO · R EsteiraExecucao · R Sistema · X MENSAGEM · X Sistema |
| SIS-CAD-04 | Alterar sistema | EE | 4 | 5 | E Sistema · R EventoAuditoria · W Sistema · X MENSAGEM · X Sistema |
| SIS-CAD-01 | Cadastrar sistema | EE | 4 | 5 | E Sistema · R EventoAuditoria · W Sistema · X MENSAGEM · X Sistema |
| SIS-CAD-02 | Definir sistema ativo | CE | 4 | 3 | E Sistema · R EsteiraExecucao · X Sistema |
| SIS-CAD-05 | Preparar sistema | EE | 4 | 7 | E Sistema · R Conta · R ExecucaoAgente · R Usuario · W Sistema · X MENSAGEM · X Sistema |
| SIS-CAD-05.2 | Acompanhar preparação e proposta | CE | 4 | 3 | E Sistema · X MENSAGEM · X Sistema |
| SIS-CAD-05.3 | Aprovar proposta de preparação | EE | 4 | 3 | E Sistema · X MENSAGEM · X Sistema |
| SIS-CAD-05.4 | Solicitar ajustes na proposta | EE | 3 | 3 | E Sistema · X MENSAGEM · X Sistema |
| SIS-CAD-03 | Transferir sistema | EE | 9 | 6 | E Sistema · R Conta · R Usuario · W Sistema · X MENSAGEM · X Sistema |
| SIS-CFG-02 | Configurar aprovadores | EE | 7 | 6 | E Sistema · R EventoAuditoria · R Perfil · W Sistema · X MENSAGEM · X Sistema |
| SIS-CFG-03 | Configurar estratégia | EE | 3 | 4 | E Sistema · W Sistema · X MENSAGEM · X Sistema |
| SIS-CFG-04 | Configurar ferramenta de demandas | EE | 3 | 4 | E FerramentaDemandas · R Sistema · X FerramentaDemandas · X MENSAGEM |
| SIS-CFG-01 | Configurar repositórios | EE | 10 | 7 | E Conta · E GitHub · E Sistema · R EventoAuditoria · W Sistema · X MENSAGEM · X Sistema |
