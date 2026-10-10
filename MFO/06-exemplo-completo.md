# 6. Exemplo completo — sistema de biblioteca

> MFO — Medição Funcional Objetiva · Versão 1.0

Este capítulo percorre o protocolo inteiro em um sistema pequeno: requisitos, modelo,
relatório gerado pela ferramenta, medição de uma mudança, segunda medição com índice de
concordância e, ao final, o mesmo sistema contado em APF e em COSMIC para situar o
resultado. Os modelos estão em [`exemplos/`](exemplos/) e todos os números abaixo foram
produzidos por `ferramentas/mfo.py`.

## 6.1 Requisitos funcionais (fonte `REQ`)

**RF-01 Cadastrar livro.** O bibliotecário informa título, autor, ISBN, ano e quantidade
de exemplares. O ISBN deve ser único no acervo. O sistema grava o livro e confirma; em
caso de erro de validação, informa o motivo.

**RF-02 Alterar livro.** O bibliotecário altera os dados de um livro existente; a unicidade
do ISBN continua valendo. O sistema grava e confirma.

**RF-03 Excluir livro.** O bibliotecário solicita a exclusão de um livro. O sistema recusa
se houver empréstimo ativo do livro; caso contrário, exclui e confirma.

**RF-04 Consultar livros.** O bibliotecário informa, opcionalmente, título e/ou autor. O
sistema lista os livros (título, autor, ISBN, ano, quantidade) ou informa que nenhum foi
encontrado. A lista pode ser exportada em CSV.

**RF-05 Cadastrar leitor.** O bibliotecário informa nome, CPF, e-mail, telefone e situação
(ativo ou inativo). O CPF deve ser único. O sistema grava e confirma.

**RF-06 Registrar empréstimo.** O bibliotecário informa o leitor, o livro e a data. O sistema
verifica: leitor ativo; exemplar disponível (quantidade maior que o número de empréstimos
ativos do livro); leitor com menos de três empréstimos ativos. Grava o empréstimo com
status "ativo" e data prevista de devolução (data mais 14 dias), apresenta a data prevista
e confirma; recusas informam o motivo.

**RF-07 Registrar devolução.** O bibliotecário informa o empréstimo e a data de devolução.
O sistema calcula a multa (dias de atraso vezes o valor diário, parâmetro do sistema),
grava a devolução, a multa e o status "devolvido", apresenta o valor da multa e confirma.

**RF-08 Relatório de atrasos.** O bibliotecário solicita o relatório, sem parâmetros. O
sistema lista os empréstimos ativos com data prevista anterior à data atual: nome do
leitor, título do livro, data prevista, dias de atraso e multa estimada; ou informa que
não há atrasos. O relatório pode ser exibido em tela ou gerado em PDF.

**RF-09 Notificar atrasos.** Diariamente, o sistema envia, por um serviço externo de
e-mail, uma mensagem a cada leitor com empréstimo em atraso (nome do leitor, título do
livro, data prevista, dias de atraso) e registra a notificação com a data de envio e o
status devolvido pelo serviço.

## 6.2 Preparação (passo 1 do protocolo)

| Item | Valor |
|---|---|
| Propósito | Dimensionar o sistema para contratação |
| Escopo | RF-01 a RF-09 |
| Nível | `RC` (requisitos conciliados com o código entregue em [`exemplos/codigo-biblioteca/v1`](exemplos/codigo-biblioteca/README.md); a extração aqui descrita é a de requisitos, e o capítulo 8 cobre a parte de código) |
| Fontes | `REQ` = este capítulo, seção 6.1; `COD` = código da v1; `TST` = testes de aceitação; `PROC` = histórico de produção |
| Usuários funcionais | UF1 Bibliotecário (`pessoa`); UF2 Relógio diário (`relogio`); UF3 Serviço de e-mail (`sistema`) |
| Glossário de entidades | Livro, Leitor, Emprestimo, ParametroMulta, Notificacao |

Decisões de fronteira registradas antes da extração:

- O serviço de e-mail é acessado por chamada, logo é usuário funcional (RI-01 d), não
  armazenamento.
