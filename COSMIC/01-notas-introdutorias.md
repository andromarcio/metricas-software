# Notas Introdutórias

> Método COSMIC v3.0.1 — Manual de Medição

O propósito do método COSMIC é prover um método padrão para a medição do tamanho funcional do software correspondente aos domínios funcionais normalmente denominados software para "aplicações de negócio" (ou 'MIS') e software 'real-time'.

O método COSMIC foi aceito pelo ISO/IEC JTC1 SC7 em dezembro de 2002 como o Padrão Internacional ISO/IEC 19761 'Engenharia de Software – COSMIC-FFP – Um método para a medição funcional de tamanho' (daqui em diante referenciado como 'ISO/IEC 19761').

Para maior clareza, a ISO/IEC 19761 contém as definições normativas e regras fundamentais do método. O propósito do Manual de Medição não é apenas prover tais regras e definições, mas também prover explicações adicionais e muito mais exemplos a fim de ajudar os medidores a entenderem completamente e aplicarem o método. Contudo, conforme mais experiência foi sendo adquirida com o método, considerou-se útil acrescentar mais regras e exemplos e até refinar as definições de alguns conceitos subjacentes. O Common Software Measurement International Consortium (COSMIC) planeja que tais acréscimos e refinamentos serão submetidos à ISO para inclusão na ISO/IEC 19761 na época de sua revisão em 2007/08.

Este 'Manual de Medição' é um dos quatro documentos COSMIC que definem a versão 3.0 do método. Os outros três são:

- 'Visão Geral da Documentação e Glossário de Termos' (O Glossário define todos os termos comuns a todos os documentos COSMIC. Este documento também descreve outros documentos de suporte disponíveis, tais como estudos de caso e guias para domínios específicos.)
- 'Visão Geral do Método'
- 'Tópicos Avançados e Relacionados' (Este documento tratará com maior detalhe a tarefa de garantir a compatibilidade entre as medições de tamanho e incluirá capítulos sobre medições aproximadas e no início do projeto, assim como a convertibilidade de medições que apareceram anteriormente na versão 2.2 do Manual de Medição.)

Aos leitores iniciantes na medição funcional de software ('FSM'), ou que estejam familiarizados com outro método FSM, é fortemente recomendada a leitura do documento 'Visão Geral do Método' antes de ler este Manual de Medição.

## Principais mudanças na versão 3.0 do método COSMIC

A mudança de designação na versão do método COSMIC de 2.2 para 3.0 indica que esta versão representa um avanço significativo sobre a versão anterior. As principais mudanças na produção desta versão 3.0 do método COSMIC a partir da versão anterior definida no Manual de Medição versão 2.2 são apresentadas a seguir.

