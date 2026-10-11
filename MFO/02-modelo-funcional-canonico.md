# 2. Modelo Funcional Canônico (MFC)

> MFO — Medição Funcional Objetiva · Versão 1.0

O Modelo Funcional Canônico é a representação, em formato estruturado, do que o software
faz para seus usuários funcionais. É o único insumo da contagem: tudo que não está no
modelo não é medido, e tudo que está no modelo deve ter evidência. Este capítulo define
os conceitos e as **regras de identificação (RI)** que dizem o que entra no modelo.

## 2.1 Visão geral

```
                 fronteira
   usuários   ┊            software medido            ┊
  funcionais  ┊  ┌───────────────────────────────┐    ┊   armazenamento
              ┊  │                               │    ┊    persistente
  pessoa   ──E──▶│         P R O C E S S O       │──W──▶  ┌──────────┐
  sistema  ◀──X──│  disparado por um evento,     │◀──R──  │ entidades│
  dispositivo ┊  │  move entidades, termina em   │    ┊   └──────────┘
  relógio     ┊  │  estado consistente           │    ┊
              ┊  └───────────────────────────────┘    ┊
```

Um software é um conjunto de **processos**. Cada processo é disparado por um **usuário
funcional**, movimenta **entidades** por meio de **movimentos** (E, X, R, W), devolve um
ou mais **desfechos** e termina. O tamanho é o número de movimentos mais o número de
desfechos além do principal.

## 2.2 Fronteira, escopo e propósito

> **RI-01 — Fronteira e escopo**
>
> a) O propósito da medição deve ser declarado (ex.: contratar, comparar, acompanhar
>    evolução, remunerar manutenção).
>
> b) O escopo lista o que está sendo medido: um software, um módulo, um conjunto de
>    requisitos ou uma mudança. O escopo deve estar inteiramente em uma única camada
>    (aplicação, serviço, componente), nunca misturar camadas.
>
> c) A fronteira separa o software medido de seus usuários funcionais. O armazenamento
>    persistente que o software lê ou grava diretamente fica **dentro** da fronteira para
>    fins de movimentos R e W, mesmo quando é mantido por outra aplicação.
>
> d) Software fora do escopo que troque mensagens ou chamadas com o software medido é
>    usuário funcional (E/X). Software fora do escopo cujos dados são acessados diretamente
>    em banco ou arquivo é armazenamento (R/W). O critério é o mecanismo de acesso descrito
>    no artefato, não a propriedade dos dados.

## 2.3 Usuários funcionais

> **RI-02 — Usuário funcional**
>
> Um usuário funcional é qualquer origem ou destino de dados que atravessam a fronteira.
> Há quatro tipos, e o tipo é registrado no modelo:
>
> | Tipo | Exemplos | Pista no artefato |
> |---|---|---|
> | `pessoa` | operador, cliente, administrador | tela, formulário, comando, app |
> | `sistema` | outra aplicação, API externa, fila, gateway, serviço de e-mail | chamada HTTP/RPC, mensagem, webhook, arquivo trocado |
> | `dispositivo` | sensor, atuador, leitor de cartão, impressora fiscal | sinal, porta, protocolo de dispositivo |
> | `relogio` | agendador, cron, temporizador | job agendado, tarefa periódica, timeout |
>
> Papéis diferentes de pessoa (perfis) só são usuários funcionais distintos quando
> disparam processos distintos. Se o mesmo processo pode ser disparado por vários perfis,
> registra-se um único usuário funcional para ele.

## 2.4 Entidades

Uma **entidade** é um grupo nomeado de atributos que descreve uma única coisa de interesse
para o usuário funcional e que o software persiste ou troca como unidade.