- O valor diário da multa é parâmetro de negócio com atributo próprio: entidade
  `ParametroMulta` (RI-03 d). Não há processo que o mantenha dentro do escopo, o que é
  permitido: a entidade existe porque é lida.
- "Exportar em CSV" (RF-04) e "tela ou PDF" (RF-08) não criam processos (RI-04 b).

## 6.3 Modelo Funcional Canônico (passo 2)

Modelo completo: [`exemplos/biblioteca-v1.mfc.json`](exemplos/biblioteca-v1.mfc.json).
Abaixo, os movimentos de cada processo com a regra que os sustenta.

**P01 Cadastrar livro** (UF1) — 4 PFO

| Tipo | Entidade | Atributos | Evidência e regra |
|---|---|---|---|
| E | Livro | isbn, titulo, autor, ano, quantidade | RF-01 · RI-05 a |
| R | Livro | isbn | RF-01 "ISBN único" · RI-07 a (lê para decidir) |
| W | Livro | isbn, titulo, autor, ano, quantidade | RF-01 · RI-08 a |
| X | MENSAGEM | — | RF-01 confirmação e erros · RI-06 c |

**P02 Alterar livro** (UF1) — 4 PFO: E Livro · R Livro · W Livro · X MENSAGEM. A exibição
dos dados atuais antes da alteração pertence a P04 (tabela de casos frequentes).

**P03 Excluir livro** (UF1) — 4 PFO

| Tipo | Entidade | Atributos | Evidência e regra |
|---|---|---|---|
| E | Livro | isbn | RF-03 |
| R | Emprestimo | livro, status | RF-03 "recusa se houver empréstimo ativo" · RI-07 b (lê atributos para decidir) |
| W | Livro | isbn | RF-03 · RI-08 a (exclusão é W) |
| X | MENSAGEM | — | RF-03 |

Não há R de Livro: a existência do livro é verificada implicitamente pela exclusão (RI-07 b).

**P04 Consultar livros** (UF1) — 4 PFO: E Livro (filtros titulo, autor) · R Livro · X Livro ·
X MENSAGEM ("nenhum encontrado"). O CSV é formato, não processo.

**P05 Cadastrar leitor** (UF1) — 4 PFO: E Leitor · R Leitor (CPF único) · W Leitor · X MENSAGEM.

**P06 Registrar empréstimo** (UF1) — 7 PFO

| Tipo | Entidade | Atributos | Evidência e regra |
|---|---|---|---|
| E | Emprestimo | leitor, livro, data_emprestimo | RF-06 · RI-03 b (chaves de leitor e livro são atributos do empréstimo) |
| R | Leitor | cpf, situacao | RF-06 "leitor ativo" |
| R | Livro | isbn, quantidade | RF-06 "exemplar disponível" |
| R | Emprestimo | leitor, livro, status | RF-06 empréstimos ativos do livro e do leitor |
| W | Emprestimo | leitor, livro, data_emprestimo, data_prevista, status | RF-06 |
| X | Emprestimo | data_prevista | RF-06 "apresenta a data prevista" · RI-06 a |
| X | MENSAGEM | — | RF-06 recusas e confirmação |

**P07 Registrar devolução** (UF1) — 6 PFO: E Emprestimo (id, data_devolucao) · R Emprestimo ·
R ParametroMulta (valor_dia) · W Emprestimo (data_devolucao, multa, status) · X Emprestimo
(multa) · X MENSAGEM.

**P08 Relatório de atrasos** (UF1) — 9 PFO

| Tipo | Entidade | Atributos | Evidência e regra |
|---|---|---|---|
| E | DISPARO | — | RF-08 "sem parâmetros" · RI-05 b |
| R | Emprestimo | id, leitor, livro, data_prevista, status | RF-08 |
| R | Leitor | cpf, nome | RF-08 "nome do leitor" |
| R | Livro | isbn, titulo | RF-08 "título do livro" |
| R | ParametroMulta | valor_dia | RF-08 "multa estimada" |
| X | Emprestimo | data_prevista, dias_atraso, multa_estimada | RF-08 · RI-06 a |
| X | Leitor | nome | RF-08 · RI-06 a (atributo pertence a Leitor, RI-03 b) |
| X | Livro | titulo | RF-08 · RI-06 a |
| X | MENSAGEM | — | RF-08 "não há atrasos" |

