# 9. Medindo a produção com IA

> MFO — Medição Funcional Objetiva · Versão 1.0

## 9.1 O que muda e o que não muda

O mercado remunera fábricas de software por ponto de função produzido, com preços
calibrados para a produtividade de equipes humanas. Quando parte da produção passa a ser
feita por IA, duas coisas precisam ficar separadas:

- **O tamanho não muda.** Um software de 54 PFO tem 54 PFO, tenha sido escrito por uma
  pessoa, por um agente de IA ou por uma combinação. O PFO mede o produto. Se a unidade
  variasse com o produtor, a comparação entre softwares (objetivo O5) e o histórico de
  medições ficariam inutilizáveis. Este é o princípio P8, neutralidade de produtor.
- **O que muda é a relação entre tamanho, esforço e custo**, e também o perfil do
  trabalho humano, que migra de escrever código para especificar, dirigir a IA, revisar e
  aceitar. Muda ainda a facilidade de produzir coisa errada, ou coisa que ninguém pediu.

Consequência prática: o preço por PF calibrado para produtividade humana deixa de
refletir custo. Isso não invalida o contrato por tamanho, que continua sendo o instrumento
certo porque paga produto, e não esforço. Mas exige três coisas que a MFO fornece: tornar
visível **quanto** foi produzido com IA e com **que autonomia**, pagar apenas o que foi
**pedido, entregue e aceito**, e medir a qualidade **na mesma unidade**.

Os ganhos de produtividade com IA não são uniformes nem devem ser presumidos: o ISBSG
mede produtividade em horas por ponto de função, custo por ponto de função e defeitos por
ponto de função e publicou em 2026 comparações entre projetos antes e depois da adoção de
assistentes de código; o COSMIC divulgou em 2025 um estudo que combina medição funcional
com amostragem estatística justamente para verificar alegações de ganho de produtividade
com IA; e um experimento controlado de 2025 (METR) encontrou desenvolvedores experientes
mais lentos com IA em suas próprias bases de código. A resposta da MFO é medir, por
contrato e por modo de produção, em vez de adotar um fator de mercado.

## 9.2 Três perguntas, três medidas

| Pergunta | Medida | Onde fica |
|---|---|---|
| Quanto software foi entregue? | PFO (nível C) e PFO aceitos | `contar` |
| Quanto disso foi produzido com IA, e com que autonomia? | PFO por modo de produção (M0 a M3) | `producao.modo` em cada processo |
| Quanto custou e quanto rendeu? | PFO por hora humana, custo por PFO, custo de IA por PFO, defeitos por PFO | `producao` do modelo mais dados externos |

## 9.3 Modos de produção

> **RP-01 — Modo de produção**
>
> a) Cada processo recebe, por versão, o modo em que foi produzido ou alterado:
>
> | Modo | Nome | Quem faz o quê | Evidência típica |
> |---|---|---|---|
> | M0 | humano | pessoas escrevem o código; sem IA generativa | commits de autores humanos sem coautoria de IA |
> | M1 | IA assistida | pessoas escrevem; IA completa e sugere trechos | ferramenta ativa; minoria dos commits com coautoria de IA |
> | M2 | IA dirigida | pessoas especificam e revisam; IA produz o código do processo | commits ou PRs com coautoria de agente de IA e revisão humana registrada |
> | M3 | IA autônoma | IA produz e valida (testes) a partir da especificação; pessoas apenas aceitam | PR aberta por agente, testes gerados, aceite humano como única intervenção |
>
> b) O modo é atribuído por processo, com evidência (RI-11): trailers de coautoria em
>    commits, autor da PR, logs de sessão de agente, telemetria da ferramenta, apontamento
>    de horas. Quando as alterações de um processo misturam modos, vale o modo
>    predominante pelas evidências; sem evidência, o processo fica como `nd` (não declarado)
>    e o contrato decide o tratamento.
>
> c) O modo descreve a produção **desta versão**. Um processo criado por humanos (M0) e
>    alterado por IA dirigida (M2) é M2 na versão da alteração; o modelo da versão anterior
>    guarda o M0.

A escala é ordinal e deliberadamente curta. Quatro níveis são suficientes para
precificar e para comparar; mais níveis só aumentariam a divergência entre quem atribui.

## 9.4 Aceite por processo

> **RP-03 — Aceite**
>
> a) Cada processo pode registrar `aceite` com status `aceito`, `pendente` ou
>    `rejeitado` e evidência (teste de aceitação, ata, registro da ferramenta).
>
> b) PFO aceitos = Σ PFO dos processos com status `aceito`. É a base de remuneração.
>
> c) **Excedente** = PFO presentes no modelo de código (C) sem correspondente no modelo
>    de requisitos (R). É produção não solicitada. Não é remunerado por padrão, e é
>    especialmente relevante com IA, que produz funcionalidade extra com facilidade.
>
> d) Correções que não alteram movimento (RC-03) continuam com tamanho zero; a
>    qualidade é medida por defeitos por PFO, não por PFO de correção.

