# 3. Regras de contagem, validação e mudança

> MFO — Medição Funcional Objetiva · Versão 1.0

A contagem é uma função determinística sobre um Modelo Funcional Canônico válido. Este
capítulo define a função (RC), as validações que o modelo deve satisfazer antes de ser
contado (V) e as regras para mudanças, agregação, suplemento e rotulagem.

## 3.1 Função de contagem

> **RC-01 — Tamanho de um processo**
>
> PFO(processo) = número de chaves distintas (tipo, entidade) entre os movimentos do
> processo. Cada chave vale 1 PFO, sem peso por tipo, por entidade ou por quantidade de
> atributos.

> **RC-02 — Tamanho do software**
>
> PFO(software) = Σ PFO(processo) para todos os processos do escopo.
>
> O resultado é um inteiro, sem limite superior, e é aditivo: o tamanho de dois escopos
> disjuntos na mesma camada é a soma dos tamanhos, observada a RC-04.

Consequências diretas:

- O menor processo possível tem 2 PFO (uma E e uma X ou W).
- Um processo que lê e grava a mesma entidade tem duas chaves (R e W) para ela.
- Repetições de uma mesma chave no modelo são erro de validação (V-06), não dedução
  silenciosa: o modelo deve ser canônico.

## 3.2 Validações obrigatórias

Um modelo que falhe em qualquer validação de nível **erro** não produz tamanho. Avisos
não impedem a contagem, mas são listados no relatório.

| Id | Nível | Regra verificada |
|---|---|---|
| V-01 | erro | Identificadores de usuários funcionais, entidades e processos são únicos; `mfo`, `software`, `proposito`, `escopo`, `nivel`, `agente`, `fontes`, `usuarios_funcionais`, `entidades` e `processos` estão presentes; `nivel` é `R`, `C` ou `RC`. |
| V-02 | erro | Todo processo tem pelo menos um movimento E (RI-04 T1). |
| V-03 | erro | Todo processo tem pelo menos um movimento X ou W (RI-04 T2). |
| V-04 | erro | Todo movimento referencia uma entidade declarada ou reservada; toda entidade declarada é referenciada por pelo menos um movimento. |
| V-05 | erro | `MENSAGEM` só aparece em X e no máximo uma vez por processo; `DISPARO` só aparece em E (RI-05b, RI-06c). |
| V-06 | erro | Não há duas chaves (tipo, entidade) iguais no mesmo processo (RI-09). |
| V-07 | erro | Todo processo e todo movimento tem evidência com prefixo de fonte declarada, ou `inferido: true` com `justificativa` (RI-11). |
| V-08 | erro | Todo processo tem pelo menos um disparador cujo `usuario` é um usuário funcional declarado (RI-02, RI-04 T1). |
| V-09 | aviso | Dois processos com o mesmo conjunto de chaves e os mesmos atributos (quando informados) podem ser o mesmo processo (RI-04 b). O relatório os lista para revisão. |
| V-10 | erro | Quando declarados: `producao.modo` é M0, M1, M2 ou M3 e `aceite.status` é aceito, pendente ou rejeitado, ambos com evidência ou inferência justificada; o bloco `producao` do modelo tem `abrange` (software ou mudanca) e valores numéricos não negativos (capítulo 9). |
| V-11 | erro | Quando declarado: `decisoes` tem as listas `desfechos` (ao menos um item) e `regras`; cada item tem `id` único na lista e evidência ou inferência justificada (RC-05, capítulo 12). |

A ferramenta de referência (`ferramentas/mfo.py validar`) implementa todas as validações.
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
> PFO(mudança) = incluídos + alterados + excluídos.
>
> Um movimento é marcado como alterado quando mudou o conjunto de atributos que ele
> movimenta ou a manipulação associada a ele (validação, cálculo, regra), conforme a
> evidência. Mudanças que não afetam nenhum movimento (cor, texto fixo, desempenho,
> refatoração, correção sem alteração de requisito) têm tamanho **zero** e devem ser
> tratadas fora da métrica, por acordo contratual, como faz o Guia STI para manutenção
> corretiva e adaptações não funcionais.

