# 10. Exemplo real: a documentação do Aval (siesa-doc) e a estrutura do siesa-engine

> PFC — Pontos de Função Caixa · Versão 1.0

O capítulo aplica o PFC a um sistema real: o **Aval**, plataforma de geração de sistemas
com agentes de IA, cuja documentação vive no repositório `siesa-doc` e é produzida pelo
kit `siesa-engine` (prompts, templates e validadores). A pergunta respondida é dupla:
**a estrutura N3 do engine sustenta a contagem PFC?** e **o que sai quando se mede de
verdade?** Todos os artefatos estão em [`exemplos/aval/`](exemplos/aval/) e são
reproduzíveis com `ferramentas/extrair_n3.py` sobre um checkout do `siesa-doc`.

## 10.1 A estrutura N3 vista pelo PFC

Cada feature N3 (`modules/<domínio>/<feature set>/f-<verbo>-<entidade>.md`) é, pela
definição do engine, "uma ação de negócio com disparador, começo, meio, fim e resultado
observável". É quase exatamente a definição de processo do PFC (RI-04). As seções do N3
mapeiam-se para o modelo canônico assim:

| Seção do N3 (siesa-engine) | Conceito PFC | Regra de mapeamento |
|---|---|---|
| front-matter `id`, `entidade`, `endpoints`, `error_codes` | identidade do processo, entidade principal, disparador, desfechos | RM-01 |
| `## Superfície` e `## Eventos › Consumidos` | usuário funcional e evento disparador | RM-01: ação em tela ou tela própria = pessoa; webhook ou evento consumido = sistema; rotina = relógio |
| `## Campos` (coluna Entidade, Preenchimento) | movimentos E, por entidade | RM-02: um E por entidade com "entrada do usuário"; `lista de opções` de outra entidade vira R + X dela |
| `## Dados lidos e gravados` (Entidade, Papel) | R e W | RM-03: lê = R, grava = W |
| `### Memória de cálculo` (`alr` por processo elementar e "por que cada ALR") | R e W quando a seção anterior falta | RM-04: EE mantém a entidade principal (W) e lê as demais (R); SE e CE leem todas; sistema externo (AIE) acessado por chamada = E |
| `## API` (resposta 2xx) e `## Colunas do resultado` | X | RM-05: consulta devolve X da entidade principal; EE devolve X quando a resposta traz `data` |
| tabela de erros da `## API` e `error_codes` do front-matter | desfechos (RI-12) | RM-06: um desfecho por código de erro de negócio distinto; célula com dois códigos vale dois; códigos técnicos (`AUTH_*`, `INTERNAL*`…) não contam; recusa indicada só nos cenários vale um |
| `## Métricas de tamanho` (Papel principal ou acessório) | um processo por elementar principal; acessório = R + X dentro do processo | RM-07 (combobox, card e menu não são processos, RI-04 b) |
| `## Eventos › Publicados` | não conta: consumidores internos (RC-04 b) | RM-08 |

A tabela é implementada por [`ferramentas/extrair_n3.py`](ferramentas/extrair_n3.py),
um extrator determinístico (agente do tipo `ferramenta`): sem modelo de linguagem, sem
julgamento, saída idêntica a cada execução. Toda movimentação cita a seção de origem
(`DOC:<arquivo>#<seção>`) e a verificação mecânica é feita por `pfc.py auditar`.

Resposta à primeira pergunta: **sim, com uma ressalva**. A estrutura sustenta a
contagem, e grande parte dela de forma puramente mecânica; a ressalva é que três
seções do N3 carregam movimentos que o extrator não interpreta, e a seção 10.4 mede o
tamanho dessa lacuna.

## 10.2 O Aval inteiro, mecanicamente

`extrair_n3.py /caminho/siesa-doc --git` sobre o commit `49265a9` (VERSION 5.0.0,
2026-10-06): 77 arquivos N3 em 6 domínios, 85 processos, 20 entidades.

