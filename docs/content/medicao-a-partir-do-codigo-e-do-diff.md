<!-- Gerado por scripts/gera-docs.py a partir de MFO/08-medicao-a-partir-do-codigo-e-do-diff.md. Não edite: edite a fonte e gere de novo. -->
# 8. Medição a partir do código e do diff

> MFO — Medição Funcional Objetiva · Versão 1.0

A APF exige documentação de requisitos e um medidor treinado. A MFO em nível C dispensa
as duas coisas: o código é a fonte, o modelo é gerado a partir dele, e cada movimento
contado aponta para um arquivo e um trecho que qualquer pessoa pode abrir. Este capítulo
define como a unidade é reconhecida no código, como o diff entre duas versões delimita e
prova uma mudança, e como a medição é auditada por máquina.

## 8.1 O diff não é a medida, mas é a melhor evidência

Linhas de código não medem funcionalidade: variam com a linguagem, o estilo, o framework
e, cada vez mais, com a verbosidade da IA que as escreveu. Um diff de 2.000 linhas pode
ser uma refatoração de 0 PFO; um diff de 40 linhas pode acrescentar um processo de 9 PFO.
Por isso a MFO não conta o diff. Ela conta a diferença entre os **modelos funcionais** das
duas versões (RC-03) e usa o diff para duas coisas:

- **delimitar**: só os processos cujo código mudou precisam ser reextraídos; o custo da
  medição é proporcional à mudança, não ao tamanho do sistema;
- **provar**: cada movimento incluído, alterado ou excluído cita um trecho que está no
  diff. A auditoria consiste em abrir o diff e conferir.

## 8.2 Como a unidade aparece no código

Um movimento é um padrão sintático reconhecível em qualquer linguagem, sempre na
fronteira de um ponto de entrada:

| Movimento | O que procurar | Exemplos por tecnologia |
|---|---|---|
| Processo | ponto de entrada acessível a um usuário funcional | rota HTTP, handler de comando, consumidor de fila, job agendado, callback de dispositivo, subcomando de CLI, programa batch, procedimento exposto |
| E | dados que chegam ao ponto de entrada | parâmetros, corpo da requisição, mensagem consumida, arquivo lido de outro sistema, leitura de sensor, resposta de chamada externa que o processo usa |
| X | dados que saem para um usuário funcional | retorno ou resposta serializada, render de tela, chamada HTTP ou RPC de saída, mensagem publicada, arquivo gerado, comando a atuador, e-mail |
| R | leitura de persistência alcançável a partir do ponto de entrada | `SELECT`, `find`, `get`, `query`, leitura de arquivo, `EXEC SQL SELECT`, `READ` em COBOL, cursor em PL/SQL |
| W | escrita de persistência alcançável a partir do ponto de entrada | `INSERT`, `UPDATE`, `DELETE`, `save`, `persist`, escrita de arquivo, `WRITE`/`REWRITE`, `EXEC SQL INSERT` |
| Entidade | unidade de persistência ou de troca | tabela, coleção, documento, classe de domínio ou entidade do ORM, tipo de mensagem, layout de registro |
| MENSAGEM | caminhos de erro e confirmação do ponto de entrada | exceções de negócio mapeadas para resposta, códigos 4xx, mensagens de validação |

Regras de leitura do código:

> **RD-01 — Movimento alterado**
>
> Um movimento é alterado quando o código que o implementa está no diff **e** mudou o
> conjunto de atributos movimentados ou a manipulação associada (validação, cálculo,
> regra). Refatoração, renomeação, mudança de biblioteca, desempenho e correção que não
> alteram atributos nem manipulação **não** alteram o movimento: tamanho zero.

> **RD-02 — Movimento incluído ou excluído**
>
> a) Ponto de entrada novo alcançável por um usuário funcional é processo novo; todos os
>    seus movimentos são incluídos. Ponto de entrada removido ou tornado inalcançável
>    (inclusive por feature flag desligada em definitivo) é processo excluído.
>
> b) Movimento novo em processo existente (nova leitura, nova gravação, nova saída) é
>    incluído; movimento que deixa de existir é excluído.
>
> c) Código morto, código atrás de feature flag desligada e endpoints internos de saúde
>    ou métricas não entram no modelo (RI-10).

> **RD-03 — Evidência de código**
>
> a) Evidência de código tem a forma `FONTE:caminho#trecho`, em que `caminho` é relativo
>    à raiz declarada na fonte e `trecho` é um símbolo ou texto literal que existe no
>    arquivo (nome de função, rota, tabela, coluna, mensagem). Um sufixo `@versão` é
>    opcional.
>
> b) A evidência deve ser **verificável por máquina**: a ferramenta confere que o arquivo
>    existe e contém o trecho (`mfo.py auditar`). Evidência que não passa invalida o
>    movimento, que volta a inferido.