**P09 Notificar atrasos** (UF2 relógio) — 9 PFO

| Tipo | Entidade | Atributos | Evidência e regra |
|---|---|---|---|
| E | DISPARO | — | RF-09 "diariamente" · RI-05 b (tique do relógio) |
| R | Emprestimo | id, leitor, livro, data_prevista, status | RF-09 |
| R | Leitor | cpf, nome, email | RF-09 |
| R | Livro | isbn, titulo | RF-09 |
| X | Emprestimo | data_prevista, dias_atraso | RF-09 conteúdo do e-mail, para UF3 · RI-06 b |
| X | Leitor | nome, email | RF-09 destinatário, para UF3 |
| X | Livro | titulo | RF-09 conteúdo do e-mail, para UF3 |
| E | Notificacao | status_envio | RF-09 "status devolvido pelo serviço" · RI-05 c (a resposta é usada) |
| W | Notificacao | emprestimo, data_envio, status_envio | RF-09 "registra a notificação" |

## 6.4 Relatório gerado (passo 3)

Saída literal de `python3 MFO/ferramentas/mfo.py contar MFO/exemplos/biblioteca-v1.mfc.json`:

```
# Relatório MFO — Biblioteca 1.0

**Rótulo:** 51 PFO · MFO 1.0 · nível RC · evidência 100% · agente: ia (assistente de medição (exemplo)) + revisão humana · escopo: Biblioteca 1.0, Requisitos RF-01 a RF-09 (acervo, leitores, empréstimos, devoluções, atrasos), conciliados com o código entregue

**Produção:** M0 humano 51 PFO (100%) · aceitos 51/51

**Propósito:** Dimensionar o sistema para contratação e servir de exemplo de referência da MFO

## Perfil funcional

| Indicador | Valor |
|---|---|
| PFO | **51** |
| NP (processos) | 9 |
| NE (entidades) | 5 |
| E / X / R / W | 10 / 17 / 17 / 7 |
| Densidade (PFO/NP) | 5,67 |
| Persistência ((R+W)/PFO) | 0,47 |
| Interface ((E+X)/PFO) | 0,53 |
| Entidades por processo (NE/NP) | 0,56 |
| Evidência | 100% (0 inferidos) |
| D (derivação, RC-05) | 4 de 9 |

## Processos

| ID | Processo | E | X | R | W | PFO | Deriv. | Evid. | Modo | Aceite |
|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Cadastrar livro | 1 | 1 | 1 | 1 | **4** | não | 4/4 | M0 | aceito |
| P02 | Alterar livro | 1 | 1 | 1 | 1 | **4** | não | 4/4 | M0 | aceito |
| P03 | Excluir livro | 1 | 1 | 1 | 1 | **4** | não | 4/4 | M0 | aceito |
| P04 | Consultar livros | 1 | 2 | 1 | 0 | **4** | não | 4/4 | M0 | aceito |
| P05 | Cadastrar leitor | 1 | 1 | 1 | 1 | **4** | não | 4/4 | M0 | aceito |
| P06 | Registrar empréstimo | 1 | 2 | 3 | 1 | **7** | sim | 7/7 | M0 | aceito |
| P07 | Registrar devolução | 1 | 2 | 2 | 1 | **6** | sim | 6/6 | M0 | aceito |
| P08 | Relatório de atrasos | 1 | 4 | 4 | 0 | **9** | sim | 9/9 | M0 | aceito |
| P09 | Notificar atrasos | 2 | 3 | 3 | 1 | **9** | sim | 9/9 | M0 | aceito |
| | **Total** | 10 | 17 | 17 | 7 | **51** | | | | |
```

O relatório segue com a seção **Produção** (modo de produção, aceite e indicadores de
alavancagem e custo), descrita no capítulo 9. Com o bloco `decisoes` registrado, a tabela
ganha as colunas D1 e D2 (capítulo 12): na v1, 21 desfechos e 15 regras ao lado dos 51 PFO.

