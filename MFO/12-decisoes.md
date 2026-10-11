# 12. Desfechos: a decisão dentro do tamanho

> MFO — Medição Funcional Objetiva · Versão 1.0

## 12.1 O teto que o movimento não vê

O tamanho de um processo medido só por movimentos cresce com as entidades que ele toca.
Quando o conjunto de entidades satura, o número para de crescer, e dois processos de
dificuldade muito diferente empatam. O caso que expôs isso: `ADM-USR-06 — Aceitar
convite`, o maior processo do Aval, tem 11 movimentos; um autorizador de compra com
cartão, modelado com as mesmas regras, tem 12. O autorizador decide dezenas de coisas
antes de responder; o aceite de convite, três ou quatro. Movimento e decisão são eixos
independentes, e nenhum método de tamanho funcional mede o segundo: a APF dá 6 PF a
ambos, o teto de uma entrada externa; o COSMIC comprime todas as mensagens de um
processo numa única Exit.

A resposta não é pesar o movimento por complexidade, o que devolveria o julgamento ao
número, nem um segundo número ao lado do primeiro, o que dobraria o que um contrato tem
de carregar. A resposta é reconhecer que a decisão já deixa uma marca na fronteira: o
processo devolve **resultados distintos**. A MFO conta essa marca com a mesma unidade e
o mesmo peso de um movimento (RI-12, RC-05), e o tamanho continua um número só.

## 12.2 Por que o desfecho, e não a regra

Duas bases foram testadas antes da escolha, nos mesmos processos: o **desfecho**, o que o
sistema devolve de diferente, e a **regra declarada**, o que a especificação enumera.
Contra os dois critérios que decidem, objetividade e resistência a inflar:

| Critério | Desfecho (por código ou mensagem) | Regra declarada |
|---|---|---|
| Ancoragem | no que o sistema emite; verificável no código, nos testes e em execução | no que a especificação escreve; verificável na fonte e, com trabalho, no código |
| Mecânica | tabela de erros do N3: extração mecânica deu 13 contra 14 da leitura (Usuários) | regras numeradas: mecânica igual à leitura, mas só onde as regras já nascem numeradas |
| Como se infla | criando códigos ou mensagens distintos, o que exige comportamento visível e um teste próprio para cada um | desdobrando uma regra em várias ("cartão ativo", "não vencido", "não cancelado"); nada no sistema muda |
| O que esconde | regras que não mudam o que o processo devolve | regras que não decidem nada (descrições de estado) |
| Convergência entre medidores | alta: a lista de códigos é fechada | média: depende da granularidade de quem escreve |

O desfecho vence nos dois critérios, e por uma razão que vale para o método inteiro: ele
é a decisão vista **da fronteira**, que é de onde a MFO mede tudo. A regra é a decisão
vista de dentro, e tudo que se conta de dentro abre espaço para inflar.

Uma segunda escolha ficou implícita e vale registrar. Um desfecho poderia ser qualquer
resultado que um teste de aceite distingue, inclusive duas causas sob o mesmo código,
separáveis pela entrada que as dispara. A MFO não conta assim: conta o que o sistema
**emite** de diferente, e duas causas sob o mesmo código são um desfecho (RI-12 b). É a
definição mais curta, a lista é fechada e fecha a única porta de inflar que restava, a
de enumerar condições sob um código genérico. O custo está na seção 12.4.

## 12.3 Os mesmos processos, com os desfechos no número

| Processo | Movimentos | Desfechos | PFO |
|---|---|---|---|
| `ADM-USR-06 — Aceitar convite` (Aval, leitura revisada) | 11 | 3 | 14 |
| `ADM-USR-02 — Convidar usuário` (Aval) | 8 | 3 | 11 |
| Registrar empréstimo (biblioteca) | 6 | 4 | 10 |
| Cadastrar livro (biblioteca) | 3 | 1 | 4 |
| Autorizar compra (autorizador de cartão, exemplo hipotético) | 12 | 17 | 29 |