| Indicador | Valor |
|---|---|
| PFC (piso mecânico) | **542** |
| NP / NE | 85 / 20 |
| E / X / R / W / D | 101 / 84 / 157 / 76 / 124 |
| Densidade | 6,38 |
| Persistência / Interface | 0,43 / 0,57 |
| Disparadores | 60 por pessoa, 25 por sistema |
| Evidências verificadas (`auditar --fonte DOC`) | 769 de 769 |
| Modo de produção (heurística git) | M2 em 85 processos |

Rótulo: `542 PFC · PFC 1.0 · nível R · evidência 100% · agente: ferramenta (extrair_n3.py 1.0); sem revisão humana · escopo: Aval (siesa-doc) 5.0.0, todos os domínios`.

O número é um **piso**: o que a estrutura declara explicitamente. Dos 542 PFC, 124 são
desfechos, um por código da tabela de erros de cada N3: é a parte mais mecânica da
contagem, porque já nasce em tabela. Um único movimento é inferido: um processo elementar
secundário sem saída nem gravação declaradas, para o qual o extrator presume a saída da
entidade principal (RI-04 T2). O relatório completo está em
[`relatorio-aval-5.0.0.md`](exemplos/aval/relatorio-aval-5.0.0.md); os 21 avisos V-09 são
pares de processos de mudança de estado (desativar e reativar, por exemplo) que têm as
mesmas chaves e são legitimamente distintos (RI-04 a).

A atribuição de produção pelo git (RP-01, heurística: maioria dos commits do arquivo com
trailer de coautoria de IA) classifica todos os N3 como M2, IA dirigida: o `siesa-doc`
é escrito por agentes e aprovado por pessoas nos gates registrados no front-matter de
cada feature. É um caso em que a própria especificação é produto de IA, e o PFC mede isso
sem alterar o tamanho.

## 10.3 PFC × PF: a contagem APF existente

Os N3 carregam, na seção `## Métricas de tamanho`, a contagem APF da equipe (CPM 4.3.1,
com memória de cálculo). Cruzando as duas medidas por domínio
([`pfc-vs-pf-aval-5.0.0.md`](exemplos/aval/pfc-vs-pf-aval-5.0.0.md)):

| Domínio | Processos | PFC (mecânico) | PF (N3) | PFC/PF |
|---|---|---|---|---|
| ADM Administração | 24 | 171 | 117 | 1,46 |
| AGT Agentes | 12 | 59 | 68 | 0,87 |
| DEM Demandas | 6 | 40 | 31 | 1,29 |
| EST Esteira | 21 | 149 | 106 | 1,41 |
| OPE Operação | 8 | 46 | 31 | 1,48 |
| SIS Sistemas | 14 | 77 | 69 | 1,12 |
| **Total** | **85** | **542** | **422** | **1,28** |

Leitura: as duas medidas andam juntas (a razão fica entre 0,87 e 1,48 por domínio), e
onde divergem a razão é explicável pelo primitivo: Agentes tem processos com poucos
movimentos, sem tabela de erros e com DER altos (uma execução que grava um resultado
grande), onde a APF pesa mais; Administração, Esteira e Operação têm processos que tocam
muitas entidades (perfil, auditoria, conta, pessoa) e recusam por vários códigos, onde
cada entidade e cada código é uma unidade no PFC e apenas um ALR ou um DER na APF. A APF
do sistema soma ainda 73 PF de funções de dados (10 ALIs), que o PFC não conta
diretamente.

## 10.4 Extração mecânica × leitura com as regras

Para medir a lacuna da extração mecânica, o feature set **Usuários** (ADM-USR, 6 N3) foi
medido duas vezes: pelo extrator e por leitura dos N3 aplicando RI-01 a RI-12
([`adm-usr-auto.mfc.json`](exemplos/aval/adm-usr-auto.mfc.json) e
[`adm-usr-revisado.mfc.json`](exemplos/aval/adm-usr-revisado.mfc.json); ambos com 100%
das evidências verificadas contra o repositório).