> **RI-03 — Identificação de entidades**
>
> Um candidato é uma entidade quando responde **sim** aos testes T1, T2 e T3:
>
> - **T1 (nomeado como unidade):** o artefato o trata como unidade: tabela, coleção,
>   documento, classe de domínio, esquema, DTO, mensagem, registro de arquivo, seção de
>   formulário, ou substantivo de um requisito acompanhado de seus atributos.
> - **T2 (uma coisa):** seus atributos descrevem um único objeto de interesse. Se o
>   candidato reúne atributos de duas coisas com identidade própria (ex.: um payload com
>   pedido e cliente), são duas entidades.
> - **T3 (significado para o usuário):** o usuário funcional reconhece, informa ou consome
>   seus atributos. Dados que só existem por decisão de implementação não passam.
>
> Desempates fixados:
>
> a) Projeções do mesmo objeto (visões, DTOs, telas com subconjuntos de colunas da mesma
>    tabela) são a **mesma** entidade. A entidade é identificada pelo objeto descrito, não
>    pelo formato.
>
> b) Atributos pertencem à entidade que os persiste (coluna da tabela, campo do documento).
>    Em medição a partir de requisitos, pertencem à entidade que o requisito descreve. Uma
>    chave estrangeira é atributo da entidade que a contém; o nome ou descrição da entidade
>    referenciada é atributo da entidade referenciada.
>
> c) Tabelas de domínio (listas código/descrição), configuração técnica, sessões, tokens,
>    caches, índices, logs técnicos, filas internas e tabelas associativas sem atributos
>    próprios **não** são entidades.
>
> d) Parâmetros de negócio (tabela de tarifas, limites, calendário de feriados) **são**
>    entidades quando têm atributos além de código e descrição ou quando o usuário funcional
>    os mantém por um processo do escopo.
>
> e) Trilha de auditoria ou histórico exigido pelo usuário funcional (quem, quando, o quê,
>    consultável) é entidade. Log técnico não é.

### Entidade reservada

Um nome é reservado e não precisa ser declarado no modelo:

| Entidade | Tipo permitido | Quando usar |
|---|---|---|
| `DISPARO` | só E | Sinal de disparo que não carrega atributo de nenhuma entidade: tique de relógio, comando sem parâmetros, clique em "gerar relatório" sem filtros. |

Mensagens de erro, validação, sucesso e estado não são movimentos: são **desfechos**
(seção 2.7, RI-12). Se a mensagem carrega atributos de uma entidade ("limite excedido em
R$ 100,00", em que o valor foi calculado a partir da conta), há, além do desfecho, uma X
dessa entidade.

## 2.5 Processos

Um **processo** é a menor unidade de funcionalidade que tem disparador, efeito e autonomia.

> **RI-04 — Identificação de processos**
>
> Um candidato é um processo quando responde **sim** aos três testes:
>
> - **T1 (disparador):** existe um evento, percebido por um usuário funcional, que faz o
>   software começar a agir e que carrega pelo menos um movimento E (de uma entidade ou
>   de `DISPARO`).
> - **T2 (efeito):** ao terminar, o software gravou pelo menos uma entidade (W), enviou
>   pelo menos uma entidade a um usuário funcional (X) ou devolveu um desfecho (RI-12).
> - **T3 (autonomia):** ao terminar, o software aguarda um novo disparador e o efeito é
>   válido para o usuário funcional sem que outra etapa seja obrigatória.
>
> Identidade e desempates:
>
> a) Criar, alterar, excluir, consultar e mudar de estado (aprovar, cancelar, reabrir) são
>    processos **distintos**, porque são decisões distintas do usuário funcional.
>
> b) **Não** geram processos distintos: canal ou mídia (tela, API, arquivo, impressão),
>    formato de saída (tela, PDF, CSV), valores de filtro, ordenação, paginação,
>    navegação entre telas, confirmações ("OK", "tem certeza?"), subconjuntos opcionais de
>    atributos de entrada e caminhos alternativos de validação. Dois candidatos que diferem
>    apenas nesses aspectos são o mesmo processo.
>
> c) **Geram** processos distintos: decisões separadas no tempo (registrar hoje, aprovar
>    depois), responsabilidades separadas (administrador mantém parâmetros; operador usa) e
>    conjuntos de movimentos diferentes (a entrada em lote que também produz um relatório de
>    rejeitados é distinta da entrada em tela).
>
> d) Etapas de um assistente (wizard) ou abas que só têm efeito quando a última é
>    concluída pertencem a um único processo. Abas que gravam separadamente são processos
>    separados.
>
> e) Lista e detalhe são processos distintos quando o detalhe apresenta atributos ou
>    entidades que a lista não apresenta; caso contrário, são o mesmo processo.
>
> f) Comandos de controle (abrir menu, sair, limpar formulário, ordenar, paginar, exibir
>    ou ocultar seção) não são processos, pois não movimentam entidades.
>
> g) Um processo pode ter mais de um disparador (tela e API, por exemplo). Registra-se o
>    processo uma vez e lista-se cada disparador.

