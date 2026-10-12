# 3. Regras de contagem, validação e mudança

> PFC — Pontos de Função Caixa · Versão 1.0

A contagem é uma função determinística sobre um Modelo Funcional Canônico válido. Este
capítulo define a função (RC), as validações que o modelo deve satisfazer antes de ser
contado (V) e as regras para mudanças, agregação, derivação informativa e rotulagem.

## 3.1 Função de contagem

> **RC-01 — Tamanho de um processo**
>
> PFC(processo) = número de chaves distintas (tipo, entidade) entre os movimentos do
> processo **mais** o número de desfechos distintos além do principal (RI-12). Cada chave
> e cada desfecho vale 1 PFC, sem peso por tipo, por entidade, por quantidade de atributos
> ou por dificuldade da regra que produz o desfecho.

> **RC-02 — Tamanho do software**
>
> PFC(software) = Σ PFC(processo) para todos os processos do escopo.
>
> O resultado é um inteiro, sem limite superior, e é aditivo: o tamanho de dois escopos
> disjuntos na mesma camada é a soma dos tamanhos, observada a RC-04.

Consequências diretas:

- O menor processo possível tem 2 PFC: uma E e uma X, uma W ou um desfecho.
- Um processo que recusa por três códigos distintos tem 3 PFC a mais do que o mesmo
  processo sem recusa; dez validações sob o mesmo código valem 1.
- Um processo que lê e grava a mesma entidade tem duas chaves (R e W) para ela.
- Repetições de uma mesma chave no modelo são erro de validação (V-06), não dedução
  silenciosa: o modelo deve ser canônico.

## 3.2 Validações obrigatórias

Um modelo que falhe em qualquer validação de nível **erro** não produz tamanho. Avisos
não impedem a contagem, mas são listados no relatório.

| Id | Nível | Regra verificada |
|---|---|---|
| V-01 | erro | Identificadores de usuários funcionais, entidades e processos são únicos; `pfc`, `software`, `proposito`, `escopo`, `nivel`, `agente`, `fontes`, `usuarios_funcionais`, `entidades` e `processos` estão presentes; `nivel` é `R`, `C` ou `RC`. |
| V-02 | erro | Todo processo tem pelo menos um movimento E (RI-04 T1). |
| V-03 | erro | Todo processo tem pelo menos um movimento X ou W, ou um desfecho (RI-04 T2). |
| V-04 | erro | Todo movimento referencia uma entidade declarada ou a reservada `DISPARO`; toda entidade declarada é referenciada por pelo menos um movimento. |
| V-05 | erro | `DISPARO` só aparece em E (RI-05 b) e não é declarada como entidade. |
| V-06 | erro | Não há duas chaves (tipo, entidade) iguais no mesmo processo (RI-09). |
| V-07 | erro | Todo processo, movimento e desfecho tem evidência com prefixo de fonte declarada, ou `inferido: true` com `justificativa` (RI-11). |
| V-08 | erro | Todo processo tem pelo menos um disparador cujo `usuario` é um usuário funcional declarado (RI-02, RI-04 T1). |
| V-09 | aviso | Dois processos com o mesmo conjunto de chaves e os mesmos atributos (quando informados) podem ser o mesmo processo (RI-04 b). O relatório os lista para revisão. |
| V-10 | erro | Quando declarados: `producao.modo` é M0, M1, M2 ou M3 e `aceite.status` é aceito, pendente ou rejeitado, ambos com evidência ou inferência justificada; o bloco `producao` do modelo tem `abrange` (software ou mudanca) e valores numéricos não negativos (capítulo 9). |
| V-11 | erro | Quando declarados: `desfechos` é uma lista e cada item tem `id` único no processo e evidência ou inferência justificada (RI-12, RC-05). |

A ferramenta de referência (`ferramentas/pfc.py validar`) implementa todas as validações.
O esquema JSON cobre a parte estrutural de V-01, V-04, V-05, V-10 e V-11; as demais são
semânticas. O campo `agente.tipo` admite `humano`, `ia` e `ferramenta` (extrator
determinístico, como o do capítulo 10).

## 3.3 Tamanho de uma mudança