A IA pode gerar os testes de aceitação; o aceite é humano ou por critério automatizado
definido pelo contratante. Como cada processo tem seus movimentos enumerados, o critério
mínimo de aceite é objetivo: existe teste que exercita cada E, verifica cada X e confere
cada W do processo.

## 9.5 Indicadores de produção

> **RP-02 — Indicadores**
>
> A partir do bloco `producao` do modelo (horas humanas de todo o ciclo, custo humano,
> custo de IA, moeda, período) e do PFO produzido no mesmo período:
>
> | Indicador | Fórmula | Leitura |
> |---|---|---|
> | PFO produzidos por modo | Σ PFO por `producao.modo` | composição da produção |
> | Alavancagem humana | PFO produzidos / horas humanas | o que uma hora de pessoa rende, incluindo especificar, dirigir, revisar e aceitar |
> | Custo por PFO | (custo humano + custo de IA) / PFO produzidos | base para recalibrar o preço |
> | Custo de IA por PFO | custo de IA / PFO produzidos | peso do consumo de IA |
> | Participação da IA no custo | custo de IA / custo total | |
> | Taxa de aceite | PFO aceitos / PFO produzidos | retrabalho e qualidade de entrega |
> | Excedente | PFO em C sem correspondente em R | disciplina de escopo |
> | Defeitos por PFO | defeitos no período / PFO produzidos | qualidade (dado externo) |
>
> As horas humanas são as de **todo o ciclo**, não apenas as de codificação. Com IA, o
> esforço humano se desloca para antes e depois do código; medir só a codificação
> superestima o ganho.

O bloco `producao` declara `abrange: software` (primeira entrega, o modelo inteiro foi
produzido no período) ou `abrange: mudanca` (versões seguintes, só o que mudou). No
primeiro caso os indicadores saem em `contar`; no segundo, em `mudanca`, sobre os PFO de
mudança. Comparar modos só vale com a mesma definição de hora, de defeito e de aceite.

## 9.6 Remuneração por PFO na era da IA

> **RP-04 — O que a métrica entrega ao contrato**
>
> A MFO não fixa preços. Entrega, por versão: PFO entregues, PFO aceitos, PFO por modo de
> produção, excedente, alavancagem e custo por PFO. Com isso, o contrato pode adotar um
> dos arranjos abaixo, todos compatíveis com a métrica.

**Arranjo A, preço único recalibrado.** Um preço por PFO aceito, revisto periodicamente
pelo custo por PFO medido. É o mais simples e preserva o incentivo de pagar produto. Exige
transparência do modo de produção para que a recalibração tenha base.

**Arranjo B, preço por modo.** `preço_modo = preço_base × fator_modo`, com o fator
derivado da medição, não da negociação: `fator_modo = custo por PFO no modo / custo por
PFO em M0`, apurado na própria carteira ao longo de alguns ciclos. Processos `nd` recebem
o fator do modo de maior autonomia, o que protege o contratante e cria o incentivo
correto para o fornecedor registrar evidência.

**Arranjo C, adaptação de um contrato por fases.** O Guia STI distribui o esforço em
refino, implementação e teste. Em M2 e M3 a fase de implementação é majoritariamente da
IA; as fases humanas podem ser remuneradas integralmente e a implementação por fator:

| Fase (Guia STI) | Peso original | M0 | M2 | M3 |
|---|---|---|---|---|
| Refino | 20% | 20% | 20% | 20% |
| Implementação | 60% | 60% | 60% × f₂ | 60% × f₃ |
| Teste | 20% | 20% | 20% | 20% |

com f₂ e f₃ calibrados por medição (arranjo B). Os pesos de refino e teste tendem a
crescer em termos relativos, o que é coerente com a migração do trabalho humano.

**Regras comuns aos três arranjos:**

1. Paga-se PFO que estejam no escopo pedido (R), entregues (C) e aceitos. Excedente só é
   remunerado com aceite explícito do contratante.
2. Piso para mudanças pequenas, definido em contrato, nunca por ajuste na contagem.
3. Limite de defeitos por PFO, medido na mesma unidade, com retenção ou retrabalho sem
   nova remuneração acima do limite.
4. Evidência de modo obrigatória por processo; auditoria por amostragem (seção 4.5).
5. O preço nunca altera a contagem. Fatores, pisos e limites aplicam-se **sobre** o PFO.

## 9.7 O trabalho humano em produção com IA

Em M2 e M3 o entregável humano deixa de ser o código e passa a ser a especificação, a
direção e o aceite. A MFO mede isso na mesma unidade:

