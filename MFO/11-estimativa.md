# 11. Estimativa

> MFO — Medição Funcional Objetiva · Versão 1.0

Medir exige artefato: requisitos, código ou sistema. Estimar é dizer quanto o software vai
ter antes de o artefato existir, para orçar, contratar e planejar. A MFO trata os dois com
o **mesmo modelo e a mesma unidade**: uma estimativa é um modelo canônico cujos movimentos
foram **inferidos** por perfis típicos em vez de extraídos com evidência. O grau de
evidência do rótulo diz quanto do número ainda é estimativa, e o número converge para a
medição à medida que os artefatos surgem e os movimentos inferidos são substituídos por
evidenciados. Não há um segundo método nem uma segunda unidade.

## 11.1 Princípios

> **RE-01 — Estimativa por perfil típico**
>
> a) Um item de backlog, história, caso de uso ou função de proposta vira um processo
>    com nome, tipo e entidades tocadas. O tipo é declarado ou inferido pelo verbo que
>    abre o nome: criar, alterar, excluir, estado (aprovar, cancelar, desativar…),
>    consultar, relatório, processar (automação por evento ou relógio) e integrar.
>
> b) Os movimentos e desfechos do processo são os do **perfil típico** do tipo (tabela da
>    seção 11.3), aplicado à entidade principal e às entidades adicionais tocadas: cada
>    entidade adicional acrescenta uma leitura e, em consultas e relatórios, também uma
>    saída; criar, alterar, excluir, mudar de estado e integrar trazem um desfecho de
>    recusa; consultar, relatório e processar, nenhum.
>
> c) Todo movimento e desfecho estimado leva `inferido: true` com a justificativa "perfil típico". O
>    modelo passa pelas mesmas validações de um modelo medido e é contado pela mesma
>    função. O rótulo muda: `≈ n PFO (estimativa Ex, mín a máx)`.

> **RE-02 — Calibração local**
>
> Os perfis padrão servem para começar. Cada modelo medido é uma observação: PFO por
> processo, por tipo. `mfo.py perfis` consolida essas observações (mediana, quartis) e
> `mfo.py estimar --perfis` as usa no lugar dos padrões. A base de calibração é registrada
> na estimativa. Perfis de outro domínio ou de outra organização não substituem os
> próprios; servem só até existirem medições locais.

> **RE-03 — Intervalo obrigatório**
>
> Uma estimativa é sempre um intervalo com um valor central. Sem calibração, o intervalo é
> o padrão do nível (E0 ±40%, E1 ±25%, E2 ±10%). Com calibração, é a soma dos quartis
> P25 e P75 dos tipos estimados. O erro relativo contra a medição posterior é registrado e
> alimenta a revisão dos perfis (seção 11.6).

> **RE-04 — De tamanho a esforço e custo**
>
> A estimativa de tamanho é neutra quanto ao produtor (P8). Esforço e custo saem dela pela
> alavancagem e pelo custo por PFO **do modo de produção previsto** (capítulo 9): o mesmo
> escopo estimado em 120 PFO gera horas e preço diferentes se será produzido em M0 ou em
> M2, e o contrato deve dizer qual.

## 11.2 Níveis

| Nível | Insumo | Como | Intervalo padrão | Quando |
|---|---|---|---|---|
| **E0 indicativo** | lista de entidades, com as que serão mantidas | cada entidade mantida gera os quatro processos de manutenção (criar, alterar, excluir, consultar); entidades só lidas entram como adicionais | ±40% | triagem, orçamento inicial, comparação de alternativas |
| **E1 estimado** | lista de processos nomeados (backlog, histórias, menu), com tipo e entidades tocadas quando conhecidas | perfil típico por processo | ±25% | proposta, planejamento de release, contratação |
| **E2 detalhado** | modelo parcial: processos com movimentos conhecidos e lacunas marcadas como inferidas | o próprio modelo canônico, com `inferido` nas lacunas | ±10% | especificação em andamento; converge para a medição |

E0 e E1 são produzidos por `mfo.py estimar` a partir de um backlog; E2 é um modelo comum
com movimentos inferidos, produzido pela extração normal (capítulo 4) quando os artefatos
ainda estão incompletos. Nos três níveis o rótulo carrega o nível e o intervalo.

Correspondência com práticas de mercado: E1 equivale à Contagem Estimativa de Pontos de
Função do Guia STI (NESMA estimada: funções identificadas, complexidade padrão), e E0 à
contagem indicativa da NESMA (só arquivos lógicos). O COSMIC trata o tema como
"dimensionamento aproximado", com tamanhos médios por processo funcional, que é
exatamente o papel dos perfis típicos.

## 11.3 Perfis típicos padrão

Derivados da tabela de casos frequentes do capítulo 2. `P` é a entidade principal; cada
entidade adicional acrescenta os movimentos da última coluna.

| Tipo | Movimentos e desfechos base | PFO base | Por entidade adicional |
|---|---|---|---|
| criar | E P · R P (unicidade) · W P · D (recusa) | 4 | + R |
| alterar | E P · R P · W P · D (recusa) | 4 | + R |
| excluir | E P · W P · D (bloqueio) | 3 | + R (dependentes) |
| estado | E P · R P · W P · D (estado inválido) | 4 | + R |
| consultar | E P (filtros) · R P · X P | 3 | + R + X |
| relatório | E DISPARO · R P · X P | 3 | + R + X |
| processar | E DISPARO · R P · W P | 3 | + R |
| integrar | E P · R P · W P · D (rejeição) | 4 | + R |
| outro | E P · R P · W P · D (recusa) | 4 | + R |

