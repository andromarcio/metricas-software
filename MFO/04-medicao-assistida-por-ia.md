# 4. Medição assistida por IA

> MFO — Medição Funcional Objetiva · Versão 1.0

## 4.1 Por que a MFO funciona com IA

Um modelo de linguagem é bom em ler artefatos heterogêneos (requisitos, telas, código em
qualquer linguagem, esquemas de banco, contratos de API) e extrair deles uma estrutura.
É ruim em ser consistente de uma execução para outra e em distinguir o que leu do que
supôs. A MFO foi desenhada em torno disso:

| Risco com IA | Salvaguarda na MFO |
|---|---|
| A IA conta de um jeito hoje e de outro amanhã | A IA não conta. Ela produz o modelo; a ferramenta conta (P3). |
| A IA inventa um processo ou uma entidade | Todo elemento exige evidência localizável (RI-11, V-07); o grau de evidência vai no rótulo. |
| A IA fragmenta demais (cada tela vira processo) ou de menos (um módulo vira processo) | Testes T1 a T3 de RI-04 e desempates fixos; V-09 aponta processos possivelmente duplicados. |
| A IA confunde dados técnicos com entidades | RI-03 c e d, RI-10. |
| A IA esquece mensagens, disparadores ou leituras de validação | V-02, V-03 e a tabela de casos frequentes (seção 2.5). |
| Ninguém sabe se a medição é reproduzível | Segunda medição independente e índice de concordância (seção 4.4). |

## 4.2 Protocolo

```
 1. Preparar      2. Extrair          3. Validar e contar    4. Segunda medição   5. Conciliar      6. Rotular e arquivar
 artefatos  ───▶  modelo (IA)   ───▶  mfo.py validar   ───▶  modelo B (IA ou  ───▶ divergências ───▶ relatório + modelo
 e escopo         com evidências      mfo.py contar          humano)               por regra         versionados
```

**Passo 1 — Preparar.** Declarar propósito, escopo, nível (R, C ou RC) e fontes com
versão (commit, versão do documento). Listar previamente os usuários funcionais e, se
possível, um glossário de entidades com os nomes que o modelo deve usar. Isso reduz
divergências de nomenclatura entre medições.

**Passo 2 — Extrair.** Executar o prompt de extração ([`prompts/extracao-mfc.md`](prompts/extracao-mfc.md))
com os artefatos. A saída é o modelo JSON. Para bases de código grandes, extrair por
módulo ou por conjunto de pontos de entrada e consolidar em um único modelo (RC-04).

**Passo 3 — Validar e contar.** `mfo.py validar` deve retornar zero erros; corrigir o
modelo (não o número) até que retorne. `mfo.py contar` gera o relatório.

**Passo 4 — Segunda medição.** Repetir o passo 2 com outro agente (outro modelo de IA,
outra configuração, ou um medidor humano) sem acesso ao primeiro modelo, reutilizando o
glossário de entidades do passo 1.

**Passo 5 — Conciliar.** `mfo.py concordancia` lista as divergências por processo e
movimento. Cada divergência é resolvida citando a regra (RI-xx) e a evidência. O modelo
conciliado recebe nível e agente adequados.

**Passo 6 — Rotular e arquivar.** O modelo e o relatório são versionados junto do
software (por exemplo em `medicao/<versao>.mfc.json`). O modelo da versão anterior é o
insumo da medição de mudanças (RC-03).

Medições de rotina (uma sprint, uma demanda) podem omitir os passos 4 e 5 quando a
organização já tem histórico de concordância alta para aquele software e aquele agente.
Medições com efeito contratual não devem omiti-los.

## 4.3 Entradas por nível e mapeamento a partir de código

Em nível R, a IA trabalha com requisitos, histórias, casos de uso, protótipos e contratos
de API. Em nível C, trabalha com o repositório. A tabela indica onde estão os conceitos
nas tecnologias mais comuns; ela é orientação, não regra: a regra continua sendo RI-04 a
RI-09.

| Tecnologia | Processo (disparador) | E | X | R / W |
|---|---|---|---|---|
| API REST / GraphQL / gRPC | rota ou operação exposta | parâmetros e corpo | corpo da resposta; chamadas a outros serviços | repositórios, ORM, SQL, drivers |
| Aplicação web ou mobile com backend | ação do usuário que chega ao backend | formulário, payload | resposta renderizada ou JSON | idem |
| Aplicação desktop ou mobile local | ação do usuário que executa lógica | campos da tela | tela, arquivo, impressão | banco local, arquivos |
| Linha de comando | subcomando | argumentos, stdin, arquivos de entrada | stdout, arquivos de saída | arquivos, banco |
| Batch / ETL | job agendado ou acionado | `DISPARO` ou parâmetros; arquivos lidos de sistemas externos | arquivos gerados, chamadas | tabelas lidas e gravadas |
| Mensageria / eventos | consumidor de tópico ou fila | mensagem consumida | mensagens publicadas | idem |
| Embarcado / tempo real | interrupção, tique, sinal de sensor | leitura de sensor, comando | comando a atuador, telemetria | memória persistente, configuração de negócio |
| Serverless / funções | gatilho da função | evento recebido | resposta, chamadas | idem |

