# 12. Decisões: a segunda dimensão

> MFO — Medição Funcional Objetiva · Versão 1.0

## 12.1 O teto que o PFO não vê

O tamanho de um processo na MFO cresce com as entidades que ele movimenta. Quando o
conjunto de entidades satura, o PFO para de crescer, e dois processos de dificuldade
muito diferente empatam. O caso que expôs isso: `ADM-USR-06 — Aceitar convite`, o maior
processo do Aval, tem 12 PFO; um autorizador de compra com cartão, modelado com as mesmas
regras, tem 13. O autorizador decide dezenas de coisas antes de responder; o aceite de
convite, quatro. Movimento e decisão são eixos independentes, e nenhum método de tamanho
funcional mede o segundo: a APF dá 6 PF a ambos, o teto de uma entrada externa; o COSMIC,
o mesmo que a MFO.

A resposta não é pesar o PFO por complexidade. Isso devolveria o julgamento ao número e
quebraria a comparabilidade com PF e PFC. A resposta é um **segundo número**, contado com
a mesma disciplina do primeiro: unidade enumerável, evidência por item, validação,
concordância entre medições, e nunca somado ao PFO. É o suplemento D da RC-05, que deixa
de ser um sim ou não por processo e passa a ser uma contagem.

## 12.2 Duas bases de contagem, lado a lado

A unidade candidata é a **decisão**: uma condição sobre dados de negócio que muda o
desfecho do processo. Há duas formas objetivas de enumerá-la, e a especificação adota as
duas enquanto não houver evidência suficiente para escolher.

> **RC-05 — Suplemento D: decisões** (redação completa na seção 3.5)
>
> a) **D1, desfechos distintos.** Número de resultados distintos que o processo pode
>    produzir para o usuário funcional: o desfecho principal, cada variante de sucesso
>    com efeito diferente (aprovação total e parcial) e cada código ou mensagem de recusa
>    ou erro de negócio distinto. Códigos técnicos de autenticação, autorização e
>    infraestrutura não contam (RI-10).
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

Onde cada base é lida:

| Fonte | D1 desfechos | D2 regras |
|---|---|---|
| Requisitos em prosa | mensagens e recusas descritas, variantes de resultado | regras numeradas, cálculos descritos |
| N3 do siesa-engine | tabela de erros da `## API` e `error_codes` do front-matter, mais o desfecho principal | itens de `## Regras de negócio` e linhas de `## Derivações` (RM-09, mecânico) |
| Código | exceções de negócio e códigos de resposta distintos alcançáveis do ponto de entrada, variantes de sucesso | condições sobre atributos de entidade e cálculos no caminho do ponto de entrada |
| Testes | cenários com "Então" distintos | cenários por regra |
| Sistema em execução | códigos de resposta observados por tipo de mensagem | não observável |

## 12.3 Os mesmos processos, com a segunda dimensão

| Processo | PFO | D1 desfechos | D2 regras |
|---|---|---|---|
| `ADM-USR-06 — Aceitar convite` (Aval, leitura revisada) | 12 | 4 | 4 |
| `ADM-USR-02 — Convidar usuário` (Aval) | 9 | 4 | 3 |
| Registrar empréstimo (biblioteca) | 7 | 5 | 4 |
| Cadastrar livro (biblioteca) | 4 | 2 | 1 |
| Autorizar compra (autorizador de cartão, exemplo hipotético) | 13 | 18 | 18 |

O autorizador e o aceite de convite empatam em PFO e se separam por um fator de quatro a
cinco na dimensão de decisões, nas duas bases. Os modelos estão em
[`exemplos/cartao/`](exemplos/cartao/autorizacao-cartao.mfc.json),
[`exemplos/aval/adm-usr-revisado.mfc.json`](exemplos/aval/adm-usr-revisado.mfc.json) e
[`exemplos/biblioteca-v1.mfc.json`](exemplos/biblioteca-v1.mfc.json), com evidência em
cada desfecho e cada regra, verificadas por `auditar`.

Totais por sistema:

| Sistema | Processos | PFO | D1 | D2 | D1 por processo | D2 por processo |
|---|---|---|---|---|---|---|
| Biblioteca v1 (leitura) | 9 | 51 | 21 | 15 | 2,3 | 1,7 |
| Aval, Usuários (leitura revisada) | 7 | 57 | 21 | 14 | 3,0 | 2,0 |
| Aval, Usuários (extração mecânica) | 6 | 37 | 19 | 14 | 3,2 | 2,3 |
| Aval inteiro (extração mecânica, 77 processos com registro) | 85 | 492 | 195 | 285 | 2,5 | 3,7 |
| Autorizador de cartão (hipotético) | 1 | 13 | 18 | 18 | 18 | 18 |

## 12.4 O que as duas bases revelam, e o que cada uma esconde

As duas bases divergem em direções opostas conforme o corpus. Na biblioteca D1 supera D2:
todo processo tem ao menos dois desfechos, o principal e uma recusa ou lista vazia, mesmo
com uma regra só ou nenhuma. No Aval inteiro D2 supera D1 por quase metade: as regras
numeradas incluem regras de estado que não produzem desfecho próprio ("a desativação
revoga o acesso sem remover registros") e várias validações desembocam num único código
`VALIDATION_ERROR`. No autorizador as duas coincidem porque a rede exige um código de
resposta distinto por motivo de recusa: cada regra tem seu desfecho.

Contra os dois critérios que decidem a escolha, objetividade e resistência a inflar:

| Critério | D1 desfechos | D2 regras |
|---|---|---|
| Ancoragem | no que o sistema emite: código, mensagem, variante de resultado; verificável no código, nos testes e em execução | no que a especificação escreve; verificável na fonte e, com trabalho, no código |
| Mecânica na estrutura do engine | tabela de erros e `error_codes`: extração mecânica deu 19 contra 21 da leitura | regras numeradas: extração mecânica deu 14 contra 14 da leitura |
| Como se infla | criando códigos ou mensagens distintos; cada um exige comportamento visível e teste próprio, o que limita o ganho | desdobrando uma regra em várias ("cartão ativo", "não vencido", "não cancelado"); nada no sistema muda |
| O que esconde | regras com o mesmo desfecho (dez validações num só 422 contam um) | regras que não decidem nada (descrições de estado) |
| Convergência entre medidores | alta: a lista de códigos é fechada | média: depende da granularidade de quem escreve |

A leitura preliminar favorece D1 nos dois critérios, com uma ressalva concreta: em
sistemas cujas respostas agrupam muitas validações sob um código genérico, D1 subconta, e
a saída é tornar os desfechos distintos, o que também beneficia o usuário e os testes. D2
continua útil onde a especificação é a única fonte e as regras já nascem numeradas, como
nos N3. A decisão fica para depois de alguns ciclos de medição com as duas bases
registradas; o custo de carregar as duas é pequeno, porque ambas saem de tabelas.

## 12.5 Para que serve o segundo número

- **Preço.** Dois números objetivos permitem dois coeficientes: `preço = a × PFO + b × D`,
  calibrados por regressão sobre o histórico, por classe de sistema. O fornecedor deixa de
  perder no autorizador e de ganhar no cadastro; o contratante enxerga onde o esforço está.
  A classe de sistema continua tratando o que nenhum dos dois mede: latência, segurança,
  disponibilidade.
- **Teste e aceite.** Cada desfecho é um caso de teste com resultado distinto; cada regra,
  um cenário. D1 é a cobertura mínima de um processo e um gate mecânico de aceite
  (capítulo 9, RP-03): processo entregue sem um teste por desfecho não está pronto.
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