- **PFO especificados**: tamanho do modelo de nível R produzido pela equipe de requisitos.
  O próprio Modelo Funcional Canônico é uma especificação precisa o bastante para dirigir
  um agente: cada processo diz o que entra, o que é lido, o que é gravado e o que sai.
- **PFO revisados e aceitos**: tamanho do que passou por revisão humana e aceite.
- **Alavancagem humana**: PFO produzidos por hora humana em todo o ciclo.

A aderência R × C (seção 5.3) fecha o circuito: o que foi pedido e não entregue, o que
foi entregue sem ser pedido, e o que coincide. Em produção com IA, esse indicador vale
tanto quanto o tamanho.

## 9.8 Como atribuir o modo com evidência

Para medição de nível C a atribuição pode ser mecânica, a partir do histórico do
repositório: para cada processo, os commits que tocam os arquivos citados em suas
evidências; em cada commit, os trailers de coautoria (`Co-Authored-By`), o autor, a PR de
origem e quem a aprovou. O prompt complementar em
[`prompts/extracao-mfc.md`](prompts/extracao-mfc.md) faz essa atribuição com um modelo de
linguagem; o extrator do capítulo 10 implementa uma heurística determinística
(`--git`). Em qualquer caso, a evidência fica no modelo (`producao.evidencia`) e é
auditável por amostragem. A IA mede o que a IA produziu, com a mesma exigência de
evidência que vale para o resto do modelo.

## 9.9 Exemplo: Biblioteca v2 entregue com IA

A versão 2.0 do exemplo do capítulo 6 foi medida em nível RC depois da entrega, com modo
de produção e aceite por processo e dados de produção da mudança (valores ilustrativos):
P07 e P08 alterados em M2, P10 novo em M3, 6 horas humanas e R$ 40 de consumo de IA.
Saída de `mfo.py mudanca biblioteca-v1.mfc.json biblioteca-v2.mfc.json`:

```
**Rótulo:** 9 PFO de mudança (5 incluídos, 3 alterados, 1 excluídos) · MFO 1.0 · nível RC · evidência 100% · agente: ia (assistente de medição (exemplo)) + revisão humana · escopo: Biblioteca 2.0, Requisitos RF-01 a RF-10, com RF-07 e RF-08 revisados, conciliados com o código entregue

**Produção da mudança:** M2 IA dirigida 5 PFO (56%) · M3 IA autônoma 4 PFO (44%) · aceitos 9/9

Tamanho anterior: 54 PFO · tamanho posterior: 58 PFO · níveis: RC → RC

## Produção

| Modo de produção | Processos | PFO de mudança | % |
|---|---|---|---|
| M0 humano | 0 | 0 | 0% |
| M1 IA assistida | 0 | 0 | 0% |
| M2 IA dirigida | 2 | 5 | 56% |
| M3 IA autônoma | 1 | 4 | 44% |

Aceite: **9 PFO de mudança aceitos** (100%) · 0 pendentes · 0 rejeitados · 0 sem registro

### Indicadores de produção (abrange: a mudança, período 2026-05)

| Indicador | Valor |
|---|---|
| PFO de mudança produzidos | 9 |
| Horas humanas (todo o ciclo) | 6,0 |
| Alavancagem humana (PFO de mudança por hora humana) | 1,50 |
| Custo total (BRL) | 940,00 |
| Custo por PFO de mudança (BRL) | 104,44 |
| Custo de IA por PFO de mudança (BRL) | 4,44 |
| Participação da IA no custo | 4% |
```

A v1, produzida em M0 (160 horas humanas, valores ilustrativos), tem alavancagem de 0,34
PFO por hora humana e custo de R$ 444,44 por PFO (`contar biblioteca-v1.mfc.json`).
Comparadas, as duas versões mostram a mecânica do arranjo B: o fator de M2 e M3 em
relação a M0 sai da razão entre custos por PFO medidos (aqui 104,44 / 444,44 = 0,23, em
números de exemplo), não de uma tabela de mercado.

## 9.10 Riscos específicos e salvaguardas

| Risco | Salvaguarda |
|---|---|
| IA entrega funcionalidade que ninguém pediu e o tamanho sobe | Excedente R × C; só se paga o que está em R e foi aceito |
| Código volumoso sem função nova | O PFO ignora volume de código; só movimentos contam |
| Qualidade cai e o PFO por hora sobe | Defeitos por PFO e taxa de aceite na mesma unidade; limite contratual |
| Evidência de modo manipulável | Trailers e logs de ferramentas independentes do fornecedor; auditoria por amostragem; `nd` tratado como maior autonomia |
| Produtividade medida só na codificação | Horas humanas de todo o ciclo (RP-02) |
| Comparar modos com qualidade diferente | Comparações só com a mesma definição de aceite e defeito |
| Fator de mercado adotado sem medir | Calibração local por carteira, revista por ciclo |