- Para tornar a documentação do método COSMIC mais amigável, a versão 3.0 do método é agora definida em quatro documentos distintos, conforme relacionado acima.
- As propostas dos dois Boletins de Atualização do Método publicados desde a última versão 2.2 do Manual de Medição foram incorporadas. Tais são a MUB 1 'Melhorias Propostas na Definição e Características de uma "Camada" de software' e MUB 2 'Melhorias Propostas na Definição de um "objeto de interesse"'. (A versão 3.0.1 incorpora mais três MUB's – ver o Apêndice D.)
- Uma fase 'Estratégia de Medição' foi definida separadamente como a primeira do processo de medição. A fase de estratégia também foi aperfeiçoada com orientações sobre a consideração do 'nível de granularidade' dos Requisitos Funcionais do Usuário do software a ser medido, para ajudar a garantir que as medições de diferentes pedaços de software sejam comparáveis.
- A experiência tem demonstrado que os conceitos correspondentes aos pontos de vista, na medição, do 'Usuário Final' e do 'Desenvolvedor', introduzidos na versão 2.2 do Manual de Medição podem ser substituído pelo conceito mais simples de 'usuário funcional'. Este último pode ser definido, de uma maneira não exata, como alguém que envia ou que deve receber dados, segundo os Requisitos Funcionais do Usuário do software a ser medido. Todas as medições de tamanho de um pedaço de software serão então realizadas sobre a funcionalidade provida aos usuários funcionais do mesmo, conforme identificado nos respectivos RFU.
- O nome da unidade de medida do método foi alterado de 'Unidade de tamanho funcional COSMIC' (abreviada como Utfc) para 'Ponto de Função COSMIC' (abreviado como PFC). Esta mudança foi efetuada para facilitar a leitura e pronúncia, trazendo também maior conformidade com os outros métodos baseados em 'Pontos de Função'. Como uma simplificação adicional, o nome do método foi alterado de 'COSMIC-FFP' para 'COSMIC'.
- O glossário foi atualizado e melhorado a fim de facilitar a leitura, tendo sido transferido para o novo documento 'Visão Geral da Documentação e Glossário de Termos'.
- Algum material foi removido, especialmente sobre conceitos de análise de dados. Este material agora faz parte do 'Guia para Dimensionamento de Aplicações de Negócio utilizando COSMIC', pois é específico daquele domínio e não de todo o método COSMIC.
- Muitas melhorias editoriais e acréscimos foram efetuados para aumentar a consistência da terminologia e melhorar o entendimento. Dentre esses, foi feita uma distinção mais consistente entre 'princípios' e 'regras' do método, por meio da adoção de uma convenção do mundo da contabilidade, de que 'as regras existem para ajudar a aplicar princípios e definições'. Tanto os princípios quanto as regras devem ser considerados obrigatórios. Dessa forma, a maioria dos exemplos foi transferida das declarações de princípios e regras para o corpo do texto.

Todas essas mudanças estão resumidas no Apêndice D.

Os leitores familiarizados com a versão 2.2 do Manual de Medição encontrarão a maioria das mudanças da versão 3.0 na fase recentemente destacada, a "Estratégia de Medição".

## Consequências das principais mudanças sobre as medições de tamanho existentes

Os princípios originais do método COSMIC permaneceram sem mudanças desde a sua publicação inicial no primeiro rascunho do Manual de Medição em 1999, apesar dos refinamentos e acréscimos necessários para produzir o Padrão Internacional e da produção das versões 2.1, 2.2, 3.0 e desta última versão 3.0.1 do Manual de Medição.

Os tamanhos funcionais medidos de acordo com os princípios e regras das versões 3.0 e 3.0.1 do Manual de Medição podem diferir dos tamanhos medidos com base em versões anteriores, apenas porque as novas regras pretendem ser mais precisas. Assim sendo, os medidores possuem menos espaço para interpretações pessoais do que havia nas versões anteriores. As mudanças na área da Estratégia de Medição e a mudança no nome da unidade de medida resultaram em diferenças triviais ao reportar os resultados, se comparado às versões anteriores.

## Explicação para as principais mudanças da versão 2.2 para a versão 3.0 do Manual de Medição

Primeiro precisamos enfatizar que a unidade de medição COSMIC, a 'Utfc' (agora denominada 'PFC'), permanece inalterada desde que foi introduzida na primeira versão pública do Manual de Medição COSMIC-FFP no ano de 1999. Este é o equivalente COSMIC de, por exemplo, uma unidade padrão de comprimento tal como o metro. Entretanto, o tamanho funcional de um pedaço de software pode ser medido de várias maneiras, e às vezes é um problema, para qualquer Método de Medição de Tamanho Funcional (MTF), responder à pergunta: 'qual tamanho deveríamos medir?'

O primeiro problema é sabermos que qualquer pedaço de software provê funcionalidade a vários tipos de 'usuários', onde um usuário é definido na terminologia do padrão ISO/IEC 14143/1 ('Princípios de MTF') basicamente como 'qualquer coisa que interage com o software sendo medido'. Segue-se que o tamanho funcional de um pedaço de software depende de quem ou o quê é(são) definido(s) como o(s) seu(s) usuário(s).

Vamos considerar o exemplo do software aplicativo de um telefone celular. Se aceitarmos a definição de 'usuário' da ISO literalmente, os usuários de um aplicativo de telefone celular poderiam incluir todos os seguintes: um ser humano que pressiona os botões; os dispositivos de hardware (por exemplo: a tela, teclas, etc.) que interagem com o aplicativo; o sistema operacional que dá suporte ao aplicativo; softwares 'pares' distintos que interagem com o aplicativo sendo medido. Todos os quatro tipos de usuário requerem funcionalidades diferentes (daí o tamanho funcional diferir dependendo de quem ou o quê for definido como o usuário). Assim sendo, como poderemos saber, dado um tamanho funcional específico, quem ou o quê são os usuários, isto é, quais funcionalidades foram medidas?

Foi esta questão que inicialmente levou o Comitê de Práticas de Medição COSMIC ('MPC') a introduzir na versão 2.2 do Manual de Medição os conceitos de Ponto de Vista de Medição do 'Usuário Final' e do "Desenvolvedor'. Contudo, a experiência tem mostrado que tais definições, especialmente a de Ponto de Vista de Medição do Desenvolvedor, não eram suficientemente genéricas para auxiliar na definição de todas as necessidades de medição. O MPC concluiu que a abordagem correta e mais genérica é definir o conceito de um 'usuário funcional' e que o tamanho funcional muda dependendo de quem ou o quê seja definido como o usuário funcional. A identificação dos usuários funcionais depende do propósito da medição e os usuários funcionais devem ser normalmente identificáveis nos Requisitos Funcionais do Usuário (RFU) do software a ser medido. A idéia de definir 'Pontos de Vista de Medição' específicos não é mais necessária.

O segundo problema é sabermos que os RFU evoluem conforme o projeto avança e, dependendo de como a medição seja realizada, o tamanho medido pode parecer aumentar. A primeira versão dos RFU para um novo pedaço de software pode ser especificada a um 'nível alto'. Conforme o projeto avança e os requisitos são elaborados em maior detalhe, os RFU são especificados em maior detalhe, ou a um 'nível mais baixo', podendo seu tamanho parecer aumentar. Distinguimos tais níveis de detalhe como 'níveis de granularidade'.

Dessa forma, o problema que deve ser abordado agora é: como podemos estar certos de que duas medições foram feitas no mesmo nível de granularidade? As versões 3.0 e 3.0.1 do Manual de Medição fornecem recomendações sobre este tópico, o que é especialmente importante quando os tamanhos são medidos cedo no ciclo de vida de um projeto, quando os RFU ainda estão evoluindo. O tópico torna-se crítico quando os tamanhos são utilizados para medições de desempenho que devem ser comparadas a partir de fontes diferentes, como acontece em exercícios de benchmarking.

É importante enfatizar que estes novos conceitos tais como 'usuário funcional' e 'nível de granularidade', assim como os processos associados à sua determinação que foram introduzidos na Estratégia de Medição não precisam ser uma exclusividade do método COSMIC. Ao contrário, são aplicáveis a todos os métodos de Medição de Tamanho Funcional (MTF). Como o método COSMIC baseia-se em princípios sólidos de engenharia e é aplicável a uma faixa mais ampla de domínios de software do que os métodos MTF de '1a. geração', o problema de definir 'qual tamanho devemos medir?' foi reconhecido e uma solução foi encontrada.

A maioria dos medidores utilizando COSMIC nos casos em que o propósito da medição é relacionado ao desempenho (por exemplo: estimativas, benchmarking, etc.) não precisarão gastar tempo na identificação de usuários funcionais ou na determinação do nível de granularidade a ser utilizado na medição, pois os mesmos serão bastante óbvios. No caso de medições onde as escolhas não sejam óbvias, existe material recente sobre o assunto na 'Fase da Estratégia de Medição' do Manual de Medição e no capítulo sobre como garantir a comparabilidade das medições de tamanho no documento 'Tópicos Avançados e Relacionados', onde os fatores a serem considerados nesses casos são discutidos em maior profundidade.

Comitê de Práticas de Medição COSMIC

Maio de 2009
