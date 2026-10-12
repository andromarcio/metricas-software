<!-- Gerado por scripts/gera-docs.py a partir de PFC/exemplos/aval/pfc-vs-pf-aval-5.0.0.md. Não edite: edite a fonte e gere de novo. -->
# PFC (extração mecânica) × PF (memória de cálculo dos N3) — Aval 5.0.0

> PFC: `extrair_n3.py` sobre siesa-doc@49265a9 (piso mecânico, sem revisão). PF: soma da tabela `## Métricas de tamanho` de cada N3, como registrada pela equipe.

## Por domínio

| Domínio | Processos | PFC | PF | PFC/PF |
|---|---|---|---|---|
| ADM | 24 | 171 | 117 | 1.46 |
| AGT | 12 | 59 | 68 | 0.87 |
| DEM | 6 | 40 | 31 | 1.29 |
| EST | 21 | 149 | 106 | 1.41 |
| OPE | 8 | 46 | 31 | 1.48 |
| SIS | 14 | 77 | 69 | 1.12 |
| **Total** | **85** | **542** | **422** | **1.28** |

## Por feature set

| Feature set | Processos | PFC | PF | PFC/PF |
|---|---|---|---|---|
| ADM-AUD | 1 | 6 | 4 | 1.50 |
| ADM-CTA | 5 | 38 | 29 | 1.31 |
| ADM-INT | 2 | 14 | 11 | 1.27 |
| ADM-MOD | 1 | 7 | 3 | 2.33 |
| ADM-ORG | 3 | 20 | 16 | 1.25 |
| ADM-PER | 6 | 42 | 20 | 2.10 |
| ADM-USR | 6 | 44 | 34 | 1.29 |
| AGT-EXE | 12 | 59 | 68 | 0.87 |
| DEM-INT | 3 | 24 | 16 | 1.50 |
| DEM-PAI | 3 | 16 | 15 | 1.07 |
| EST-ACO | 11 | 66 | 59 | 1.12 |
| EST-APR | 10 | 83 | 47 | 1.77 |
| OPE-GCO | 8 | 46 | 31 | 1.48 |
| SIS-ACE | 2 | 15 | 10 | 1.50 |
| SIS-CAD | 8 | 37 | 36 | 1.03 |
| SIS-CFG | 4 | 25 | 23 | 1.09 |
| **Total** | **85** | **542** | **422** | **1.28** |

## Por processo

