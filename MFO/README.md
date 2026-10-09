# MFO — Medição Funcional Objetiva · Versão 1.0

Especificação de uma métrica de tamanho funcional de software projetada para três
exigências simultâneas: ser **objetiva** (duas medições do mesmo software, feitas por
pessoas ou por IAs diferentes, devem chegar ao mesmo número ou a divergências
localizáveis), ser **aplicável por IA** (o resultado é um modelo verificável, não uma
opinião) e permitir **comparação entre softwares** feitos em qualquer linguagem ou
tecnologia.

A unidade de medida é o **PFO — Ponto de Função Objetivo**. Um PFO corresponde a uma
movimentação de dados entre o software e seus usuários funcionais ou entre o software e
seu armazenamento persistente.

> Posição em relação aos métodos já documentados neste repositório: a MFO herda da
> [APF/IFPUG](../APF/README.md) o foco na visão do usuário e na unidade de processo
> elementar, e do [COSMIC](../COSMIC/README.md) o primitivo de medição (a movimentação
> de dados, sem pesos de complexidade). O que ela acrescenta é a separação rígida entre
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
| **Evidência** | Referência a um artefato (requisito, tela, endpoint, função, tabela) que sustenta cada processo e cada movimento. |
| **Rótulo** | Identificação obrigatória do resultado: versão do método, nível de medição, grau de evidência, agente e escopo. |

**Regra de contagem única:** cada movimento distinto (processo, tipo, entidade) vale **1 PFO**.
O tamanho do software é a soma dos movimentos de todos os seus processos. Não há pesos,
tabelas de complexidade nem fatores de ajuste.

**Duas entidades reservadas:** `MENSAGEM` (indicações de erro, sucesso ou estado, no máximo
uma X por processo) e `DISPARO` (sinal de disparo sem dados, como o tique de um relógio).

**Tamanho de uma mudança:** movimentos incluídos + alterados + excluídos entre o modelo
anterior e o posterior, calculado por diferença de chaves.

**Objetividade operacional:** o modelo só produz tamanho se passar nas validações
V-01 a V-09; a concordância entre duas medições independentes é medida (índice de
concordância) e as divergências são resolvidas por regra e evidência, nunca por opinião.

---

## Sumário

- [1. Motivação e princípios de projeto](01-motivacao-e-principios.md)
- [2. Modelo Funcional Canônico — conceitos e regras de identificação (RI-01 a RI-11)](02-modelo-funcional-canonico.md)
- [3. Regras de contagem, validação e mudança (RC-01 a RC-06, V-01 a V-09)](03-regras-de-contagem.md)
- [4. Medição assistida por IA — protocolo, concordância e salvaguardas](04-medicao-assistida-por-ia.md)
- [5. Comparação entre softwares — perfil funcional, indicadores e relação com APF e COSMIC](05-comparacao-entre-softwares.md)
- [6. Exemplo completo — sistema de biblioteca medido de ponta a ponta](06-exemplo-completo.md)
- [7. Glossário](07-glossario.md)

### Artefatos de apoio

| Artefato | Caminho | Uso |
|---|---|---|
| Esquema JSON do Modelo Funcional Canônico | [`schema/mfc.schema.json`](schema/mfc.schema.json) | Validação estrutural por ferramentas e por IAs |
| Ferramenta de referência | [`ferramentas/mfo.py`](ferramentas/mfo.py) | `validar`, `contar`, `mudanca`, `concordancia` (Python 3.8+, sem dependências) |
| Prompt de extração para IA | [`prompts/extracao-mfc.md`](prompts/extracao-mfc.md) | Produzir o modelo a partir de requisitos ou código |
| Exemplo: biblioteca v1 | [`exemplos/biblioteca-v1.mfc.json`](exemplos/biblioteca-v1.mfc.json) | Modelo completo (51 PFO) |
| Exemplo: biblioteca v2 | [`exemplos/biblioteca-v2.mfc.json`](exemplos/biblioteca-v2.mfc.json) | Medição de mudança (8 PFO de mudança) |
| Exemplo: segunda medição da v1 | [`exemplos/biblioteca-v1-medicao-B.mfc.json`](exemplos/biblioteca-v1-medicao-B.mfc.json) | Índice de concordância entre medições |

### Uso rápido

```bash
python3 MFO/ferramentas/mfo.py validar MFO/exemplos/biblioteca-v1.mfc.json
python3 MFO/ferramentas/mfo.py contar   MFO/exemplos/biblioteca-v1.mfc.json
python3 MFO/ferramentas/mfo.py mudanca  MFO/exemplos/biblioteca-v1.mfc.json MFO/exemplos/biblioteca-v2.mfc.json
python3 MFO/ferramentas/mfo.py concordancia MFO/exemplos/biblioteca-v1.mfc.json MFO/exemplos/biblioteca-v1-medicao-B.mfc.json
```

### Como citar um resultado

Todo tamanho MFO deve ser apresentado com o rótulo completo, por exemplo:

```
51 PFO · MFO 1.0 · nível RC · evidência 100% · agente: IA + revisão humana · escopo: Biblioteca v1.0 (RF-01 a RF-09)
```

Tamanhos sem rótulo, ou com níveis de medição diferentes, não devem ser comparados.

### Estado da especificação

Versão 1.0, proposta inicial. As regras foram escritas para serem testadas em campo:
cada regra de identificação tem forma de teste de decisão, e a seção 5.5 lista o que a
métrica deliberadamente não mede. Sugestões de mudança devem apontar a regra afetada
(RI-xx, RC-xx ou V-xx) e um caso concreto em que ela produza resultado ambíguo.
