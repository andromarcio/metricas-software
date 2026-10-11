<!-- Gerado por scripts/gera-docs.py a partir de MFO/12-decisoes.md. Não edite: edite a fonte e gere de novo. -->
# 12. Decisões: a segunda dimensão

> MFO — Medição Funcional Objetiva · Versão 1.0

## 12.1 O teto que o PFO não vê

O tamanho de um processo na MFO cresce com as entidades que ele movimenta. Quando o
conjunto de entidades satura, o PFO para de crescer, e dois processos de dificuldade
muito diferente empatam. O caso que expôs isso: `ADM-USR-06 — Aceitar convite`, o maior
processo do Aval, tem 12 PFO; um autorizador de compra com cartão, modelado com as mesmas
regras, tem 13. O autorizador decide dezenas de coisas antes de responder; o aceite de
convite, de quatro a seis, conforme a base. Movimento e decisão são eixos independentes,
e nenhum método de tamanho funcional mede o segundo: a APF dá 6 PF a ambos, o teto de uma
entrada externa; o COSMIC, o mesmo que a MFO.

A resposta não é pesar o PFO por complexidade. Isso devolveria o julgamento ao número e
quebraria a comparabilidade com PF e PFC. A resposta é um **segundo número**, contado com
a mesma disciplina do primeiro: unidade enumerável, evidência por item, validação,
concordância entre medições, e nunca somado ao PFO. É o suplemento D da RC-05, que deixa
de ser um sim ou não por processo e passa a ser uma contagem.

## 12.2 Duas bases de contagem, lado a lado

A unidade candidata é a **decisão**: uma condição sobre dados de negócio que muda o
desfecho do processo. Há duas formas objetivas de enumerá-la. A especificação registra as
duas e adota a primeira como base contratual (seção 12.4).

> **RC-05 — Suplemento D: decisões** (redação completa na seção 3.5)
>
> a) **D1, desfechos distintos.** Número de resultados que o processo pode produzir para
>    o usuário funcional, distinguíveis na fronteira por um teste de aceite: o desfecho
>    principal, cada variante de sucesso com efeito diferente (aprovação total e parcial)
>    e cada recusa ou erro de negócio distinto por código, por mensagem ou, sob o mesmo
>    código, pela condição de entrada que o dispara, desde que declarada na fonte. O
>    desfecho que só a condição distingue é marcado `oculto` e informado à parte. Códigos
>    técnicos de autenticação, autorização e infraestrutura não contam (RI-10).
>
> b) **D2, regras declaradas.** Número de regras de negócio enumeradas na fonte que
>    validam, restringem, mudam estado ou calculam, inclusive cada atributo derivado por
>    cálculo próprio. Regras de apresentação e regras técnicas não contam.
>
> c) Cada desfecho e cada regra é um item com identificador, descrição e evidência
>    (RI-11); o modelo registra os dois conjuntos em `decisoes` e a validação V-11 os
>    confere. D1 tem no mínimo um item, o desfecho principal.
>
> d) D1 e D2 são reportados por processo e no total, sempre ao lado do PFO e nunca
>    somados a ele. O rótulo do tamanho não muda.
>
> e) A base contratual é D1. D2 é registrada ao lado, como diagnóstico, até que
>    concordância entre medições e regressão sobre o histórico confirmem D1.

Onde cada base é lida:

| Fonte | D1 desfechos | D2 regras |
|---|---|---|
| Requisitos em prosa | mensagens e recusas descritas, variantes de resultado e, sob a mesma recusa, as condições enumeradas | regras numeradas, cálculos descritos |
| N3 do siesa-engine | tabela de erros da `## API`: uma causa por código e, sob o mesmo código, uma por condição enumerada na situação; `error_codes` do front-matter; mais o desfecho principal (RM-09, mecânico) | itens de `## Regras de negócio` e linhas de `## Derivações` (RM-09, mecânico) |
| Código | exceções de negócio, códigos de resposta e mensagens distintos alcançáveis do ponto de entrada, variantes de sucesso e, sob o mesmo código, cada condição que o dispara | condições sobre atributos de entidade e cálculos no caminho do ponto de entrada |
| Testes | um cenário por desfecho: "Então" distinto, ou o mesmo "Então" com entrada distinta que o provoca | cenários por regra |
| Sistema em execução | códigos de resposta observados por tipo de mensagem; o que só a condição distingue não é observável sem a fonte | não observável |

