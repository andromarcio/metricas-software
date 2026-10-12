# PFC — Pontos de Função Caixa · Versão 1.0

Especificação de uma métrica de tamanho funcional de software projetada para três
exigências simultâneas: ser **objetiva** (duas medições do mesmo software, feitas por
pessoas ou por IAs diferentes, devem chegar ao mesmo número ou a divergências
localizáveis), ser **aplicável por IA** (o resultado é um modelo verificável, não uma
opinião) e permitir **comparação entre softwares** feitos em qualquer linguagem ou
tecnologia.

A unidade de medida leva o nome do método: o **PFC**. Um PFC corresponde a uma
movimentação de dados entre o software e seus usuários funcionais ou entre o software e
seu armazenamento persistente, ou a um desfecho distinto que um processo devolve.

> Posição em relação aos métodos já documentados neste repositório: o PFC herda da
> [APF/IFPUG](../APF/README.md) o foco na visão do usuário e na unidade de processo
> elementar, e do [COSMIC](../COSMIC/README.md) o primitivo de medição (a movimentação
> de dados, sem pesos de complexidade). O que ele acrescenta é a separação rígida entre
> *interpretar* (produzir um modelo com evidências) e *calcular* (uma função
> determinística sobre esse modelo), que é o que torna a medição auditável e automatizável.

---

## A métrica em uma página

| Elemento | Definição resumida |
|---|---|
| **Fronteira** | Linha conceitual entre o software medido e o resto do mundo. Dentro dela está o armazenamento persistente do software. |
| **Usuário funcional (UF)** | Quem envia ou recebe dados através da fronteira: pessoa, sistema externo, dispositivo ou relógio. |
| **Entidade** | Grupo nomeado de atributos que descreve uma única coisa de interesse do negócio, persistida ou trocada como unidade. |
| **Processo** | Menor unidade de funcionalidade com disparador identificável, efeito observável (saída ou gravação) e autonomia (deixa o software em estado consistente). |
| **Movimento** | Deslocamento de **uma** entidade em um processo. Quatro tipos: **E** (entra de um UF), **X** (sai para um UF), **R** (lida do armazenamento), **W** (gravada no armazenamento). |
| **Desfecho** | Resultado distinto que o processo devolve ao UF, além do principal: cada recusa, erro de negócio ou variante de sucesso com código ou mensagem próprios. |
| **Evidência** | Referência a um artefato (requisito, tela, endpoint, função, tabela) que sustenta cada processo e cada movimento. |
| **Rótulo** | Identificação obrigatória do resultado: versão do método, nível de medição, grau de evidência, agente e escopo. |

**Regra de contagem única:** cada movimento distinto (processo, tipo, entidade) e cada
desfecho distinto além do principal valem **1 PFC**. O tamanho do software é a soma dos
movimentos e desfechos de todos os seus processos. Não há pesos, tabelas de complexidade
nem fatores de ajuste.

**Uma entidade reservada:** `DISPARO` (sinal de disparo sem dados, como o tique de um
relógio). Mensagens de erro, sucesso ou estado não são movimentos: são desfechos.

**Tamanho de uma mudança:** movimentos incluídos + alterados + excluídos entre o modelo
anterior e o posterior, calculado por diferença de chaves. Em código, o diff entre duas
versões delimita o que reextrair e prova o que mudou; cada movimento cita arquivo e
trecho verificáveis por máquina.

**Decisões dentro do tamanho:** o que um processo decide entra na conta pelo que ele
devolve de diferente: um desfecho por código ou mensagem. Um autorizador de cartão com 17
códigos de recusa e um aceite de convite com três movem um número parecido de entidades
e medem 29 e 14 PFC. Dez validações sob o mesmo código valem um: o que a fronteira não
distingue não é função.

**Estimativa:** uma estimativa é o mesmo modelo com movimentos inferidos por perfis típicos,
rotulada por nível (E0 indicativo, E1 estimado, E2 detalhado) e sempre com intervalo; o
grau de evidência diz quanto ainda é estimativa e o número converge para a medição.

**Produção com IA:** o tamanho não depende de quem produziu (princípio P8). O modelo
registra, por processo, o modo de produção (M0 humano, M1 IA assistida, M2 IA dirigida,
M3 IA autônoma) com evidência, e o aceite; o relatório traz PFC por modo, PFC aceitos,
PFC por hora humana e custo por PFC, que é o que um contrato precisa para repreçar.

**Objetividade operacional:** o modelo só produz tamanho se passar nas validações
V-01 a V-11; a concordância entre duas medições independentes é medida (índice de
concordância) e as divergências são resolvidas por regra e evidência, nunca por opinião.

---

## Sumário

- [1. Motivação e princípios de projeto](01-motivacao-e-principios.md)
- [2. Modelo Funcional Canônico — conceitos e regras de identificação (RI-01 a RI-12)](02-modelo-funcional-canonico.md)
- [3. Regras de contagem, validação e mudança (RC-01 a RC-06, V-01 a V-11)](03-regras-de-contagem.md)
- [4. Medição assistida por IA — protocolo, concordância e salvaguardas](04-medicao-assistida-por-ia.md)
- [5. Comparação entre softwares — perfil funcional, indicadores e relação com APF e COSMIC](05-comparacao-entre-softwares.md)
- [6. Exemplo completo — sistema de biblioteca medido de ponta a ponta](06-exemplo-completo.md)
- [7. Glossário](07-glossario.md)
- [8. Medição a partir do código e do diff (RD-01 a RD-04)](08-medicao-a-partir-do-codigo-e-do-diff.md)
- [9. Medindo a produção com IA (RP-01 a RP-04)](09-producao-com-ia.md)
- [10. Exemplo real: a documentação do Aval (siesa-doc) e a estrutura do siesa-engine (RM-01 a RM-08)](10-exemplo-real-aval.md)
- [11. Estimativa (RE-01 a RE-04)](11-estimativa.md)
- [12. Desfechos: a decisão dentro do tamanho (RI-12, RC-05)](12-decisoes.md)