Leitura do perfil: densidade alta (5,67) para um sistema de cadastro, puxada pelos dois
processos de atraso, que cruzam quatro entidades. O suplemento D aponta exatamente os
quatro processos que calculam algo (data prevista, multa, dias de atraso): é o que a APF
chamaria de "dados derivados", obtido aqui por comparação de conjuntos de atributos.

## 6.5 Medindo uma mudança (RC-03)

A versão 2.0 traz três alterações de requisitos:

- **RF-07 (revisado):** o bibliotecário pode marcar isenção da multa, informando a
  justificativa; o sistema grava a isenção e a justificativa.
- **RF-08 (revisado):** o relatório deixa de apresentar a multa estimada.
- **RF-10 (novo) Consultar leitor:** o bibliotecário informa o CPF; o sistema apresenta
  nome, CPF, e-mail, telefone e situação, ou informa que o leitor não foi encontrado.

No modelo da v2 ([`exemplos/biblioteca-v2.mfc.json`](exemplos/biblioteca-v2.mfc.json)),
os movimentos E e W de Emprestimo em P07 ganharam atributos e foram marcados
`"alterado": true`; em P08, a R de ParametroMulta foi removida e a X de Emprestimo perdeu
um atributo (marcada alterada); P10 foi incluído. Saída de
`mfo.py mudanca biblioteca-v1.mfc.json biblioteca-v2.mfc.json`:

```
**Rótulo:** 8 PFO de mudança (4 incluídos, 3 alterados, 1 excluídos) · MFO 1.0 · nível RC · evidência 100% · agente: ia (assistente de medição (exemplo)) + revisão humana · escopo: Biblioteca 2.0, Requisitos RF-01 a RF-10, com RF-07 e RF-08 revisados, conciliados com o código entregue

**Produção da mudança:** M2 IA dirigida 4 PFO (50%) · M3 IA autônoma 4 PFO (50%) · aceitos 8/8

Tamanho anterior: 51 PFO · tamanho posterior: 54 PFO · níveis: RC → RC

## Incluídos (4)
- P10 · E Leitor
- P10 · R Leitor
- P10 · X Leitor
- P10 · X MENSAGEM

## Alterados (3)
- P07 · E Emprestimo
- P07 · W Emprestimo
- P08 · X Emprestimo

## Excluídos (1)
- P08 · R ParametroMulta
```

A mudança mede 8 PFO embora o software tenha crescido apenas 3 PFO (51 para 54): o
tamanho da mudança inclui o que foi alterado e removido, exatamente como PF e PFC de
melhoria. A mesma mudança, vista pelo diff do código, está na seção 8.5; sua composição
por modo de produção e os indicadores de custo, na seção 9.9.

## 6.6 Segunda medição e concordância (passos 4 e 5)

Um segundo medidor, sem acesso ao primeiro modelo e com o mesmo glossário, produziu
[`exemplos/biblioteca-v1-medicao-B.mfc.json`](exemplos/biblioteca-v1-medicao-B.mfc.json)
a partir dos requisitos (nível R). Comparar uma medição de nível R com a de nível RC do
mesmo software é legítimo (seção 3.6). Saída de `mfo.py concordancia`:

```
**Índice de concordância:** 0,887 (47 chaves comuns de 53)
PFO em A: 51 · PFO em B: 49
Leitura: divergência localizada: revisar os processos divergentes e o glossário de entidades

## Só em A (4)
- P01 · R Livro
- P09 · X Emprestimo
- P09 · X Leitor
- P09 · X Livro

## Só em B (2)
- P03 · R Livro
- P09 · X Notificacao
```

Os totais diferem pouco (51 contra 49), mas o índice mostra que há seis chaves em
desacordo, o que o total esconderia. Conciliação, uma linha por divergência:

| Chave | Regra | Decisão | Evidência que decide |
|---|---|---|---|
| P01 · R Livro (só em A) | RI-07 a | manter | RF-01 exige ISBN único: o processo lê Livro para decidir |
| P03 · R Livro (só em B) | RI-07 b | remover | RF-03 não usa atributo de Livro; a existência é implícita na exclusão |
| P09 · X Emprestimo, X Leitor, X Livro (só em A) e X Notificacao (só em B) | RI-06 a, RI-03 b | manter A, remover B | os atributos enviados (nome, e-mail, título, data prevista, dias) pertencem a Leitor, Livro e Emprestimo; Notificacao persiste apenas data e status de envio |