O teste de aceite é a âncora: um desfecho existe se há um teste que o produz com uma
entrada e o reconhece no resultado. É o que torna D1 verificável no código, nos testes e
em execução, e o que impede o código genérico de esconder a contagem: dez validações sob
um mesmo `422` são dez desfechos quando a fonte declara as dez condições, e um quando
declara só "dados inválidos".

## 12.3 Os mesmos processos, com a segunda dimensão

| Processo | PFO | D1 desfechos | dos quais só por teste | D2 regras |
|---|---|---|---|---|
| `ADM-USR-06 — Aceitar convite` (Aval, leitura revisada) | 12 | 6 | 2 | 4 |
| `ADM-USR-02 — Convidar usuário` (Aval) | 9 | 6 | 2 | 3 |
| Registrar empréstimo (biblioteca) | 7 | 6 | 1 | 4 |
| Cadastrar livro (biblioteca) | 4 | 2 | 0 | 1 |
| Autorizar compra (autorizador de cartão, exemplo hipotético) | 13 | 24 | 6 | 25 |

O autorizador e o aceite de convite empatam em PFO e se separam por um fator de quatro em
D1 e de seis em D2. O autorizador foi escrito para as duas bases divergirem de propósito:
uma regra de estado sem resposta própria (toda negativa incrementa o contador do dia)
conta só em D2, e seis regras de prevenção à fraude respondem com o mesmo código 59, por
decisão de segurança, de modo que só o teste de aceite de cada uma as separa. Contado só
por código, D1 cairia a 18. Os modelos estão em
[`exemplos/cartao/`](https://github.com/andromarcio/metricas-software/blob/main/MFO/exemplos/cartao/autorizacao-cartao.mfc.json),
[`exemplos/aval/adm-usr-revisado.mfc.json`](https://github.com/andromarcio/metricas-software/blob/main/MFO/exemplos/aval/adm-usr-revisado.mfc.json) e
[`exemplos/biblioteca-v1.mfc.json`](https://github.com/andromarcio/metricas-software/blob/main/MFO/exemplos/biblioteca-v1.mfc.json), com evidência em
cada desfecho e cada regra, verificadas por `auditar`.

Totais por sistema:

| Sistema | Processos | PFO | D1 | só por teste | D2 | D1 por processo | D2 por processo |
|---|---|---|---|---|---|---|---|
| Biblioteca v1 (leitura) | 9 | 51 | 23 | 2 | 15 | 2,6 | 1,7 |
| Aval, Usuários (leitura revisada) | 7 | 57 | 26 | 5 | 14 | 3,7 | 2,0 |
| Aval, Usuários (extração mecânica) | 6 | 37 | 24 | 5 | 14 | 4,0 | 2,3 |
| Aval inteiro (extração mecânica, 77 processos com registro) | 85 | 492 | 231 | 36 | 285 | 3,0 | 3,7 |
| Autorizador de cartão (hipotético) | 1 | 13 | 24 | 6 | 25 | 24 | 25 |

## 12.4 O que as duas bases revelam, e o que cada uma esconde

As duas bases divergem em direções opostas conforme o corpus. Na biblioteca D1 supera D2:
todo processo tem ao menos dois desfechos, o principal e uma recusa ou lista vazia, mesmo
com uma regra só ou nenhuma. No Aval inteiro D2 supera D1 por um quinto: as regras
numeradas incluem regras de estado que não produzem desfecho próprio ("a desativação
revoga o acesso sem remover registros"), e 36 dos 231 desfechos só existem porque a
coluna de situação da tabela de erros enumera as causas sob códigos genéricos como
`VALIDATION_ERROR` e `RESOURCE_NOT_FOUND`; contados só por código, seriam 195. No
autorizador as duas quase coincidem, 24 e 25, porque a rede exige um código distinto por
motivo de recusa, e a diferença está onde foi posta: a regra de estado e o bloco de
fraude da seção 12.3.

Contra os dois critérios que decidem a escolha, objetividade e resistência a inflar:

| Critério | D1 desfechos | D2 regras |
|---|---|---|
| Ancoragem | no que um teste de aceite distingue na fronteira: código, mensagem, variante de resultado, condição de disparo; verificável no código, nos testes e em execução | no que a especificação escreve; verificável na fonte e, com trabalho, no código |
| Mecânica na estrutura do engine | tabela de erros e `error_codes`: extração mecânica deu 24 contra 26 da leitura, e a diferença é um processo que a mecânica não separa | regras numeradas: extração mecânica deu 14 contra 14 da leitura |
| Como se infla | criando códigos ou mensagens distintos, o que exige comportamento visível e teste próprio; ou enumerando condições sob o mesmo código, a parte de D1 tão exposta quanto D2, que por isso o relatório informa à parte | desdobrando uma regra em várias ("cartão ativo", "não vencido", "não cancelado"); nada no sistema muda |
| O que esconde | regras sem desfecho próprio (regras de estado) e condições que a fonte não declara sob um código genérico | regras que não decidem nada (descrições de estado) |
| Convergência entre medidores | alta nos desfechos visíveis, porque a lista de códigos é fechada; média nos ocultos, que dependem da enumeração da fonte | média: depende da granularidade de quem escreve |

**Recomendação: D1 como base contratual, D2 como diagnóstico.** D1 vence nos dois
critérios na parte que domina a contagem, os desfechos visíveis (195 dos 231 no Aval, 18
dos 24 no autorizador), e a parte exposta fica identificada: o relatório diz quantos
desfechos só o teste distingue, e o contratante pode exigir o teste de aceite de cada um
antes de pagar. D2 continua no relatório porque é a única base onde a especificação é a
fonte e as regras já nascem numeradas, como nos N3, e porque D1 baixo com D2 alto aponta
regras sem comportamento observável. Sai do contrato quando a concordância entre medições
e a regressão de preço sobre o histórico confirmarem que D1 explica o esforço sem ele.

O código genérico, que parecia a ressalva de D1, resolve-se em três casos, e em nenhum
deles o medidor decide: decide a fonte.

1. **Causa preservada no detalhe.** A resposta é genérica, mas a situação, a mensagem ou
   o cenário diz o que a disparou. Conta um desfecho por causa, marcado oculto. O código
   genérico é mais eficiente para quem consome a interface e não custa nada à contagem.
2. **Causa apagada.** A fonte diz só "dados inválidos" e não enumera o que valida. Conta
   um, e está certo: o que não é distinguível na fronteira não é desfecho, é
   implementação. Quem quiser que conte precisa declarar as condições, e cada uma vira
   um teste de aceite, que é o incentivo que a métrica quer criar.
3. **Apagamento intencional.** Na fraude o sistema não deve revelar qual regra recusou,
   e a resposta é um só código. As condições estão na fonte e em seus testes de aceite,
   e a âncora no teste as conta. É o caso do autorizador: seis desfechos sob o código 59.

## 12.5 Para que serve o segundo número

- **Preço.** Dois números objetivos permitem dois coeficientes: `preço = a × PFO + b × D1`,
  calibrados por regressão sobre o histórico, por classe de sistema. O fornecedor deixa de
  perder no autorizador e de ganhar no cadastro; o contratante enxerga onde o esforço está.
  A classe de sistema continua tratando o que nenhum dos dois mede: latência, segurança,
  disponibilidade.
- **Teste e aceite.** Cada desfecho é, por definição, um teste de aceite com entrada e
  resultado próprios; cada regra, um cenário. D1 é a cobertura mínima de um processo e um
  gate mecânico de aceite (capítulo 9, RP-03): processo entregue sem um teste por desfecho
  não está pronto, e é no aceite que cada desfecho oculto prova que existe.
- **Agentes.** Para quem implementa, a lista de desfechos é o contrato de respostas e a
  lista de regras é o checklist de validações; para quem especifica, D1 baixo com D2 alto
  aponta regras sem comportamento observável, que valem uma pergunta ao PO.
- **Estimativa.** Os perfis típicos (capítulo 11) passam a carregar D1 e D2 por tipo de
  processo assim que houver medições suficientes; até lá, as decisões entram na
  estimativa como intervalo declarado, não como número.

## 12.6 Limites

Decisão não é esforço. Dezoito regras simples custam menos que três regras com cálculo
atuarial, e o número não distingue as duas. O que a MFO entrega é a contagem objetiva;
o peso de cada decisão por domínio é calibração, não contagem, e o passo 6 do bcp-agent
mostra a tentação a evitar: pontuar cada regra de 1 a 8 por julgamento devolve a
subjetividade que os dois números tiraram. Fora dos dois eixos ficam, como sempre, os
requisitos de qualidade, que pertencem à classe contratual do sistema.