O que os modelos medidos mostram sobre esses padrões: em 101 processos de três modelos
(Aval mecânico, biblioteca e Usuários revisado), a mediana é 6 PFO por processo e varia
de 5 a 8 conforme o tipo (processar 5, mudanças de estado 8, 9 no único relatório). O
tipo discrimina menos do que o número de entidades tocadas e de recusas distintas. Por
isso a entrada mais valiosa de um backlog é a lista de entidades de cada item, e por isso
a calibração local pesa mais do que a tabela.

## 11.4 Ferramenta e formato do backlog

```
python3 mfo.py perfis <modelos medidos...> -o perfis.json     # RE-02: PFO por tipo, com quartis
python3 mfo.py estimar <backlog.json> [--perfis perfis.json] [--medido modelo.json] [-o estimativa.mfc.json]
```

Backlog mínimo (E1):

```json
{
  "software": "Biblioteca", "nivel_estimativa": "E1",
  "fonte": { "id": "PROP", "tipo": "requisitos", "ref": "proposta comercial v0.3" },
  "itens": [
    { "id": "P06", "nome": "Registrar empréstimo", "entidades": ["Emprestimo", "Leitor", "Livro"], "ref": "item 2.4" },
    { "id": "P08", "nome": "Relatório de atrasos", "tipo": "relatorio", "entidades": ["Emprestimo", "Leitor", "Livro"] }
  ]
}
```

Para E0, um item `{ "entidade": "Livro", "crud": true }` expande-se nos quatro processos de
manutenção. A saída de `estimar` é um modelo canônico válido (todos os movimentos
inferidos), gravado com `-o`, que a extração posterior refina item a item; `--medido`
calcula o erro relativo contra um modelo medido do mesmo escopo.

## 11.5 Resultados nos exemplos

| Estimativa | Base de perfis | Resultado (intervalo) | Medido | Erro | Medido no intervalo |
|---|---|---|---|---|---|
| Biblioteca E0, 3 entidades mantidas | padrão | 52 (31 a 73) | 54 | 4% | sim |
| Biblioteca E1, 9 itens com entidades | padrão | 43 (32 a 54) | 54 | 20% | no limite |
| Biblioteca E1, 9 itens com entidades | calibrada, 101 processos | 56 (46 a 70) | 54 | 4% | sim |
| Aval E1, 85 features só pelo nome e entidade principal | padrão | 304 (228 a 380) | 542 | 44% | não |
| Aval E1, idem | calibrada em outros sistemas, 16 processos | 616 (433 a 873) | 542 | 14% | sim |
| Aval E1, idem | calibrada incluindo o próprio Aval (circular, só ilustra o mecanismo) | 544 (433 a 666) | 542 | 0% | sim |

Arquivos: [`biblioteca-backlog.json`](exemplos/biblioteca-backlog.json),
[`biblioteca-backlog-indicativo.json`](exemplos/biblioteca-backlog-indicativo.json),
[`aval/aval-backlog-E1.json`](exemplos/aval/aval-backlog-E1.json),
[`aval/perfis-calibrados.md`](exemplos/aval/perfis-calibrados.md) e os relatórios
`*-estimativa-*.md` ao lado de cada um.

Três leituras. A estimativa da biblioteca ficou dentro do intervalo nos três casos porque o
backlog listava as entidades de cada item; a E1 padrão encostou no limite porque o perfil
típico prevê uma recusa por processo e Registrar empréstimo tem quatro. A do Aval pelos
nomes, com só a entidade principal, subestimou em quase metade: os processos do Aval
tocam três ou quatro entidades e recusam por um ou dois códigos em média, e isso o nome
não diz. Com perfis calibrados em outros sistemas, ainda sem ler os N3, o intervalo
passou a conter o valor medido. A regra prática: peça as entidades tocadas e as recusas
previstas antes de pedir qualquer outra coisa, e calibre com o primeiro sistema medido.

## 11.6 Acompanhar a precisão

Cada estimativa com rótulo deve ser confrontada com a medição quando o artefato existir
(`--medido`). O erro relativo por nível, acumulado em algumas dezenas de casos, substitui
os intervalos padrão pelos intervalos observados na organização, e a tabela de perfis é
regenerada com `perfis` a cada novo modelo medido. Uma estimativa que erra sempre para o
mesmo lado indica perfil desatualizado ou backlog sem entidades, não um defeito do
estimador.

## 11.7 Onde entra na esteira do Aval

| Etapa | Insumo disponível | Nível MFO |
|---|---|---|
| Triagem | texto da demanda e features impactadas | E0 ou E1 pelo mapa de features |
| História de usuário | ações nomeadas por ator | E1 |
| N3 de negócio (3A) | campos, regras, entidades | E2, ou medição de nível R |
| N3 técnico (3B) | API, dados lidos e gravados, memória de cálculo | medição de nível R |
| Código entregue | repositório | medição de nível C e aderência R × C |

A estimativa de triagem é o que a APF não consegue dar cedo: a Contagem Estimativa exige
identificar arquivos lógicos e transações classificadas, o que só existe no 3B. Com a MFO,
o mapa de features impactadas da triagem já produz um E1 com intervalo, e a análise de
impacto de uma sprint pode ser estimada como `mudança`: features novas pelo perfil
inteiro, features alteradas por um movimento alterado por entidade tocada, até que a
extração substitua a inferência.