| Processo | Nome | Tipo APF | PF | PFC | Chaves contadas |
|---|---|---|---|---|---|
| ADM-AUD-01 | Pesquisar auditoria | CE | 4 | 6 | E EventoAuditoria · R EventoAuditoria · R Usuario · X EventoAuditoria · X Usuario · D VALIDATION_ERROR |
| ADM-CTA-02 | Autenticar usuário | EE | 6 | 10 | E Identidade Google · E Pessoa · R Conta · R EventoAuditoria · R Identidade Google · R Perfil · W EventoAuditoria · W Usuario · X Usuario · D RECUSA |
| ADM-CTA-01 | Criar conta | EE | 6 | 9 | E Identidade Google · E Pessoa · R EventoAuditoria · R Identidade Google · W Conta · W EventoAuditoria · W Usuario · X Pessoa · D VALIDATION_ERROR |
| ADM-CTA-03 | Recuperar senha | EE | 3 | 6 | E Pessoa · R EventoAuditoria · W EventoAuditoria · W Usuario · X Usuario · D VALIDATION_ERROR |
| ADM-CTA-03.2 | Redefinir a senha | EE | 4 | 4 | E Usuario · R EventoAuditoria · W Usuario · X Usuario |
| ADM-CTA-04 | Trocar de conta | EE | 10 | 9 | E Pessoa · R Conta · R Usuario · W Pessoa · X Conta · X Pessoa · X Usuario · D RESOURCE_NOT_FOUND · D VALIDATION_ERROR |
| ADM-INT-01 | Configurar conexão GitHub | EE | 8 | 10 | E GitHub · R Conta · R EventoAuditoria · R GitHub · W Conta · W EventoAuditoria · X Conta · X GitHub · D CONEXAO_GITHUB_INSTALL_FAILED · D CONEXAO_GITHUB_INACTIVE |
| ADM-INT-01.2 | Processar revogação (webhook do GitHub) | EE | 3 | 4 | E GitHub · R EventoAuditoria · W Conta · X GitHub |
| ADM-MOD-01 | Configurar modelo por etapa | EE | 3 | 7 | E ModeloEtapa · R Conta · W Conta · X Conta · X ModeloEtapa · D MODELO_IA_NAO_SUPORTADO · D ETAPA_DESCONHECIDA |
| ADM-ORG-03 | Alterar organização | EE | 3 | 5 | E Conta · W Conta · X Conta · D CONTA_IDENTIFICADOR_CONFLICT · D VALIDATION_ERROR |
| ADM-ORG-01 | Criar organização | EE | 6 | 8 | E Conta · R Perfil · W Conta · W Perfil · W Usuario · X Conta · D CONTA_IDENTIFICADOR_CONFLICT · D VALIDATION_ERROR |
| ADM-ORG-02 | Visualizar organização | SE | 7 | 7 | E DISPARO · R Conta · R Perfil · R Sistema · R Usuario · X Conta · D RECUSA |
| ADM-PER-05 | Ativar funcionalidade | EE | 3 | 6 | E Funcionalidade · R EventoAuditoria · W EventoAuditoria · W Funcionalidade · X Funcionalidade · D RESOURCE_NOT_FOUND |
| ADM-PER-02 | Conceder funcionalidade | EE | 3 | 10 | E PerfilFuncionalidade · R EventoAuditoria · R Funcionalidade · R Perfil · W EventoAuditoria · W Funcionalidade · W Perfil · X Funcionalidade · D PERFIL_ADMIN_IMMUTABLE · D RESOURCE_NOT_FOUND |
| ADM-PER-01 | Criar perfil | EE | 4 | 6 | E Perfil · R EventoAuditoria · W EventoAuditoria · W Perfil · X Perfil · D PERFIL_NAME_CONFLICT |
| ADM-PER-04 | Desativar funcionalidade | EE | 3 | 6 | E Funcionalidade · R EventoAuditoria · W EventoAuditoria · W Funcionalidade · X Funcionalidade · D RESOURCE_NOT_FOUND |
| ADM-PER-03 | Revogar funcionalidade | EE | 3 | 9 | E PerfilFuncionalidade · R EventoAuditoria · R Funcionalidade · R Perfil · W EventoAuditoria · W Funcionalidade · X Funcionalidade · D PERFIL_ADMIN_IMMUTABLE · D RESOURCE_NOT_FOUND |
| ADM-PER-06 | Visualizar matriz de perfis e funcionalidades | CE | 4 | 5 | E Funcionalidade · R Funcionalidade · R Perfil · X Funcionalidade · D RESOURCE_NOT_FOUND |
| ADM-USR-06 | Aceitar convite | EE | 10 | 12 | E Pessoa · R Conta · R Convite · R Perfil · R Usuario · W Convite · W Usuario · X Conta · X Convite · D CONVITE_INVALID · D RESOURCE_NOT_FOUND · D VALIDATION_ERROR |
| ADM-USR-03 | Alterar perfil do usuário | EE | 4 | 7 | E Usuario · R Perfil · W Usuario · X Perfil · X Usuario · D USUARIO_LAST_ADMIN · D RESOURCE_NOT_FOUND |
| ADM-USR-02 | Convidar usuário | EE | 9 | 9 | E Convite · R Perfil · W Convite · W Usuario · X Convite · X Perfil · D CONVITE_EMAIL_ACTIVE · D RESOURCE_NOT_FOUND · D VALIDATION_ERROR |
| ADM-USR-04 | Desativar usuário | EE | 3 | 5 | E Usuario · W Usuario · X Usuario · D USUARIO_LAST_ADMIN · D RESOURCE_NOT_FOUND |
| ADM-USR-01 | Pesquisar usuários | SE | 5 | 6 | E Usuario · R Perfil · R Usuario · X Perfil · X Usuario · D VALIDATION_ERROR |
| ADM-USR-05 | Reativar usuário | EE | 3 | 5 | E Usuario · W Usuario · X Usuario · D USUARIO_NOT_INACTIVE · D RESOURCE_NOT_FOUND |
| AGT-EXE-02 | Detalhar requisitos | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-07 | Executar testes do sistema | EE | 6 | 6 | E DISPARO · E GitHub · R Demanda · W EsteiraExecucao · W ExecucaoAgente · D RECUSA |
| AGT-EXE-10 | Gerar análise de impacto | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R ExecucaoAgente · W EsteiraExecucao |
| AGT-EXE-04 | Gerar casos de teste | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-06 | Gerar código | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-03 | Gerar modelo de dados | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-05 | Gerar plano de implementação | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · R EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-09 | Gerar preparação do sistema | EE | 4 | 5 | E ExecucaoAgente · R Conta · R Sistema · W ExecucaoAgente · W Sistema |
| AGT-EXE-09.2 | Materializar preparação aprovada (agente) | EE | 6 | 2 | E ExecucaoAgente · X ExecucaoAgente |
| AGT-EXE-11 | Gerar protótipo | EE | 6 | 7 | E DISPARO · E GitHub · R Demanda · R ExecucaoAgente · W EsteiraExecucao · X EtapaExecucao · D RESOURCE_NOT_FOUND |
| AGT-EXE-08 | Preparar implantação | EE | 6 | 5 | E DISPARO · E GitHub · R Demanda · W EsteiraExecucao · W ExecucaoAgente |
| AGT-EXE-01 | Processar triagem | EE | 4 | 4 | E DISPARO · E GitHub · R Demanda · W ExecucaoAgente |
| DEM-INT-02 | Iniciar esteira | EE | 6 | 9 | E Demanda · R EventoAuditoria · R Sistema · W Demanda · W EsteiraExecucao · X Demanda · D ESTEIRA_ALREADY_RUNNING · D SISTEMA_REPOSITORIES_MISSING · D RESOURCE_NOT_FOUND |
| DEM-INT-03 | Iniciar execução do acervo | EE | 6 | 9 | E Demanda · R Sistema · W Demanda · W EsteiraExecucao · X Demanda · D DEMANDA_FEATURE_ALREADY_RUNNING · D DEMANDA_FEATURE_NOT_APPROVED · D VALIDATION_ERROR · D RESOURCE_NOT_FOUND |
| DEM-INT-01 | Registrar demanda | EE | 4 | 6 | E Demanda · R Sistema · W Demanda · W EventoAuditoria · X Demanda · D VALIDATION_ERROR |
| DEM-PAI-02 | Cancelar demanda | EE | 6 | 9 | E Demanda · R EsteiraExecucao · R EventoAuditoria · R ExecucaoAgente · W Demanda · X Demanda · D DEMANDA_NOT_CANCELABLE · D VALIDATION_ERROR · D RESOURCE_NOT_FOUND |
| DEM-PAI-01 | Pesquisar demandas | SE | 5 | 5 | E Demanda · R EsteiraExecucao · R Perfil · X Demanda · D RECUSA |
| DEM-PAI-01.2 | Consultar resumo do painel (contadores) | CE | 4 | 2 | E Demanda · X Demanda |
| EST-ACO-01 | Acompanhar esteira | SE | 7 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EsteiraExecucao · D RESOURCE_NOT_FOUND |
| EST-ACO-10 | Consultar consumo de IA | SE | 5 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X ExecucaoAgente · D RESOURCE_NOT_FOUND |
| EST-ACO-09 | Consultar saúde das esteiras | SE | 5 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EsteiraExecucao · D RESOURCE_NOT_FOUND |
| EST-ACO-08 | Visualizar análise de impacto | CE | 6 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X RegistroImpacto · D RESOURCE_NOT_FOUND |
| EST-ACO-04 | Visualizar casos de teste | CE | 6 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EtapaExecucao · D RESOURCE_NOT_FOUND |
| EST-ACO-05 | Visualizar codificação | CE | 6 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EtapaExecucao · D RESOURCE_NOT_FOUND |
| EST-ACO-07 | Visualizar implantação | CE | 4 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EtapaExecucao · D RESOURCE_NOT_FOUND |
| EST-ACO-03 | Visualizar modelo de dados | CE | 6 | 7 | E DISPARO · R Demanda · R EsteiraExecucao · R EventoAgente · R ExecucaoAgente · X EtapaExecucao · D RESOURCE_NOT_FOUND |
| EST-ACO-11 | Visualizar protótipo | CE | 4 | 5 | E DISPARO · E GitHub · R EtapaExecucao · X EtapaExecucao · D RESOURCE_NOT_FOUND |
| EST-ACO-02 | Visualizar requisitos | CE | 6 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EtapaExecucao · D RESOURCE_NOT_FOUND |
| EST-ACO-06 | Visualizar testes do sistema | CE | 4 | 6 | E DISPARO · R Demanda · R EsteiraExecucao · R ExecucaoAgente · X EtapaExecucao · D RESOURCE_NOT_FOUND |
| EST-APR-09 | Aprovar escopo de impacto | EE | 4 | 8 | E PendenciaAprovacao · R EventoAuditoria · R Sistema · W EsteiraExecucao · X PendenciaAprovacao · D ETAPA_NOT_PENDING · D ETAPA_APPROVER_MISMATCH · D RESOURCE_VERSION_CONFLICT |
| EST-APR-01 | Aprovar etapa | EE | 6 | 9 | E PendenciaAprovacao · R EventoAuditoria · R Perfil · R Sistema · W EsteiraExecucao · X PendenciaAprovacao · D ETAPA_NOT_PENDING · D ETAPA_APPROVER_MISMATCH · D RESOURCE_VERSION_CONFLICT |
| EST-APR-03 | Aprovar feature | EE | 4 | 6 | E PendenciaAprovacao · R EventoAuditoria · W EsteiraExecucao · X PendenciaAprovacao · D ETAPA_NOT_PENDING · D RESOURCE_VERSION_CONFLICT |
| EST-APR-04 | Aprovar história | EE | 4 | 8 | E PendenciaAprovacao · R EventoAuditoria · R Sistema · W EsteiraExecucao · X PendenciaAprovacao · D ETAPA_FEATURES_NOT_APPROVED · D ETAPA_NOT_PENDING · D ETAPA_APPROVER_MISMATCH |
| EST-APR-07 | Autorizar implantação | EE | 6 | 11 | E GitHub · E PendenciaAprovacao · R EsteiraExecucao · R EventoAuditoria · R Perfil · R Sistema · X PendenciaAprovacao · D VALIDATION_ERROR · D ETAPA_NOT_PENDING · D ETAPA_APPROVER_MISMATCH · D RESOURCE_VERSION_CONFLICT |
| EST-APR-06 | Homologar entrega | EE | 4 | 8 | E PendenciaAprovacao · R EventoAuditoria · R Sistema · W EsteiraExecucao · X PendenciaAprovacao · D ETAPA_NOT_PENDING · D ETAPA_APPROVER_MISMATCH · D RESOURCE_VERSION_CONFLICT |
| EST-APR-08 | Listar pendências | SE | 5 | 6 | E PendenciaAprovacao · R Demanda · R EsteiraExecucao · R Perfil · X PendenciaAprovacao · D RECUSA |
| EST-APR-05 | Reprovar testes do sistema | EE | 6 | 10 | E PendenciaAprovacao · R EsteiraExecucao · R EventoAuditoria · R Perfil · R Sistema · X PendenciaAprovacao · D VALIDATION_ERROR · D ETAPA_NOT_PENDING · D ETAPA_APPROVER_MISMATCH · D RESOURCE_VERSION_CONFLICT |
| EST-APR-10 | Responder esclarecimentos | EE | 4 | 10 | E PendenciaAprovacao · R EsteiraExecucao · R EventoAuditoria · R ExecucaoAgente · W ExecucaoAgente · X PendenciaAprovacao · D ETAPA_SEM_ESCLARECIMENTOS · D ETAPA_NOT_PENDING · D VALIDATION_ERROR · D RESOURCE_VERSION_CONFLICT |
| EST-APR-02 | Solicitar ajustes | EE | 4 | 7 | E PendenciaAprovacao · R EventoAuditoria · R ExecucaoAgente · W EsteiraExecucao · X PendenciaAprovacao · D ETAPA_NOT_PENDING · D RESOURCE_VERSION_CONFLICT |
| OPE-GCO-02 | Criar organização | EE | 6 | 7 | E Conta · R Convite · R EventoAuditoria · R Usuario · W Conta · X Conta · D CONTA_IDENTIFICADOR_CONFLICT |
| OPE-GCO-06 | Definir limites de consumo | EE | 3 | 6 | E Conta · R EventoAuditoria · W Conta · X Conta · D VALIDATION_ERROR · D RESOURCE_NOT_FOUND |
| OPE-GCO-03 | Editar organização | EE | 3 | 6 | E Conta · R EventoAuditoria · W Conta · X Conta · D CONTA_IDENTIFICADOR_CONFLICT · D RESOURCE_NOT_FOUND |
| OPE-GCO-07 | Entrar como | EE | 3 | 5 | E Conta · R EventoAuditoria · W Conta · X Conta · D RESOURCE_NOT_FOUND |
| OPE-GCO-01 | Listar contas | SE | 5 | 8 | E Conta · R Conta · R EsteiraExecucao · R ExecucaoAgente · R Sistema · R Usuario · X Conta · D RECUSA |
| OPE-GCO-01.2 | Consultar resumo da plataforma | CE | 4 | 2 | E Conta · X Conta |
| OPE-GCO-05 | Reativar conta | EE | 3 | 6 | E Conta · R EventoAuditoria · W Conta · X Conta · D CONTA_NOT_SUSPENDED · D RESOURCE_NOT_FOUND |
| OPE-GCO-04 | Suspender conta | EE | 4 | 6 | E Conta · R EventoAuditoria · W Conta · X Conta · D CONTA_NOT_SUSPENDABLE · D RESOURCE_NOT_FOUND |
| SIS-ACE-01 | Visualizar catálogo de features | SE | 5 | 8 | E Sistema · R Demanda · R EsteiraExecucao · R Sistema · X Sistema · D SISTEMA_REPOSITORIES_MISSING · D GITHUB_APP_UNAVAILABLE · D RESOURCE_NOT_FOUND |
| SIS-ACE-02 | Visualizar mapa de features | SE | 5 | 7 | E DISPARO · R EsteiraExecucao · R Sistema · X Sistema · D SISTEMA_REPOSITORIES_MISSING · D GITHUB_APP_UNAVAILABLE · D RESOURCE_NOT_FOUND |
| SIS-CAD-04 | Alterar sistema | EE | 4 | 6 | E Sistema · R EventoAuditoria · W Sistema · X Sistema · D FIELD_IMMUTABLE · D RESOURCE_NOT_FOUND |
| SIS-CAD-01 | Cadastrar sistema | EE | 4 | 5 | E Sistema · R EventoAuditoria · W Sistema · X Sistema · D SISTEMA_IDENTIFIER_CONFLICT |
| SIS-CAD-02 | Definir sistema ativo | CE | 4 | 3 | E Sistema · R EsteiraExecucao · X Sistema |
| SIS-CAD-05 | Preparar sistema | EE | 4 | 10 | E Sistema · R Conta · R ExecucaoAgente · R Usuario · W Sistema · X Sistema · D CONEXAO_GITHUB_REPO_PERMISSION_MISSING · D CONEXAO_GITHUB_INACTIVE · D RESOURCE_VERSION_CONFLICT · D VALIDATION_ERROR |
| SIS-CAD-05.2 | Acompanhar preparação e proposta | CE | 4 | 2 | E Sistema · X Sistema |
| SIS-CAD-05.3 | Aprovar proposta de preparação | EE | 4 | 2 | E Sistema · X Sistema |
| SIS-CAD-05.4 | Solicitar ajustes na proposta | EE | 3 | 2 | E Sistema · X Sistema |
| SIS-CAD-03 | Transferir sistema | EE | 9 | 7 | E Sistema · R Conta · R Usuario · W Sistema · X Sistema · D VALIDATION_ERROR · D RESOURCE_NOT_FOUND |
| SIS-CFG-02 | Configurar aprovadores | EE | 7 | 6 | E Sistema · R EventoAuditoria · R Perfil · W Sistema · X Sistema · D VALIDATION_ERROR |
| SIS-CFG-03 | Configurar estratégia | EE | 3 | 5 | E Sistema · W Sistema · X Sistema · D VALIDATION_ERROR · D RESOURCE_NOT_FOUND |
| SIS-CFG-04 | Configurar ferramenta de demandas | EE | 3 | 5 | E FerramentaDemandas · R Sistema · X FerramentaDemandas · D VALIDATION_ERROR · D RESOURCE_NOT_FOUND |
| SIS-CFG-01 | Configurar repositórios | EE | 10 | 9 | E Conta · E GitHub · E Sistema · R EventoAuditoria · W Sistema · X Sistema · D REPOSITORIO_UNREACHABLE · D REPOSITORIO_DUPLICATE · D CONEXAO_GITHUB_INACTIVE |