| Medição | Processos | PFC | APF (N3) |
|---|---|---|---|
| Extrator (`ferramenta`) | 6 | 44 | 34 PF |
| Leitura com as regras (`ia`) | 7 | 64 | |
| Índice de concordância | | **0,588** (40 chaves comuns de 68) | |

As 28 chaves divergentes ([`concordancia-adm-usr.md`](exemplos/aval/concordancia-adm-usr.md))
concentram-se em quatro padrões, todos sustentados por texto do N3 que o extrator não lê:

| Padrão | Chaves | Onde está no N3 | Regra PFC |
|---|---|---|---|
| Leitura para decidir uma regra ("ao menos um Administrador ativo", "e-mail não pode ser de usuário ativo") | R Usuario em 4 processos | `## Regras de negócio` | RI-07 b |
| Trilha de auditoria gravada em cada ação | W EventoAuditoria em 5 processos | `## Campos automáticos` ("Registro de auditoria") e `## Eventos` | RI-08 c |
| Nome de entidade referenciada na resposta (nome do perfil, da organização) | X Perfil, X Conta | corpo da resposta em `## API` | RI-06 a |
| Consulta do convite pelo código como processo próprio (disparador distinto, resultado válido sozinho) | processo ADM-USR-06b | `## Métricas de tamanho` marca como acessório | RI-04 T3 |

Os desfechos quase não divergem: 13 no extrator contra 14 na leitura, e a diferença é o
processo de consulta do convite, que a mecânica funde ao aceite. A tabela de erros do
N3 é fonte fechada; os movimentos é que dependem de prosa.

Duas conclusões. A primeira é sobre o extrator: ele é um piso confiável e auditável
(nenhuma chave inventada; as 4 chaves só dele são leituras e saídas que a memória de
cálculo registra para o acessório fundido), mas captura cerca de dois terços das
chaves. A segunda é sobre o engine, e é a mais útil: as lacunas são **estruturais**, não
de redação. Três mudanças no template N3 tornariam a contagem PFC integralmente
mecânica:

1. `## Dados lidos e gravados` obrigatória em toda feature, hoje presente em 17 das 77,
   com o papel `lê` registrando também leituras feitas **para validar regra**;
2. uma tabela de **saídas por entidade** (quais entidades têm atributos na resposta ou na
   tela), em vez de inferir do JSON de exemplo;
3. o registro de auditoria declarado como gravação da entidade `EventoAuditoria`, e não
   apenas como evento publicado.

Com isso, a memória de cálculo APF e o modelo PFC passariam a ser gerados da mesma fonte,
e a concordância entre extração mecânica e leitura tenderia a 1.

## 10.4a Desfechos no Aval