### Casos frequentes

| Situação | Decisão | Movimentos e desfechos típicos |
|---|---|---|
| Cadastro com validação de unicidade (CPF único) | 1 processo | E, R (verifica), W · desfecho: duplicidade |
| Alterar registro existente | 1 processo (a exibição prévia é o processo de consulta) | E, R, W · desfecho: não encontrado |
| Excluir registro, bloqueado se houver dependentes | 1 processo | E, R (dependentes), W · desfecho: bloqueado |
| Excluir sem nenhuma verificação | 1 processo | E, W |
| Lista com filtros | 1 processo | E (filtros), R, X · desfecho: "nenhum registro", quando a mensagem existe |
| Relatório sem parâmetros | 1 processo | E `DISPARO`, R…, X… · desfecho: "sem dados", quando a mensagem existe |
| Relatório em PDF e CSV | 1 processo | idem |
| Mesma função por tela e por API | 1 processo com dois disparadores | idem |
| Entrada on-line e carga em lote com relatório de rejeições | 2 processos | lote tem X ou W adicional |
| Assistente de 3 etapas que grava ao final | 1 processo | E (todas as entidades informadas), R, W · desfechos: cada recusa com código ou mensagem própria |
| Autenticar (login e senha) | 1 processo | E Usuário, R Usuário · desfecho: credenciais inválidas |
| Sair (logout) | não é processo | — |
| Trocar senha | 1 processo | E, R, W · desfecho: senha atual incorreta |
| Job diário que envia e-mails por serviço externo | 1 processo | E `DISPARO`, R…, X… (para o serviço), E (status devolvido, se usado), W (se registra envio) |
| Consumir mensagem de fila e gravar | 1 processo | E (entidade da mensagem), R…, W… · desfecho: rejeição com motivo, se houver |
| Webhook recebido | 1 processo | E, R, W · desfecho: rejeição com código |
| Sensor dispara alarme | 1 processo | E (leitura), R (limites), X (comando ao atuador) |
| Exportar dados para outro sistema por arquivo | 1 processo | E `DISPARO` ou filtros, R…, X… |
| Importar dados de outro sistema lidos direto do banco dele | 1 processo | E `DISPARO`, R (entidades do outro sistema), W… · desfecho: rejeição, se houver relatório de recusa |
| Página estática, ajuda, "sobre" | não é processo | — |

## 2.6 Movimentos

Um **movimento** desloca exatamente uma entidade entre um processo e um usuário funcional
(E, X) ou entre um processo e o armazenamento persistente (R, W). A **chave** de um
movimento é a tripla (processo, tipo, entidade).

> **RI-05 — Entrada (E)**
>
> a) Conta-se uma E por entidade cujos atributos entram no processo a partir de um usuário
>    funcional, incluindo o disparador.
>
> b) Se o disparador não carrega atributo de entidade, registra-se E `DISPARO`.
>
> c) A resposta de um sistema externo chamado pelo processo conta como E da entidade que a
>    resposta descreve, **somente** se o processo usa seus atributos (grava, decide ou
>    reenvia). Resposta ignorada ou mero código de retorno não conta.
>
> d) Obter a hora do sistema, ler parâmetros técnicos ou receber confirmações de controle
>    ("OK") não são E.

> **RI-06 — Saída (X)**
>
> a) Conta-se uma X por entidade cujos atributos são enviados a um usuário funcional
>    (tela, resposta de API, arquivo, mensagem, sinal a dispositivo). Uma saída que combina
>    atributos de três entidades gera três X.
>
> b) Chamada a sistema externo é X da(s) entidade(s) enviada(s). Chamada que não envia
>    atributo de entidade (só um sinal de controle) não é X.
>
> c) Mensagens de erro, validação, sucesso e estado não são X: são desfechos (RI-12).
>    Identificador gerado sem outros atributos (protocolo, token) também não é X.
>
> d) Rótulos, títulos, cabeçalhos, textos fixos, totais de página e elementos de navegação
>    não são atributos de entidade e não geram X.

> **RI-07 — Leitura (R)**
>
> a) Conta-se uma R por entidade da qual o processo obtém atributos do armazenamento
>    persistente para decidir, transformar ou enviar.
>
> b) Verificação de existência implícita em uma gravação (o "update" falha se o registro
>    não existe) não é R. Verificação que lê atributos para decidir (há empréstimo ativo?)
>    é R da entidade lida.
>
> c) Leitura de tabelas de domínio, configuração técnica, cache, sessão ou constantes não
>    é R.