O capítulo 8 detalha a medição a partir do código e do diff entre duas versões. Regras
práticas para código:

- Um **ponto de entrada acessível a um usuário funcional** é candidato a processo. Funções
  internas, utilitárias e de framework não são.
- A **entidade** é identificada pela tabela, coleção, classe de domínio ou tipo de mensagem,
  nunca pelo nome da tela ou do DTO (RI-03 a).
- **R e W** são identificados nos acessos a persistência alcançáveis a partir do ponto de
  entrada, não apenas nos escritos no handler.
- Caminhos de erro geram **uma** X `MENSAGEM` por processo, por mais numerosos que sejam.
- Código morto, feature flags desligadas e endpoints internos de saúde ou métricas são
  excluídos (RI-10).

## 4.4 Concordância e revisão

> **Índice de concordância**
>
> Dados dois modelos do mesmo software, C = |K_A ∩ K_B| / |K_A ∪ K_B|, em que K é o
> conjunto de chaves (processo, tipo, entidade) de cada modelo, com processos pareados
> por `id` ou, na falta dele, por nome normalizado. C varia de 0 a 1.

Interpretação sugerida:

| C | Leitura | Ação |
|---|---|---|
| ≥ 0,90 | medições equivalentes | conciliar as poucas divergências e rotular |
| 0,75 a 0,89 | divergência localizada | revisar os processos divergentes; verificar glossário de entidades |
| < 0,75 | interpretação diferente do escopo ou da fronteira | revisar o passo 1 antes de nova extração |

Cada divergência é fechada com um registro de três partes: a chave divergente, a regra
aplicável e a evidência que decide. Exemplo: "P03 R Livro — RI-07 b: a exclusão não usa
atributos de Livro, apenas verifica dependentes em Empréstimo; não conta". Esses registros
formam, com o tempo, a base de exemplos da organização e realimentam o prompt.

## 4.5 Salvaguardas adicionais

- **Evidência verificável por amostragem.** Em revisões humanas, sortear uma fração dos
  movimentos e abrir as evidências. Evidência que não leva ao elemento invalida o
  movimento (passa a inferido) e sinaliza o agente.
- **Nunca editar o número.** Toda correção é feita no modelo; a ferramenta recalcula.
- **Prompt versionado.** O texto do prompt e a identificação do modelo de IA fazem parte
  do rótulo (`agente`). Mudar o prompt é mudar o agente.
- **Nível declarado.** Uma IA que leu código e inferiu requisitos produz nível C, não RC.
  RC exige que as duas fontes tenham sido lidas e conciliadas.

## 4.6 Ferramenta de referência

`ferramentas/mfo.py` é a implementação de referência das regras RC-01 a RC-06 e V-01 a
V-09. Não tem dependências externas.

```
python3 mfo.py validar <modelo.json>                 # lista erros e avisos; código de saída 1 se houver erro
python3 mfo.py contar <modelo.json> [--json]         # relatório com rótulo, perfil, produção e tabela por processo
python3 mfo.py mudanca <antes.json> <depois.json>    # tamanho da mudança (RC-03), por modo de produção
python3 mfo.py concordancia <a.json> <b.json>        # índice de concordância e divergências por processo
python3 mfo.py impacto <modelo.json> --dirs A B      # processos afetados por um diff (ou --git REPO REF_A REF_B)
python3 mfo.py auditar <modelo.json> --raiz DIR      # confere que cada evidência de código existe (RD-03)
python3 mfo.py perfis <modelos...> -o perfis.json    # PFO típico por tipo de processo (RE-02)
python3 mfo.py estimar <backlog.json> [--perfis P]   # estimativa E0/E1 como modelo com movimentos inferidos (RE-01)
```

O extrator `extrair_n3.py` (capítulo 10) produz modelos a partir da estrutura de
documentação do siesa-engine sem modelo de linguagem; é um exemplo de agente do tipo
`ferramenta`.

Qualquer outra implementação é conforme se, para todo modelo válido, produzir o mesmo
tamanho, o mesmo perfil e as mesmas validações da ferramenta de referência.
