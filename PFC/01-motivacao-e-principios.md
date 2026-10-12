# 1. Motivação e princípios de projeto

> PFC — Pontos de Função Caixa · Versão 1.0

## 1.1 O problema

A APF (IFPUG) e o COSMIC são métodos maduros, normatizados (ISO/IEC 20926 e ISO/IEC 19761)
e independentes de tecnologia. Ambos, porém, foram desenhados para serem aplicados por
especialistas certificados, e é nesse ponto que surgem as dificuldades quando se quer
medir com apoio de IA, medir sistemas legados sem documentação ou comparar carteiras
grandes de software:

1. **Pontos de julgamento não registrados.** Decidir se uma saída é SE ou CE (APF), se um
   relatório movimenta um ou três grupos de dados (COSMIC) ou onde fica a fronteira é
   uma escolha do medidor. O resultado é um número; a escolha que o produziu fica na
   cabeça de quem mediu. Duas contagens divergentes são difíceis de reconciliar.
2. **Volume de regras.** O CPM 4.3.1 tem mais de 500 páginas; o manual COSMIC remete a
   guias complementares por domínio. Isso não é defeito dos métodos, mas limita quem pode
   aplicá-los e dificulta a verificação de uma contagem por terceiros.
3. **Pesos e tetos.** A APF atribui pesos fixos (3 a 15 PF) por tabelas de complexidade com
   faixas estreitas; funções muito grandes ficam subdimensionadas, e a classificação em
   faixas é mais uma fonte de divergência. O COSMIC resolve isso com uma unidade sem teto.
4. **Uso com IA.** Um modelo de linguagem consegue aplicar as regras da APF ou do COSMIC,
   mas a saída é um texto argumentativo. Sem um formato canônico e sem exigência de
   evidência, não há como validar automaticamente a contagem nem detectar funções
   inventadas ou omitidas.

## 1.2 Objetivos do PFC

| Id | Objetivo | Como o PFC atende |
|---|---|---|
| O1 | Objetividade | Regras de identificação escritas como testes sim/não (RI-xx), contagem por função determinística (RC-xx), validações automáticas (V-xx). |
| O2 | Simplicidade | Sete conceitos, duas coisas contadas do mesmo jeito (o movimento e o desfecho), um peso (1), uma entidade reservada. O núcleo cabe em uma página. |
| O3 | Independência de tecnologia | Mede o que o software faz para seus usuários funcionais; nunca como foi construído. Aplicável a sistemas de negócio, APIs, batch, embarcados, mobile e linhas de comando. |
| O4 | Aplicabilidade por IA | O produto da interpretação é um modelo JSON com evidências; o número sai de uma ferramenta; a reprodutibilidade é medida por índice de concordância. |
| O5 | Comparabilidade | Rótulo obrigatório (nível, evidência, agente, escopo) e perfil funcional (distribuição E/X/R/W, densidade) além do total. |
| O6 | Produção com IA | O tamanho não depende de quem produziu; o modo de produção (humano a IA autônoma) e o aceite são registrados por processo com evidência, e o relatório traz PFC por modo, por hora humana e por custo (capítulo 9). |
| O7 | Estimativa | Estimar com o mesmo modelo e a mesma unidade: movimentos inferidos por perfis típicos calibráveis, níveis E0 a E2, intervalo obrigatório e convergência para a medição (capítulo 11). |

## 1.3 Princípios de projeto

**P1 — Medir o quê, não o como.** Só requisitos funcionais do usuário entram na medida. Requisitos
técnicos e de qualidade (desempenho, segurança, usabilidade, plataforma) são registrados
no rótulo e tratados fora da métrica, como fazem APF e COSMIC.

**P2 — Um peso só.** O tamanho é o número de coisas distintas que cruzam a fronteira ou o
armazenamento: as movimentações de dados (princípio P-03 do COSMIC) e os desfechos
distintos que o processo devolve. Não há tabelas de complexidade, pesos por tipo nem
fator de ajuste: cada movimento e cada desfecho vale 1 PFC. Toda regra que precisaria de
um "peso" é substituída por uma regra de identificação.

**P3 — Interpretar e calcular são passos separados.** A interpretação produz o Modelo
Funcional Canônico (MFC). O cálculo é uma função pura sobre o modelo. Qualquer pessoa ou
programa que receba o mesmo modelo obtém o mesmo número. Divergências entre medições
ficam, portanto, localizadas em elementos do modelo, não no total.

**P4 — Tudo que conta tem evidência.** Cada processo e cada movimento aponta para o
artefato que o sustenta (requisito, tela, endpoint, função, tabela, mensagem). Um
elemento sem evidência só entra no modelo marcado como inferido, e o grau de evidência
faz parte do rótulo do resultado.