O autorizador e o aceite de convite, empatados em movimentos, separam-se por um fator de
dois. Os modelos estão em
[`exemplos/cartao/`](exemplos/cartao/autorizacao-cartao.mfc.json),
[`exemplos/aval/adm-usr-revisado.mfc.json`](exemplos/aval/adm-usr-revisado.mfc.json) e
[`exemplos/biblioteca-v1.mfc.json`](exemplos/biblioteca-v1.mfc.json), com evidência em
cada desfecho, verificada por `auditar`.

Totais por sistema:

| Sistema | Processos | Movimentos | Desfechos | PFO | Desfechos por processo |
|---|---|---|---|---|---|
| Biblioteca v1 (leitura) | 9 | 43 | 11 | 54 | 1,2 |
| Aval, Usuários (leitura revisada) | 7 | 50 | 14 | 64 | 2,0 |
| Aval, Usuários (extração mecânica) | 6 | 31 | 13 | 44 | 2,2 |
| Aval inteiro (extração mecânica) | 85 | 418 | 124 | 542 | 1,5 |
| Autorizador de cartão (hipotético) | 1 | 12 | 17 | 29 | 17 |

Os desfechos pesam entre um quinto e um quarto do tamanho nos sistemas de negócio, e
mais da metade no autorizador, onde a rede exige um código por motivo de recusa. É a
diferença que o movimento sozinho não via.

## 12.4 O código genérico

Um sistema que responde a dez validações com o mesmo código `422` e a mesma mensagem
tem um desfecho, não dez. Três situações aparecem na prática:

1. **Causa preservada no detalhe.** O código é genérico, mas a mensagem muda ("ISBN já
   cadastrado", "CPF já cadastrado"). Cada mensagem distinta é um desfecho: a fronteira
   distingue.
2. **Causa apagada.** A resposta é só "dados inválidos", para qualquer causa. Conta um, e
   está certo: o que não é distinguível na fronteira não é desfecho, é implementação.
   Quem quiser que conte precisa de códigos ou mensagens distintos, e cada um vira um
   comportamento visível e um teste de aceite, que é o incentivo que a métrica quer criar.
3. **Apagamento intencional.** O autorizador de cartão do exemplo responde a seis regras
   de prevenção à fraude com o mesmo código 59, por decisão de segurança: a rede e o
   portador não devem saber qual regra recusou. Conta um. É o caso em que a MFO
   deliberadamente mede menos do que o sistema decide, e é assim por desenho: o que a
   fronteira esconde de propósito, a métrica não revela. A dificuldade dessa lógica
   pertence à classe contratual do sistema, como a latência e a segurança.

Em nenhum dos três casos o medidor decide; decide o que o sistema emite.

## 12.5 Para que serve

- **Contrato.** Um número só, com dois primitivos que valem o mesmo. O preço por PFO
  continua um coeficiente, calibrado por classe de sistema, e o fornecedor deixa de
  perder no autorizador sem que o cadastro fique mais caro.
- **Teste e aceite.** Cada desfecho é um caso de teste com entrada e resultado próprios.
  O processo entregue sem um teste por desfecho não está pronto (capítulo 9, RP-03).
- **Agentes.** Para quem implementa, a lista de desfechos é o contrato de respostas; para
  quem especifica, um processo com muitas regras e poucos desfechos aponta regras sem
  comportamento observável, que valem uma pergunta ao PO.
- **Estimativa.** Os perfis típicos (capítulo 11) carregam um desfecho de recusa nos tipos
  que gravam, e a calibração local ajusta quantos um domínio costuma ter.

## 12.6 Limites

Desfecho não é esforço. Dezoito recusas simples custam menos que três recusas com cálculo
atuarial, e o número não distingue as duas. Regras que não mudam o que o processo devolve
não contam, e lógica deliberadamente opaca, como a de fraude, conta pelo que mostra. O que
a MFO entrega é a contagem objetiva; o peso de cada decisão por domínio é calibração, não
contagem, e o passo 6 do bcp-agent mostra a tentação a evitar: pontuar cada regra de 1 a
8 por julgamento devolve a subjetividade que o número tirou. Fora do tamanho ficam, como
sempre, os requisitos de qualidade, que pertencem à classe contratual do sistema.