> **RC-03 — Mudança**
>
> Dados dois modelos do mesmo software, anterior (A) e posterior (B), com identificadores
> estáveis de processos e entidades:
>
> - **incluídos** = chaves presentes em B e ausentes em A (inclusive todas as chaves de
>   processos novos);
> - **excluídos** = chaves presentes em A e ausentes em B (inclusive todas as chaves de
>   processos removidos);
> - **alterados** = chaves presentes em A e em B cujo movimento em B está marcado com
>   `"alterado": true`.
>
> PFC(mudança) = incluídos + alterados + excluídos.
>
> As chaves de um modelo são as de movimento (processo, tipo, entidade) e as de desfecho
> (processo, D, identificador). Um movimento é marcado como alterado quando mudou o
> conjunto de atributos que ele movimenta ou a manipulação associada a ele (validação,
> cálculo, regra), conforme a evidência; um desfecho, quando mudou o código, a mensagem
> ou a condição que o produz. Mudanças que não afetam nenhum movimento (cor, texto fixo, desempenho,
> refatoração, correção sem alteração de requisito) têm tamanho **zero** e devem ser
> tratadas fora da métrica, por acordo contratual, como faz o Guia STI para manutenção
> corretiva e adaptações não funcionais.

Marcação automática: em medição de nível C, `pfc.py impacto` aponta os movimentos cuja
evidência está em trecho modificado entre as duas versões (candidatos). A confirmação
segue a RD-01 do capítulo 8, pois nem toda modificação de código muda o movimento.

O tamanho de uma mudança também é um inteiro sem peso: incluir, alterar ou excluir um
movimento custa 1 PFC. Organizações que precisem remunerar esses três casos de forma
diferente devem fazê-lo por fator contratual aplicado **sobre** o PFC, e nunca alterar a
contagem.

## 3.4 Agregação e componentes

> **RC-04 — Agregação**
>
> a) Tamanhos só se somam quando medidos no mesmo nível de medição (R, C ou RC), na mesma
>    versão do método e em escopos disjuntos da mesma camada.
>
> b) Quando um software é medido como um todo, movimentos entre seus componentes
>    internos não existem: o que um componente envia a outro não atravessa a fronteira do
>    todo. Quando cada componente é medido separadamente (porque cada um tem seu próprio
>    escopo e usuários funcionais), esses movimentos existem em cada medição. Por isso o
>    tamanho do todo é, em geral, **menor** que a soma dos componentes, e as duas formas
>    não se misturam.
>
> c) Camadas diferentes (aplicação e serviço de infraestrutura, por exemplo) são medidas
>    separadamente e reportadas separadamente.

## 3.5 Desfechos e derivação

> **RC-05 — Desfechos no tamanho**
>
> a) Os desfechos identificados pela RI-12 (um por código ou mensagem distinto, além do
>    principal) entram na contagem como as chaves de movimento: 1 PFC cada, na RC-01, na
>    mudança (RC-03) e na concordância (seção 4.4). Cada um tem evidência (V-07, V-11).
>
> b) Não há segunda dimensão, suplemento nem peso por regra: da decisão entra no número só
>    o que ela devolve de visível. Regras sem desfecho próprio não contam, e dez
>    validações sob um mesmo código valem um desfecho. O capítulo 12 registra por que o
>    PFC escolheu assim.

O relatório mantém, a título informativo, a derivação por atributos (processo cujas
saídas ou gravações têm atributo ausente das entradas e leituras), que corresponde ao
critério "dados derivados" da APF; ela não entra no tamanho.

## 3.6 Rotulagem

> **RC-06 — Rótulo**
>
> Todo resultado é apresentado com o rótulo, nesta ordem:
>
> `<n> PFC · PFC <versão do método> · nível <R|C|RC> · evidência <p>% · agente: <tipo e nome; revisão humana sim/não> · escopo: <software, versão, escopo>`
>
> em que `evidência` é a porcentagem de movimentos e desfechos com pelo menos uma
> evidência (não inferidos). Mudanças usam a forma `<n> PFC de mudança (<i> incluídos, <a> alterados,
> <e> excluídos)` seguida do mesmo rótulo. Estimativas usam `≈ <n> PFC (estimativa
> <E0|E1|E2>, <mín> a <máx>)` (capítulo 11).

Níveis de medição:

| Nível | Fonte principal | Momento | Observação |
|---|---|---|---|
| `R` | requisitos, histórias, protótipos, contratos de API | antes ou durante o desenvolvimento | é o tamanho do que foi pedido |
| `C` | código, banco, sistema em execução | depois | é o tamanho do que foi entregue |
| `RC` | ambos, conciliados | aceite, auditoria | divergências entre R e C documentadas no modelo |

Comparar um tamanho `R` com um `C` do mesmo software é legítimo e útil (mostra o que foi
pedido e não entregue, ou entregue sem ter sido pedido). Comparar softwares diferentes
exige o mesmo nível.
