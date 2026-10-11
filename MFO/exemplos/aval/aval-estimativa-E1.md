# Estimativa MFO — Aval (siesa-doc) 5.0.0 (estimativa E1)

**Rótulo:** ≈ 616 PFO (estimativa E1, 433 a 873) · MFO 1.0 · nível R · evidência 0% · agente: ferramenta (mfo.py estimar 1.0); sem revisão humana · escopo: Aval (siesa-doc) 5.0.0 (estimativa E1), 85 features N3 como itens de backlog, sem ler o conteúdo dos N3

| Indicador | Valor |
|---|---|
| Nível da estimativa | E1 |
| Processos estimados | 85 |
| PFO do modelo (perfis típicos) | 304 |
| Fator de calibração | 2,02 |
| PFO calibrado | **616** |
| Intervalo | 433 a 873 PFO |
| Base | perfis de 16 processos medidos (biblioteca-v1.mfc.json, adm-usr-revisado.mfc.json) |
| Medido (para conferência) | 542 PFO · erro relativo 14% |

## Itens

| ID | Processo | Tipo | Entidades | PFO |
|---|---|---|---|---|
| ADM-AUD-01 | Pesquisar auditoria | consultar | EventoAuditoria | 3 |
| ADM-CTA-02 | Autenticar usuário | outro | Identidade Google | 4 |
| ADM-CTA-01 | Criar conta | criar | Identidade Google | 4 |
| ADM-CTA-03 | Recuperar senha | processar | Pessoa | 3 |
| ADM-CTA-03.2 | Redefinir a senha | alterar | Usuario | 4 |
| ADM-CTA-04 | Trocar de conta | alterar | Pessoa | 4 |
| ADM-INT-01 | Configurar conexão GitHub | alterar | GitHub | 4 |
| ADM-INT-01.2 | Processar revogação (webhook do GitHub) | processar | GitHub | 3 |
| ADM-MOD-01 | Configurar modelo por etapa | alterar | ModeloEtapa | 4 |
| ADM-ORG-03 | Alterar organização | alterar | Conta | 4 |
| ADM-ORG-01 | Criar organização | criar | Conta | 4 |
| ADM-ORG-02 | Visualizar organização | consultar | Conta | 3 |
| ADM-PER-05 | Ativar funcionalidade | estado | Funcionalidade | 4 |
| ADM-PER-02 | Conceder funcionalidade | alterar | PerfilFuncionalidade | 4 |
| ADM-PER-01 | Criar perfil | criar | Perfil | 4 |
| ADM-PER-04 | Desativar funcionalidade | estado | Funcionalidade | 4 |
| ADM-PER-03 | Revogar funcionalidade | alterar | PerfilFuncionalidade | 4 |
| ADM-PER-06 | Visualizar matriz de perfis e funcionalidades | consultar | Funcionalidade | 3 |
| ADM-USR-06 | Aceitar convite | estado | Pessoa | 4 |
| ADM-USR-03 | Alterar perfil do usuário | alterar | Usuario | 4 |
| ADM-USR-02 | Convidar usuário | criar | Convite | 4 |
| ADM-USR-04 | Desativar usuário | estado | Usuario | 4 |
| ADM-USR-01 | Pesquisar usuários | consultar | Usuario | 3 |
| ADM-USR-05 | Reativar usuário | estado | Usuario | 4 |
| AGT-EXE-02 | Detalhar requisitos | consultar | GitHub | 3 |
| AGT-EXE-07 | Executar testes do sistema | processar | GitHub | 3 |
| AGT-EXE-10 | Gerar análise de impacto | processar | GitHub | 3 |
| AGT-EXE-04 | Gerar casos de teste | processar | GitHub | 3 |
| AGT-EXE-06 | Gerar código | processar | GitHub | 3 |
| AGT-EXE-03 | Gerar modelo de dados | processar | GitHub | 3 |
| AGT-EXE-05 | Gerar plano de implementação | processar | GitHub | 3 |
| AGT-EXE-09 | Gerar preparação do sistema | processar | ExecucaoAgente | 3 |
| AGT-EXE-09.2 | Materializar preparação aprovada (agente) | processar | ExecucaoAgente | 3 |
| AGT-EXE-11 | Gerar protótipo | processar | GitHub | 3 |
| AGT-EXE-08 | Preparar implantação | alterar | GitHub | 4 |
| AGT-EXE-01 | Processar triagem | processar | GitHub | 3 |
| DEM-INT-02 | Iniciar esteira | estado | Demanda | 4 |
| DEM-INT-03 | Iniciar execução do acervo | estado | Demanda | 4 |
| DEM-INT-01 | Registrar demanda | criar | Demanda | 4 |
| DEM-PAI-02 | Cancelar demanda | estado | Demanda | 4 |
| DEM-PAI-01 | Pesquisar demandas | consultar | Demanda | 3 |
| DEM-PAI-01.2 | Consultar resumo do painel (contadores) | consultar | Demanda | 3 |
| EST-ACO-01 | Acompanhar esteira | consultar | Demanda | 3 |
| EST-ACO-10 | Consultar consumo de IA | consultar | Demanda | 3 |
| EST-ACO-09 | Consultar saúde das esteiras | consultar | Demanda | 3 |
| EST-ACO-08 | Visualizar análise de impacto | consultar | Demanda | 3 |
| EST-ACO-04 | Visualizar casos de teste | consultar | Demanda | 3 |
| EST-ACO-05 | Visualizar codificação | consultar | Demanda | 3 |
| EST-ACO-07 | Visualizar implantação | consultar | Demanda | 3 |
| EST-ACO-03 | Visualizar modelo de dados | consultar | Demanda | 3 |
| EST-ACO-11 | Visualizar protótipo | consultar | GitHub | 3 |
| EST-ACO-02 | Visualizar requisitos | consultar | Demanda | 3 |
| EST-ACO-06 | Visualizar testes do sistema | consultar | Demanda | 3 |
| EST-APR-09 | Aprovar escopo de impacto | estado | PendenciaAprovacao | 4 |
| EST-APR-01 | Aprovar etapa | estado | PendenciaAprovacao | 4 |
| EST-APR-03 | Aprovar feature | estado | PendenciaAprovacao | 4 |
| EST-APR-04 | Aprovar história | estado | PendenciaAprovacao | 4 |
| EST-APR-07 | Autorizar implantação | estado | GitHub | 4 |
| EST-APR-06 | Homologar entrega | estado | PendenciaAprovacao | 4 |
| EST-APR-08 | Listar pendências | consultar | PendenciaAprovacao | 3 |
| EST-APR-05 | Reprovar testes do sistema | estado | PendenciaAprovacao | 4 |
| EST-APR-10 | Responder esclarecimentos | estado | PendenciaAprovacao | 4 |
| EST-APR-02 | Solicitar ajustes | criar | PendenciaAprovacao | 4 |
| OPE-GCO-02 | Criar organização | criar | Conta | 4 |
| OPE-GCO-06 | Definir limites de consumo | alterar | Conta | 4 |
| OPE-GCO-03 | Editar organização | alterar | Conta | 4 |
| OPE-GCO-07 | Entrar como | outro | Conta | 4 |
| OPE-GCO-01 | Listar contas | consultar | Conta | 3 |
| OPE-GCO-01.2 | Consultar resumo da plataforma | consultar | Conta | 3 |
| OPE-GCO-05 | Reativar conta | estado | Conta | 4 |
| OPE-GCO-04 | Suspender conta | estado | Conta | 4 |
| SIS-ACE-01 | Visualizar catálogo de features | consultar | Sistema | 3 |
| SIS-ACE-02 | Visualizar mapa de features | consultar | EsteiraExecucao | 3 |
| SIS-CAD-04 | Alterar sistema | alterar | Sistema | 4 |
| SIS-CAD-01 | Cadastrar sistema | criar | Sistema | 4 |
| SIS-CAD-02 | Definir sistema ativo | alterar | Sistema | 4 |
| SIS-CAD-05 | Preparar sistema | alterar | Sistema | 4 |
| SIS-CAD-05.2 | Acompanhar preparação e proposta | consultar | Sistema | 3 |
| SIS-CAD-05.3 | Aprovar proposta de preparação | estado | Sistema | 4 |
| SIS-CAD-05.4 | Solicitar ajustes na proposta | criar | Sistema | 4 |
| SIS-CAD-03 | Transferir sistema | alterar | Sistema | 4 |
| SIS-CFG-02 | Configurar aprovadores | alterar | Sistema | 4 |
| SIS-CFG-03 | Configurar estratégia | alterar | Sistema | 4 |
| SIS-CFG-04 | Configurar ferramenta de demandas | alterar | FerramentaDemandas | 4 |
| SIS-CFG-01 | Configurar repositórios | alterar | Conta | 4 |

Todos os movimentos e desfechos estão marcados como inferidos (evidência 0%); a extração substitui cada um por evidência conforme os artefatos surgem.