> **RD-04 — Mudança sem movimento**
>
> Manutenção corretiva, técnica, de plataforma e de desempenho tem tamanho zero em PFO e
> é tratada fora da métrica, por acordo contratual (como o Guia STI faz nas seções 4.4 a
> 4.8). O relatório de impacto registra que houve diff sem movimento, para que o
> trabalho fique visível sem inflar o tamanho.

## 8.3 Pipeline de medição por diff

```
 versão A (ref ou pasta)             versão B (ref ou pasta)
        │                                    │
        ▼                                    ▼
 modelo A (baseline) ─── mfo.py impacto ───▶ processos afetados, trechos mudados,
                           A → B             arquivos sem processo (entradas novas)
                                                      │
                                    extração só do que foi afetado (IA ou pessoa),
                                    com evidências em B e 'alterado' conforme RD-01
                                                      │
                                                      ▼
                                              modelo B  ──▶ mfo.py auditar (RD-03)
                                                      │
                 mfo.py mudanca A B ◀─────────────────┘
                   incluídos · alterados · excluídos · por modo de produção (cap. 9)
                                                      │
                                                      ▼
                                  modelo B arquivado como novo baseline
```

1. **Baseline.** Modelo da versão A, arquivado na medição anterior. Na primeira medição
   de um sistema legado, o modelo A é extraído do código inteiro uma única vez.
2. **Impacto.** `mfo.py impacto` cruza as evidências do modelo A com os arquivos do diff
   (dois diretórios ou duas referências git). Para cada processo diz se não foi afetado,
   se apenas um arquivo citado mudou, ou se o trecho citado mudou; lista os movimentos
   candidatos a alterado e os arquivos alterados que nenhum processo cita, onde podem
   estar pontos de entrada novos.
3. **Extração dirigida.** A IA (ou o medidor) reextrai apenas os processos afetados e
   procura processos novos nos arquivos sem processo. Candidatos a alterado são
   confirmados ou descartados pela RD-01.
4. **Auditoria.** `mfo.py auditar` confirma que toda evidência do modelo B existe no
   código da versão B.
5. **Mudança.** `mfo.py mudanca A B` conta incluídos, alterados e excluídos, por modo de
   produção quando declarado (capítulo 9).
6. **Arquivo.** O modelo B passa a ser o baseline. O histórico de modelos é o inventário
   funcional do sistema, versão a versão, sem documentação adicional.

