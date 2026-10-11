<!-- Gerado por scripts/gera-docs.py a partir de MFO/05-comparacao-entre-softwares.md. Não edite: edite a fonte e gere de novo. -->
# 5. Comparação entre softwares

> MFO — Medição Funcional Objetiva · Versão 1.0

## 5.1 Condições de comparabilidade

Dois tamanhos MFO são comparáveis quando:

1. foram medidos com a **mesma versão do método**;
2. têm o **mesmo nível** de medição (R, C ou RC);
3. têm **escopo declarado** e fronteiras definidas pelo mesmo critério (aplicação inteira,
   serviço, módulo), na mesma camada;
4. têm **grau de evidência** compatível (a organização fixa um mínimo; 90% é um ponto de
   partida razoável para comparações com efeito contratual);
5. para comparações de produtividade ou custo, o esforço ou custo associados foram
   apurados com a mesma definição (as mesmas fases, como o Guia STI faz ao distribuir
   esforço por refino, implementação e teste).

Comparações que violem uma dessas condições devem dizer qual e por quê.

## 5.2 Perfil funcional

O total esconde a forma do software. Dois sistemas de 500 PFO podem ser muito diferentes:
um com 40 processos densos, outro com 150 processos simples. O relatório MFO traz, além do
total, o **perfil funcional**, calculado pela ferramenta:

| Indicador | Definição | O que revela |
|---|---|---|
| PFO | total de movimentos | tamanho |
| NP | número de processos | amplitude funcional |
| NE | número de entidades declaradas (sem as reservadas) | amplitude do domínio de dados |
| E, X, R, W | movimentos por tipo | forma |
| Densidade | PFO / NP | complexidade média das transações |
| Persistência | (R + W) / PFO | quanto o software gira em torno de dados armazenados |
| Interface | (E + X) / PFO | quanto gira em torno de troca com usuários e sistemas |
| Entidades por processo | NE / NP | acoplamento médio entre funções e dados |
| Evidência | movimentos com evidência / PFO | confiabilidade do modelo |
| D1, D2 (suplemento D) | desfechos distintos e regras declaradas, totais e por processo | a dimensão de decisão que o PFO não vê (capítulo 12) |

Perfis típicos:

- **CRUD administrativo:** densidade 3,5 a 4,5; persistência próxima de 0,5; muitos processos.
- **Integração / API de orquestração:** interface alta (> 0,6), muitas X para sistemas.
- **Relatórios e BI operacional:** R dominante, X por várias entidades, densidade alta.
- **Embarcado / controle:** E e X de dispositivos, poucas entidades, persistência baixa.

Comparar perfis permite afirmar, por exemplo, que "o sistema A é 20% maior que o B, mas
tem metade da densidade; o esforço por processo tende a ser menor em A", sem sair dos
números.

## 5.3 Indicadores derivados

O PFO é tamanho. Indicadores de gestão nascem de sua combinação com dados da organização:

| Indicador | Fórmula | Condição |
|---|---|---|
| Produtividade | PFO entregues / horas (ou pessoa-dia) | mesmo nível, mesma definição de esforço |
| Custo unitário | custo / PFO | idem |
| Preço com duas dimensões | a × PFO + b × D, com a e b por regressão sobre o histórico | mesma classe de sistema; D = D1, a base contratual (capítulo 12) |
| Densidade de defeitos | defeitos / PFO | mesma definição de defeito e janela |
| Velocidade de evolução | PFO de mudança por período | mesmo software, modelos consecutivos |
| Aderência R × C | PFO(C) / PFO(R) e lista de chaves só em R ou só em C | mesmo software, mesma versão |
| Cobertura de testes funcional | processos com teste automatizado / NP | nível C |
| Erro de estimativa | (PFO estimado − PFO medido) / PFO medido | estimativa rotulada e medição do mesmo escopo (capítulo 11) |

Os valores de referência (taxa de entrega, custo por PFO) devem ser calibrados pela
própria organização, como se faz com PF e PFC. A MFO não publica valores de mercado. Os
indicadores de produção com IA (PFO por modo, alavancagem humana, custo por PFO, aceite,
excedente) estão no capítulo 9.

## 5.4 Relação com APF e COSMIC

### Correspondência conceitual

| MFO | APF (IFPUG) | COSMIC |
|---|---|---|
| Processo | Processo elementar (EE, SE, CE) | Processo funcional |
| Entidade | Arquivo lógico (ALI, AIE) ou seu RLR | Objeto de interesse / grupo de dados |
| E | DER de entrada; a própria EE | Entry |
| X | DER de saída; SE ou CE | Exit |
| R | ALR referenciado; AIE | Read |
| W | ALI mantido | Write |
| X `MENSAGEM` | DER de mensagem | Exit de mensagens de erro/confirmação |
| E `DISPARO` | ação do usuário (DER de ação) | Entry disparadora de um atributo |
| PFO de mudança | PF incluído, alterado, excluído | PFC incluído, alterado, excluído |

### Diferenças de resultado esperadas

- **Em relação ao COSMIC:** os totais tendem a ser próximos, porque o primitivo é o mesmo.
  As diferenças aparecem onde o COSMIC deixa ao medidor a identificação de grupos de dados
  em saídas compostas (RI-06 a fixa uma X por entidade) e onde a MFO fixa casos
  frequentes (canais, formatos, lista e detalhe). O exemplo do capítulo 6 mostra uma
  faixa de 47 a 51 PFC para 51 PFO.
- **Em relação à APF:** a APF conta funções de dados diretamente (7 a 15 PF por arquivo
  lógico) e limita cada transação a 7 PF. Sistemas com muitos arquivos e transações
  simples tendem a ter mais PF que PFO; sistemas com transações ricas (muitas entidades por
  processo) tendem ao contrário. Não existe fator fixo de conversão. No sistema real do
  capítulo 10, a razão PFO/PF de transação variou de 0,87 a 1,39 entre domínios (1,17 no
  total), pelos motivos acima.

### Procedimento de calibração local

1. Selecionar de 10 a 20 softwares (ou demandas) já medidos em PF ou PFC.
2. Medir cada um em PFO no mesmo nível e com o mesmo escopo.
3. Ajustar uma regressão simples (PF = a × PFO + b) e registrar o coeficiente de
   determinação e a dispersão.
4. Usar o fator **apenas** para converter históricos; novas medições são feitas em PFO.
5. Repetir a calibração a cada versão do método ou mudança relevante de carteira.

## 5.5 Limites e cuidados

- **O julgamento não desaparece; é confinado.** Decidir fronteira, entidades e processos
  ainda exige interpretação. A MFO reduz a variação com testes de decisão, exige evidência
  e **mede** a variação restante pelo índice de concordância. Um resultado sem segunda
  medição é uma medição, não uma prova de objetividade.
- **Atributos não pesam.** Um processo que move uma entidade de 3 atributos e outro que
  move uma de 60 têm o mesmo tamanho. É a mesma simplificação do COSMIC. Quem precisar
  disso deve criar uma extensão local, reportada à parte, nunca somada.
- **Pedaços pequenos.** Mudanças de 1 a 3 PFO podem exigir esforço desproporcional. Use
  pisos contratuais, não ajustes na contagem.
- **Interfaces ricas** (editores, mapas, gráficos interativos) são subdimensionadas por
  qualquer método funcional. Registre o requisito não funcional e trate-o fora.
- **Software intensivo em algoritmos** (otimização, simulação, aprendizado de máquina): o
  tamanho funcional captura entradas, saídas e dados persistidos, não a dificuldade do
  algoritmo. O suplemento D indica onde há derivação, mas não quanto custa.