O modelo conciliado coincide com A; o rótulo final registra os dois agentes. Em uma
organização, as três linhas acima entram na base de exemplos que realimenta o prompt.

## 6.7 O mesmo sistema em APF e em COSMIC (ilustrativo)

As contagens abaixo foram feitas pelas regras de cada método para situar o PFO. São
ilustrativas: contagens oficiais exigem medidores certificados, e alguns itens admitem
leituras diferentes, indicadas nas observações.

### APF (IFPUG CPM 4.3.1)

| Função | Tipo | ALR ou RLR | DER | Complexidade | PF |
|---|---|---|---|---|---|
| Livro | ALI | 1 RLR | 5 | Baixa | 7 |
| Leitor | ALI | 1 RLR | 5 | Baixa | 7 |
| Empréstimo | ALI | 1 RLR | 8 | Baixa | 7 |
| Notificação | ALI | 1 RLR | 4 | Baixa | 7 |
| Parâmetro de multa | dados de código | — | — | não contado | 0 |
| Cadastrar livro | EE | 1 | 7 | Baixa | 3 |
| Alterar livro | EE | 1 | 7 | Baixa | 3 |
| Excluir livro | EE | 2 | 3 | Baixa | 3 |
| Consultar livros | CE | 1 | 7 | Baixa | 3 |
| Cadastrar leitor | EE | 1 | 7 | Baixa | 3 |
| Registrar empréstimo | EE | 3 | 6 | Alta | 6 |
| Registrar devolução | EE | 1 | 5 | Baixa | 3 |
| Relatório de atrasos | SE | 3 | 6 | Média | 5 |
| Notificar atrasos | SE | 4 | 6 | Alta | 7 |
| **Total** | | | | | **64 PF** |

Observações: o parâmetro de multa foi tratado como dados de código (CPM Parte 3, cap. 1;
Guia STI 4.15); se fosse ALI, somaria 7 PF e elevaria a complexidade de duas transações.
"Notificar atrasos" foi classificado como SE por enviar dados derivados para fora da
fronteira e manter um ALI. A APF chega a 64 PF porque conta os quatro arquivos lógicos
diretamente (28 PF, 44% do total), enquanto na MFO os dados só pesam quando movimentados.

### COSMIC 3.0.1

| Processo funcional | E | X | R | W | PFC |
|---|---|---|---|---|---|
| Cadastrar livro | 1 | 1 | 1 | 1 | 4 |
| Alterar livro | 1 | 1 | 1 | 1 | 4 |
| Excluir livro | 1 | 1 | 1 | 1 | 4 |
| Consultar livros | 1 | 2 | 1 | 0 | 4 |
| Cadastrar leitor | 1 | 1 | 1 | 1 | 4 |
| Registrar empréstimo | 1 | 2 | 3 | 1 | 7 |
| Registrar devolução | 1 | 2 | 2 | 1 | 6 |
| Relatório de atrasos | 1 | 2 a 4 | 4 | 0 | 7 a 9 |
| Notificar atrasos | 2 | 1 a 3 | 3 | 1 | 7 a 9 |
| **Total** | | | | | **47 a 51 PFC** |

Observação: a faixa vem de um único ponto de julgamento, a identificação dos grupos de
dados nas saídas compostas (a linha do relatório e o e-mail descrevem um objeto de
interesse "empréstimo em atraso" ou três objetos?). O manual COSMIC admite as duas
leituras conforme os RFU. A MFO fixa a leitura por entidade (RI-06 a) e por isso chega
sempre a 51; a segunda medição da seção 6.6 mostrou exatamente essa divergência sendo
detectada e fechada por regra.

### Resumo

| Método | Tamanho | Fonte de variação entre medidores |
|---|---|---|
| APF | 64 PF | classificação de dados de código, SE × CE, faixas de complexidade |
| COSMIC | 47 a 51 PFC | grupos de dados em saídas compostas |
| MFO | 51 PFO | nenhuma após as regras; divergências restantes medidas pelo índice de concordância |