A tabela de erros da `## API` rende, no Aval 5.0.0, 124 desfechos em 67 dos 85
processos: mediana de 1 por processo, máximo de 4, 1,5 na média. Os processos sem
desfecho são os de Agentes (execuções internas, sem tabela de erros) e os elementares
secundários. Uma linha com dois códigos ("`DEMANDA_FEATURE_NOT_APPROVED` ·
`VALIDATION_ERROR`") vale dois; uma situação com duas causas sob o mesmo código
("usuário ou perfil fora da conta") vale um, porque a fronteira devolve o mesmo código
(RI-12 b). Em Usuários, 13 desfechos mecânicos contra 14 da leitura revisada. Ao contrário
dos movimentos, os desfechos já nascem em tabela no N3, e a mecânica quase não perde nada.

## 10.5 Mudança entre duas versões da documentação

O `siesa-doc` tem histórico suficiente para medir uma mudança real: entre o commit
`10b547b` (17 de julho de 2026, VERSION 1.23.1, 58 N3) e o `49265a9` (6 de outubro,
VERSION 5.0.0, 77 N3). O extrator foi aplicado às duas versões, com `--antes` marcando
como alterado todo movimento cuja seção de origem mudou (aproximação da RD-01 em nível
de seção). Saída de `pfc.py mudanca` ([`mudanca-aval-1.23.1-para-5.0.0.md`](exemplos/aval/mudanca-aval-1.23.1-para-5.0.0.md)):

```
397 PFC de mudança (263 incluídos, 102 alterados, 32 excluídos) · PFC 1.0 · nível R · evidência 99% · agente: ferramenta (extrair_n3.py 1.0)
Tamanho anterior: 311 PFC · tamanho posterior: 542 PFC · níveis: R → R
Processos novos: 24 · processos removidos: nenhum
```

A evidência de 99% vem dos oito processos da versão de julho sem saída nem gravação
declaradas, cuja saída o extrator presume (um movimento inferido cada); na versão de
outubro os N3 passaram a declará-las.

O `pfc.py impacto` com as duas referências git
([`impacto-aval-1.23.1-para-5.0.0.md`](exemplos/aval/impacto-aval-1.23.1-para-5.0.0.md))
mostra o outro lado: 375 arquivos mudaram, todos os 61 processos de julho foram tocados
(14 com trecho citado alterado, 47 apenas com arquivo alterado, porque o front-matter de
gates de cada N3 mudou), e 142 arquivos novos sem processo associado, onde estão as 24
features novas. É o comportamento esperado em três meses de evolução intensa; em uma
sprint, a lista de afetados é curta e a reextração dirigida custa minutos.

A marcação de alterado por seção superestima: uma mudança de texto em `## API` marca
todos os E e X do processo. Em uso contratual, o passo de extração dirigida (seção 8.3)
confirma cada candidato pela RD-01. Aqui o número serve para mostrar a mecânica e a
ordem de grandeza.

## 10.6 O que o exemplo real ensina

- **A unidade é reconhecível em uma estrutura de documentação madura** sem medidor
  certificado e sem planilha: 542 PFC, 769 evidências verificadas, em segundos.
- **O piso mecânico e a leitura com regras têm papéis diferentes.** O piso serve para
  acompanhar evolução, detectar escopo e comparar versões com custo zero; a leitura
  serve para contrato. A concordância entre os dois mede a maturidade da documentação.
- **A APF existente e o PFC se explicam mutuamente.** As razões por domínio não são
  ruído: apontam onde um método pesa dados e o outro pesa movimentos.
- **Produção por IA fica visível sem mudar o tamanho.** O `siesa-doc` é 100% M2 pelo
  git; a mesma mecânica se aplica ao código gerado a partir dele.
- **O engine ganha com três ajustes no template** (seção 10.4), que também beneficiam a
  própria contagem APF: a memória de cálculo passa a nascer de tabelas, não de prosa.

## 10.7 Reproduzindo

```bash
# modelo mecânico da versão atual, com modo de produção pelo git
python3 PFC/ferramentas/extrair_n3.py /caminho/siesa-doc --git -o aval-atual.mfc.json
python3 PFC/ferramentas/pfc.py contar aval-atual.mfc.json
python3 PFC/ferramentas/pfc.py auditar aval-atual.mfc.json --raiz /caminho/siesa-doc --fonte DOC

# versão anterior (exportada do git) e mudança
git -C /caminho/siesa-doc archive 10b547b modules global VERSION | tar -x -C /tmp/siesa-doc-jul
python3 PFC/ferramentas/extrair_n3.py /tmp/siesa-doc-jul -o aval-jul.mfc.json
python3 PFC/ferramentas/extrair_n3.py /caminho/siesa-doc --git --antes /tmp/siesa-doc-jul -o aval-atual.mfc.json
python3 PFC/ferramentas/pfc.py mudanca aval-jul.mfc.json aval-atual.mfc.json
python3 PFC/ferramentas/pfc.py impacto aval-jul.mfc.json --git /caminho/siesa-doc 10b547b 49265a9 --fonte DOC

# um feature set, mecânico × revisado
python3 PFC/ferramentas/extrair_n3.py /caminho/siesa-doc --escopo ADM-USR -o adm-usr-auto.mfc.json
python3 PFC/ferramentas/pfc.py concordancia adm-usr-auto.mfc.json PFC/exemplos/aval/adm-usr-revisado.mfc.json
```