Marcação automática: em medição de nível C, `mfo.py impacto` aponta os movimentos cuja
evidência está em trecho modificado entre as duas versões (candidatos). A confirmação
segue a RD-01 do capítulo 8, pois nem toda modificação de código muda o movimento.

O tamanho de uma mudança também é um inteiro sem peso: incluir, alterar ou excluir um
movimento custa 1 PFO. Organizações que precisem remunerar esses três casos de forma
diferente devem fazê-lo por fator contratual aplicado **sobre** o PFO, e nunca alterar a
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

## 3.5 Suplemento D: decisões

A MFO, como o COSMIC, não mede manipulação de dados no tamanho. O que o PFO não vê, o
capítulo 12 mostra: dois processos com as mesmas entidades em movimento podem diferir em
uma ordem de grandeza no número de decisões que tomam. O suplemento D conta essa segunda
dimensão com a mesma disciplina do PFO e a reporta sempre à parte.

> **RC-05 — Suplemento D (decisões)**
>
> a) **D1, desfechos distintos:** número de resultados distintos que o processo pode
>    produzir para o usuário funcional: o desfecho principal, cada variante de sucesso com
>    efeito diferente e cada código ou mensagem de recusa ou erro de negócio distinto.
>    Códigos técnicos de autenticação, autorização e infraestrutura não contam (RI-10).
>
> b) **D2, regras declaradas:** número de regras de negócio enumeradas na fonte que
>    validam, restringem, mudam estado ou calculam, inclusive cada atributo derivado por
>    cálculo próprio. Regras de apresentação e técnicas não contam.
>
> c) Cada desfecho e cada regra é um item do bloco `decisoes` do processo, com
>    identificador, descrição e evidência (RI-11). D1 tem ao menos o desfecho principal.
>
> d) D1 e D2 são reportados por processo e no total, ao lado do PFO, e **nunca** somados a
>    ele. Processos sem o bloco aparecem como "n/d" e ficam fora das médias.
>
> e) Enquanto a organização não fixar uma das bases, as duas são registradas; o capítulo
>    12 compara as duas contra os critérios de objetividade e resistência a inflar.

O relatório mantém, a título informativo, a derivação por atributos (processo cujas
saídas ou gravações têm atributo ausente das entradas e leituras), que corresponde ao
critério "dados derivados" da APF; ela não substitui D1 nem D2.

## 3.6 Rotulagem

> **RC-06 — Rótulo**
>
> Todo resultado é apresentado com o rótulo, nesta ordem:
>
> `<n> PFO · MFO <versão do método> · nível <R|C|RC> · evidência <p>% · agente: <tipo e nome; revisão humana sim/não> · escopo: <software, versão, escopo>`
>
> em que `evidência` é a porcentagem de movimentos com pelo menos uma evidência (não
> inferidos). Mudanças usam a forma `<n> PFO de mudança (<i> incluídos, <a> alterados,
> <e> excluídos)` seguida do mesmo rótulo. Estimativas usam `≈ <n> PFO (estimativa
> <E0|E1|E2>, <mín> a <máx>)` (capítulo 11). O suplemento, quando reportado, vem em linha
> própria: `D = <n> de <NP>`.

Níveis de medição:

| Nível | Fonte principal | Momento | Observação |
|---|---|---|---|
| `R` | requisitos, histórias, protótipos, contratos de API | antes ou durante o desenvolvimento | é o tamanho do que foi pedido |
| `C` | código, banco, sistema em execução | depois | é o tamanho do que foi entregue |
| `RC` | ambos, conciliados | aceite, auditoria | divergências entre R e C documentadas no modelo |

Comparar um tamanho `R` com um `C` do mesmo software é legítimo e útil (mostra o que foi
pedido e não entregue, ou entregue sem ter sido pedido). Comparar softwares diferentes
exige o mesmo nível.