Em código, a heurística de bloco da ferramenta delimita o trecho citado pela
indentação (funções em Python, Go, Java, JavaScript, C#, blocos em COBOL e SQL) e compara
as duas versões; é uma aproximação deliberadamente simples, e por isso o passo 3 confirma.

## 8.4 Auditoria

Uma medição MFO de nível C é auditável em três camadas, da mais barata para a mais cara:

| Camada | Pergunta | Como | Custo |
|---|---|---|---|
| Mecânica | Toda evidência existe no código? | `mfo.py auditar` | segundos |
| Amostral | As evidências sustentam os movimentos? | sortear movimentos e abrir os trechos; conferir tipo e entidade pelas regras RI | minutos por amostra |
| Independente | Outra extração chega ao mesmo modelo? | segunda extração e `mfo.py concordancia` | uma extração |

O modelo é o laudo: quem audita não precisa do medidor, só do código na versão citada e
das regras.

## 8.5 Exemplo: a biblioteca em código, v1 → v2

Os requisitos do capítulo 6 foram implementados em
[`exemplos/codigo-biblioteca/`](#/exemplo-codigo) (Python sem
dependências, uma função por processo). Os modelos
[`biblioteca-v1.mfc.json`](https://github.com/andromarcio/metricas-software/blob/main/MFO/exemplos/biblioteca-v1.mfc.json) e
[`biblioteca-v2.mfc.json`](https://github.com/andromarcio/metricas-software/blob/main/MFO/exemplos/biblioteca-v2.mfc.json) estão em nível RC, com
evidências de requisito (`REQ`), de código (`COD`, no formato RD-03) e de teste de
aceitação (`TST`, uma função de teste por processo).

**Impacto.** `mfo.py impacto biblioteca-v1.mfc.json --dirs codigo-biblioteca/v1 codigo-biblioteca/v2`:

```
Arquivos alterados: 5 (M 5, A 0, D 0) · fonte de evidências: COD

| Arquivo | Status | Linhas +/− | Processos e entidades que o citam |
|---|---|---|---|
| biblioteca/__init__.py | M | +1/−1 | — |
| biblioteca/api.py | M | +4/−2 | P01, P02, P03, P04, P05, P06, P07, P08 |
| biblioteca/modelos.py | M | +2/−0 | entidade Emprestimo, entidade Leitor, entidade Livro, entidade Notificacao, entidade ParametroMulta |
| biblioteca/repositorio.py | M | +7/−3 | P01, P02, P03, P04, P05, P06, P07, P08, P09 |
| biblioteca/servicos.py | M | +20/−6 | P01, P02, P03, P04, P05, P06, P07, P08, P09 |

| Processo | Situação | Trechos citados com mudança | Movimentos candidatos a 'alterado' |
|---|---|---|---|
| P06 Registrar empréstimo | afetado (trecho) | biblioteca/repositorio.py#salvar_emprestimo (alterado) | W Emprestimo (alterado) |
| P07 Registrar devolução | afetado (trecho) | biblioteca/api.py#POST /emprestimos/{id}/devolucao (alterado); biblioteca/repositorio.py#salvar_emprestimo (alterado); biblioteca/servicos.py#registrar_devolucao (alterado) | E Emprestimo (alterado); W Emprestimo (alterado) |
| P08 Relatório de atrasos | afetado (trecho) | biblioteca/servicos.py#nome_leitor (alterado); biblioteca/servicos.py#relatorio_atrasos (alterado); biblioteca/servicos.py#titulo_livro (alterado) | X Leitor (alterado); X Livro (alterado) |

## Resumo

- Re-extrair e marcar movimentos conforme RD-01: P06, P07, P08
- Afetados apenas por arquivo (confirmar na extração): P01, P02, P03, P04, P05, P09
- Arquivos alterados sem processo nem entidade associados (procurar pontos de entrada novos): biblioteca/__init__.py
```

Leitura: o diff de 34 linhas tocou todos os arquivos, mas só três processos têm trechos
citados alterados. Dos candidatos, a extração dirigida confirma dois e descarta dois pela
RD-01: em P06 a função `salvar_emprestimo` mudou, mas a gravação do empréstimo novo
continua com os mesmos atributos (não alterado); em P08 as linhas que citam nome do
leitor e título mudaram porque a estrutura da linha do relatório perdeu a multa
estimada, mas os atributos de Leitor e Livro são os mesmos (não alterados), enquanto a
saída de Emprestimo perdeu um atributo (alterada) e a leitura de ParametroMulta
desapareceu (excluída). O processo novo P10 não aparece no impacto, por definição; é
encontrado na extração da v2 a partir da nova rota em `api.py`.

**Auditoria.** `mfo.py auditar biblioteca-v2.mfc.json --raiz codigo-biblioteca --fonte COD --fonte TST`:

```
**89 de 89 evidências verificadas (100%)**
```

**Mudança.** `mfo.py mudanca biblioteca-v1.mfc.json biblioteca-v2.mfc.json` produz os
mesmos 8 PFO de mudança do capítulo 6 (4 incluídos, 3 alterados, 1 excluído), agora com
evidências de código em cada chave e com a composição por modo de produção do capítulo 9.

**Aceite.** Os testes em `codigo-biblioteca/testes/teste_aceitacao.py` exercitam um
processo por função; rodá-los contra a v2 é a evidência do campo `aceite` de cada
processo:

```
python3 -I MFO/exemplos/codigo-biblioteca/testes/teste_aceitacao.py v2
```

## 8.6 Limites

- **Pontos de entrada não evidentes.** Reflexão, plugins, roteamento por configuração e
  geração de código escondem processos. O impacto aponta arquivos alterados sem processo;
  o restante é trabalho da extração.
- **Lógica em configuração.** Regras em planilhas, motores de regras e fluxos
  configuráveis mudam movimentos sem mudar código. A fonte, nesses casos, é a
  configuração, declarada como fonte do modelo.
- **Mudanças só de interface.** Uma tela refeita sem mudar atributos é tamanho zero
  (RD-04). O relatório de impacto registra o diff para que o trabalho não fique invisível.
- **Código gerado ou ofuscado.** A evidência deve apontar para a fonte que as pessoas
  editam, não para o artefato gerado.
- **Heurística de bloco.** A delimitação por indentação é aproximada; ela indica
  candidatos, nunca decide. A decisão é da RD-01 na extração.