**P5 — Regras como testes de decisão.** Cada regra de identificação é um conjunto de perguntas
com resposta sim/não e um desempate fixado para os casos recorrentes (CRUD, múltiplos
canais, assistentes de várias etapas, relatórios, jobs, mensageria, autenticação).

**P6 — Reprodutibilidade medida, não presumida.** O protocolo prevê uma segunda medição
independente e um índice de concordância calculado por ferramenta. A objetividade é um
resultado observável do processo, não uma propriedade declarada.

**P7 — Comparar só o comparável.** Resultados carregam rótulo; só se comparam tamanhos
do mesmo nível de medição (requisitos, código ou conciliado) com escopo declarado.

**P8 — Neutralidade de produtor.** O PFC mede o produto. Pessoa, IA assistida, IA dirigida
ou IA autônoma produzem o mesmo tamanho para a mesma funcionalidade; o que varia, e é
medido à parte, é esforço, custo, modo de produção e qualidade.

## 1.4 Comparação conceitual

| Dimensão | APF (IFPUG CPM 4.3.1) | COSMIC 3.0.1 | PFC 1.0 |
|---|---|---|---|
| Unidade | PF | CFP | PFC |
| Primitivo contado | Funções de dados (ALI, AIE) e de transação (EE, SE, CE) | Movimentações de dados (E, X, R, W) | Movimentações de dados (E, X, R, W) e desfechos distintos (D) |
| Peso | 3 a 15 por tabela de complexidade | 1 por movimentação | 1 por movimento ou desfecho |
| Teto por função | Sim (máx. 7 por transação, 15 por dado) | Não | Não |
| Dados persistentes | Contados diretamente (ALI/AIE) | Contados via R/W | Contados via R/W; entidades listadas no perfil |
| Formato do resultado | Planilha de contagem | Lista de processos e movimentações | Modelo JSON validável + relatório gerado |
| Evidência por item | Recomendada | Recomendada | Obrigatória (ou marcação de inferência) |
| Saídas com várias entidades | Uma função; DER/ALR contam complexidade | Depende da identificação de grupos de dados | Uma X por entidade cujos atributos saem (RI-06) |
| Mensagens de erro | DER de mensagem | Uma Exit por processo | Um desfecho por código ou mensagem distinto (RI-12) |
| Vários canais da mesma função | Single ou multiple instance (escolha do medidor) | Geralmente um processo | Um processo (RI-04) |
| Mudanças | PF incluído, alterado, excluído | CFP incluído, alterado, excluído | Diferença de chaves entre dois modelos |
| Verificação automática | Não prevista | Não prevista | Validações V-01 a V-11, auditoria de evidências e índice de concordância |
| Medição a partir do código | Não prevista; exige requisitos | Admite derivar RFU do software instalado | Nível C com evidência `arquivo#trecho` verificável por máquina; diff delimita e prova a mudança (capítulo 8) |
| Produtor do software | Não distingue | Não distingue | Neutro no tamanho; modo de produção e aceite por processo (capítulo 9) |
| Estimativa antecipada | Contagem estimativa e indicativa (NESMA), exige funções já classificadas | Dimensionamento aproximado por tamanhos médios | Mesmo modelo com movimentos inferidos; níveis E0 a E2 com intervalo; calibração por modelos medidos (capítulo 11) |
| Complexidade de decisão | Três faixas por DER e ALR, com teto | Não medida | Dentro do tamanho, pelo que a decisão devolve: um desfecho por código ou mensagem distinto, com evidência por item (capítulo 12) |

A unidade do COSMIC aparece na tabela como CFP, o símbolo do manual original. A tradução
brasileira do manual a abrevia PFC, sigla que esta especificação reserva ao Ponto de
Função Caixa.

## 1.5 O que o PFC não mede

- Esforço, custo, prazo ou produtividade. O PFC é tamanho; esses indicadores derivam dele
  quando combinados com dados da organização (seção 5.3).
- Requisitos não funcionais e qualidade do código.
- Complexidade algorítmica. Como o COSMIC, o PFC assume que a manipulação de dados está
  embutida nos movimentos. Da decisão entra no tamanho só o que ela produz de visível: um
  desfecho por código ou mensagem distinto (RI-12, capítulo 12); regras que não mudam o
  que o processo devolve não contam.
- Riqueza de interface. Dois processos com os mesmos movimentos têm o mesmo tamanho,
  ainda que um tenha uma tela sofisticada e o outro um comando de terminal.
- Pedaços muito pequenos. Como em qualquer método funcional, uma mudança de um ou dois
  movimentos pode ter esforço desproporcional ao tamanho.