> **RI-08 — Gravação (W)**
>
> a) Conta-se uma W por entidade que o processo cria, altera ou exclui no armazenamento
>    persistente. Criar, alterar e excluir a mesma entidade no mesmo processo é uma única W.
>
> b) Gravações de log técnico, cache, sessão, métricas e dados intermediários que não
>    sobrevivem ao processo não são W.
>
> c) Gravação de trilha de auditoria exigida pelo usuário funcional é W da entidade
>    `Auditoria` (ou do nome adotado no modelo).

> **RI-09 — Unicidade**
>
> a) Cada chave (processo, tipo, entidade) é contada uma única vez por processo,
>    independentemente de quantas ocorrências, telas, chamadas ou caminhos a implementem.
>
> b) A mesma entidade pode aparecer com tipos diferentes no mesmo processo (R e W de
>    `Pedido`, por exemplo). Cada tipo é uma chave.
>
> c) Um movimento é contado no processo em que ocorre. Se dois processos leem a mesma
>    entidade, há duas R.

> **RI-10 — Exclusões**
>
> Não entram no modelo, em nenhuma hipótese: código de infraestrutura e framework,
> autenticação e autorização embutidas em cada chamada (a autenticação só conta como o
> processo que o usuário dispara para se autenticar), tratamento de erros técnicos, retentativas,
> transações, migrações de esquema, testes, scripts de build e implantação, telemetria,
> e qualquer funcionalidade sem usuário funcional identificável.

## 2.7 Desfechos

Um processo não devolve só dados: devolve um **resultado**, e um processo que recusa por
dez motivos diferentes faz mais pelo usuário funcional do que um que recusa por um. A
MFO conta isso pelo que o sistema **emite de diferente**, nunca pela regra que o produz.

> **RI-12 — Desfecho**
>
> a) Um desfecho é um resultado que o processo devolve ao usuário funcional e que se
>    distingue dos demais pelo que o sistema emite: um código de resposta ou uma mensagem
>    diferente. Contam-se os desfechos **além do principal**: cada recusa ou erro de
>    negócio com código ou mensagem próprios e cada variante de sucesso com efeito
>    diferente (aprovação total e parcial). O desfecho principal não conta: ele já está
>    nas saídas e gravações do processo.
>
> b) Mesmo código ou mesma mensagem, ainda que produzidos por condições diferentes, são
>    **um** desfecho. O que a fronteira não distingue não é desfecho, é implementação.
>
> c) Mensagens parametrizadas pelo mesmo molde ("campo X é obrigatório", para cada campo)
>    são um desfecho. Códigos técnicos de autenticação, autorização e infraestrutura não
>    contam (RI-10).
>
> d) Cada desfecho tem identificador (o código ou o nome da mensagem, único no processo),
>    descrição e evidência (RI-11), e é registrado na lista `desfechos` do processo. Vale
>    1 PFO, como uma chave de movimento (RC-01).

O capítulo 12 mostra por que a unidade é o desfecho e não a regra, e o que acontece com
um processo que esconde várias regras sob um código só.

## 2.8 Evidência

> **RI-11 — Evidência**
>
> a) Todo processo, todo movimento e todo desfecho carregam pelo menos uma referência de evidência no
>    formato `FONTE:localizador`, em que `FONTE` é o identificador de uma fonte declarada
>    no modelo e `localizador` aponta o trecho (id de requisito, nome de tela, rota,
>    símbolo de código com caminho, tabela ou coluna, nome de mensagem).
>
> b) Elemento sem evidência disponível só entra marcado com `"inferido": true` e uma
>    `justificativa`. Ele é contado, mas reduz o grau de evidência do resultado.
>
> c) A evidência deve permitir que um revisor abra o artefato e confirme o elemento sem
>    conhecer o medidor. Evidência vaga ("código do sistema") não satisfaz a regra.

## 2.9 Estrutura do modelo

O modelo é um documento JSON validado pelo esquema [`schema/mfc.schema.json`](schema/mfc.schema.json).
Campos marcados com * são obrigatórios.