### Artefatos de apoio

| Artefato | Caminho | Uso |
|---|---|---|
| Esquema JSON do Modelo Funcional Canônico | [`schema/mfc.schema.json`](schema/mfc.schema.json) | Validação estrutural por ferramentas e por IAs |
| Ferramenta de referência | [`ferramentas/pfc.py`](ferramentas/pfc.py) | `validar`, `contar`, `mudanca`, `concordancia`, `impacto`, `auditar`, `perfis`, `estimar` (Python 3.8+, sem dependências) |
| Extrator para a estrutura N3 do siesa-engine | [`ferramentas/extrair_n3.py`](ferramentas/extrair_n3.py) | Modelo mecânico a partir de `modules/**/f-*.md`, com produção pelo git e marcação de alterados |
| Prompt de extração para IA | [`prompts/extracao-mfc.md`](prompts/extracao-mfc.md) | Produzir o modelo a partir de requisitos ou código |
| Exemplo: biblioteca v1 | [`exemplos/biblioteca-v1.mfc.json`](exemplos/biblioteca-v1.mfc.json) | Modelo completo (54 PFC) |
| Exemplo: biblioteca v2 | [`exemplos/biblioteca-v2.mfc.json`](exemplos/biblioteca-v2.mfc.json) | Medição de mudança (9 PFC de mudança) |
| Exemplo: segunda medição da v1 | [`exemplos/biblioteca-v1-medicao-B.mfc.json`](exemplos/biblioteca-v1-medicao-B.mfc.json) | Índice de concordância entre medições |
| Exemplo: código da biblioteca, v1 e v2 | [`exemplos/codigo-biblioteca/`](exemplos/codigo-biblioteca/README.md) | Medição por diff, auditoria de evidências e testes de aceitação por processo |
| Exemplo real: Aval (siesa-doc) | [`exemplos/aval/`](exemplos/aval/) | 542 PFC mecânicos, PFC × PF, mudança entre versões, concordância mecânico × revisado, perfis calibrados e estimativa E1 |
| Exemplo: estimativas da biblioteca | [`exemplos/biblioteca-backlog.json`](exemplos/biblioteca-backlog.json), [`exemplos/biblioteca-backlog-indicativo.json`](exemplos/biblioteca-backlog-indicativo.json) | E1 por backlog e E0 por entidades, comparadas aos 54 PFC medidos |
| Exemplo: autorizador de cartão (hipotético) | [`exemplos/cartao/`](exemplos/cartao/autorizacao-requisitos.md) | 29 PFC num processo só: 12 movimentos e 17 códigos de recusa; seis regras de fraude sob um código único contam um |

### Uso rápido

```bash
python3 PFC/ferramentas/pfc.py validar PFC/exemplos/biblioteca-v1.mfc.json
python3 PFC/ferramentas/pfc.py contar   PFC/exemplos/biblioteca-v1.mfc.json
python3 PFC/ferramentas/pfc.py mudanca  PFC/exemplos/biblioteca-v1.mfc.json PFC/exemplos/biblioteca-v2.mfc.json
python3 PFC/ferramentas/pfc.py concordancia PFC/exemplos/biblioteca-v1.mfc.json PFC/exemplos/biblioteca-v1-medicao-B.mfc.json
python3 PFC/ferramentas/pfc.py impacto  PFC/exemplos/biblioteca-v1.mfc.json --dirs PFC/exemplos/codigo-biblioteca/v1 PFC/exemplos/codigo-biblioteca/v2
python3 PFC/ferramentas/pfc.py auditar  PFC/exemplos/biblioteca-v2.mfc.json --raiz PFC/exemplos/codigo-biblioteca --fonte COD --fonte TST
python3 PFC/ferramentas/pfc.py perfis   PFC/exemplos/biblioteca-v1.mfc.json PFC/exemplos/aval/adm-usr-revisado.mfc.json -o /tmp/perfis.json
python3 PFC/ferramentas/pfc.py estimar  PFC/exemplos/biblioteca-backlog.json --perfis /tmp/perfis.json --medido PFC/exemplos/biblioteca-v1.mfc.json
```

### Como citar um resultado

Todo tamanho PFC deve ser apresentado com o rótulo completo, por exemplo:

```
54 PFC · PFC 1.0 · nível RC · evidência 100% · agente: IA + revisão humana · escopo: Biblioteca v1.0 (RF-01 a RF-09)
```

Tamanhos sem rótulo, ou com níveis de medição diferentes, não devem ser comparados.

### Estado da especificação

Versão 1.0, proposta inicial. As regras foram escritas para serem testadas em campo:
cada regra de identificação tem forma de teste de decisão, e a seção 5.5 lista o que a
métrica deliberadamente não mede. O capítulo 10 aplica o método a um sistema real.
Sugestões de mudança devem apontar a regra afetada (RI, RC, RD, RP, RM, RE ou V) e um
caso concreto em que ela produza resultado ambíguo.
