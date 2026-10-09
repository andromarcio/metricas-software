# 7. Glossário

> MFO — Medição Funcional Objetiva · Versão 1.0

| Termo | Definição |
|---|---|
| **Agente** | Quem produziu o modelo: pessoa, IA (identificada por nome e versão) ou combinação. Faz parte do rótulo. |
| **Alterado** | Movimento presente em dois modelos consecutivos cujos atributos ou manipulação mudaram (RC-03). |
| **Armazenamento persistente** | Qualquer meio em que dados sobrevivem ao término de um processo e podem ser lidos por outro: banco de dados, arquivo, memória não volátil. |
| **Chave de movimento** | Tripla (processo, tipo, entidade) que identifica um movimento. Cada chave vale 1 PFO. |
| **Concordância (índice de)** | Razão entre chaves comuns e chaves totais de dois modelos do mesmo software (seção 4.4). |
| **D (suplemento de derivação)** | Número de processos cujas saídas ou gravações contêm atributo ausente das entradas e leituras (RC-05). Reportado à parte. |
| **Densidade** | PFO dividido pelo número de processos. |
| **DISPARO** | Entidade reservada para o movimento E de um disparador sem atributos de entidade. |
| **Disparador** | Evento percebido por um usuário funcional que inicia um processo, com o usuário funcional que o gera. |
| **Entidade** | Grupo nomeado de atributos que descreve uma única coisa de interesse, persistida ou trocada como unidade (RI-03). |
| **Entrada (E)** | Movimento de uma entidade de um usuário funcional para o processo (RI-05). |
| **Escopo** | Conjunto de funcionalidades incluídas na medição (RI-01). |
| **Evidência** | Referência `FONTE:localizador` que permite confirmar um elemento do modelo no artefato (RI-11). |
| **Fonte** | Artefato declarado no modelo, com identificador e versão, de onde vêm as evidências. |
| **Fronteira** | Linha conceitual entre o software medido e seus usuários funcionais (RI-01). |
| **Grau de evidência** | Porcentagem de movimentos não inferidos. Faz parte do rótulo. |
| **Gravação (W)** | Movimento de uma entidade do processo para o armazenamento persistente: criar, alterar ou excluir (RI-08). |
| **Inferido** | Elemento incluído no modelo sem evidência localizável, com justificativa (RI-11 b). |
| **Leitura (R)** | Movimento de uma entidade do armazenamento persistente para o processo (RI-07). |
| **MENSAGEM** | Entidade reservada para a única X por processo que representa mensagens de erro, validação, sucesso e estado. |
| **MFC — Modelo Funcional Canônico** | Documento JSON que descreve usuários funcionais, entidades, processos e movimentos com evidências. Insumo único da contagem. |
| **MFO — Medição Funcional Objetiva** | O método descrito nesta especificação. |
| **Movimento** | Deslocamento de uma entidade em um processo; tipos E, X, R, W. |
| **Nível de medição** | Origem do modelo: R (requisitos), C (código ou sistema) ou RC (conciliado). |
| **NP, NE** | Número de processos e número de entidades declaradas. |
| **Perfil funcional** | Conjunto de indicadores derivados do modelo (seção 5.2). |
| **PFO — Ponto de Função Objetivo** | Unidade de tamanho da MFO. Um PFO por chave de movimento. |
| **Processo** | Menor unidade de funcionalidade com disparador, efeito e autonomia (RI-04). |
| **Rótulo** | Identificação obrigatória de um resultado (RC-06). |
| **Saída (X)** | Movimento de uma entidade do processo para um usuário funcional (RI-06). |
| **Usuário funcional (UF)** | Origem ou destino de dados através da fronteira: pessoa, sistema, dispositivo ou relógio (RI-02). |
| **Validação (V-xx)** | Verificação que o modelo deve satisfazer para ser contado (seção 3.2). |