```jsonc
{
  "mfo": "1.0",                                    // * versão do método
  "software": "Biblioteca",                        // * nome do software ou escopo
  "versao": "1.0",                                 //   versão do software medida
  "proposito": "Dimensionar para contratação",     // * RI-01a
  "escopo": "RF-01 a RF-09 do documento de requisitos", // * RI-01b
  "nivel": "RC",                                   // * R (requisitos), C (código), RC (conciliado)
  "agente": { "tipo": "ia", "nome": "modelo X", "revisao_humana": true }, // * quem mediu
  "fontes": [                                      // * artefatos usados
    { "id": "REQ", "tipo": "requisitos", "ref": "docs/requisitos.md@v1.0" },
    { "id": "COD", "tipo": "codigo", "ref": "git:a1b2c3d" }
  ],
  "usuarios_funcionais": [                         // * RI-02
    { "id": "UF1", "nome": "Bibliotecário", "tipo": "pessoa" }
  ],
  "entidades": [                                   // * RI-03 (exceto a reservada DISPARO)
    { "id": "Livro", "descricao": "Título do acervo", "atributos": ["isbn", "titulo"], "evidencia": ["REQ:RF-01", "COD:db/livro"] }
  ],
  "processos": [                                   // * RI-04
    {
      "id": "P01",
      "nome": "Cadastrar livro",
      "disparadores": [ { "usuario": "UF1", "evento": "bibliotecário submete os dados de um novo livro" } ],
      "evidencia": ["REQ:RF-01", "COD:POST /livros"],
      "movimentos": [                              // RI-05 a RI-09
        { "tipo": "E", "entidade": "Livro", "evidencia": ["COD:LivroRequest"], "atributos": ["isbn", "titulo", "autor", "ano", "quantidade"] },
        { "tipo": "R", "entidade": "Livro", "evidencia": ["REQ:RF-01 (ISBN único)"] },
        { "tipo": "W", "entidade": "Livro", "evidencia": ["COD:LivroRepositorio.salvar"] }
      ],
      "desfechos": [                               // RI-12: além do principal, um por código ou mensagem
        { "id": "ISBN_DUPLICADO", "descricao": "ISBN já cadastrado", "evidencia": ["REQ:RF-01 (ISBN único)", "COD:LivroController 409"] }
      ]
    }
  ]
}
```

Campos opcionais em movimentos: `atributos` (lista; habilita a derivação informativa da
seção 3.5), `inferido` e `justificativa` (RI-11b), `alterado` (RC-03), `nota`. Cada
desfecho tem `id`, `descricao` e `evidencia`, com os mesmos opcionais `inferido`,
`justificativa`, `alterado` e `nota`.
Identificadores de processos e entidades devem ser estáveis entre versões do mesmo
software, pois a medição de mudanças depende deles.

## 2.10 Onde encontrar cada conceito

| Conceito | Em requisitos / histórias | Em telas e protótipos | Em APIs e contratos | Em código e banco |
|---|---|---|---|---|
| Usuário funcional | ator, "como <papel>", sistema citado | perfil de acesso | consumidor da API, sistema chamado | cliente autenticado, integração, agendador |
| Entidade | substantivo com atributos | formulário, grade, cartão | schema, tipo de payload | tabela, coleção, classe de domínio, mensagem |
| Processo | "o sistema deve permitir…", caso de uso, história | botão de ação, submissão, item de menu que executa algo | rota/operação, método RPC, tópico consumido | handler de rota, comando, job, consumer, callback de dispositivo |
| E | dados informados, arquivo recebido, evento | campos de entrada | parâmetros, corpo da requisição, mensagem recebida | parâmetros do handler, payload desserializado |
| X | dados apresentados, enviados, impressos, notificados | campos exibidos, listagem, download | corpo da resposta, chamada a serviço, mensagem publicada | serialização, render, chamada HTTP de saída, publish |
| Desfecho | "recusa se…", "informa o motivo", "ou informa que não há…" | mensagens de validação e alertas distintos | códigos de resposta, tabela de erros | exceções de negócio mapeadas para resposta, códigos 4xx, mensagens distintas |
| R | "consulta", "verifica", "com base em" | dados carregados na tela | — | SELECT/find/get, leitura de arquivo |
| W | "registra", "grava", "atualiza", "exclui" | ação de salvar | — | INSERT/UPDATE/DELETE/save, escrita de arquivo |
