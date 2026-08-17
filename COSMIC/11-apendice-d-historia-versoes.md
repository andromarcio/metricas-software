# Apêndice D — História das Versões do Método COSMIC

> Método COSMIC v3.0.1 — Manual de Medição

Este Apêndice contém um resumo das principais mudanças efetuadas na derivação da versão 3.0 e desta versão 3.0.1 do método de medição de tamanho funcional COSMIC a partir da versão 2.2. A Versão 2.2 do método foi completamente descrita no ‘Manual de Medição v2.2’ (abreviado ‘MM’), mas da versão v3.0 em diante a documentação do método é agora distribuída em quatro documentos, apenas um dos quais é denominado ‘Manual de Medição’.

O propósito deste Apêndice é permitir a um leitor familiarizado com o MM v2.2 acompanhar as mudanças feitas nas versões 3.0 e 3.0.1 e, onde necessário, entender sua justificativa. (Para as mudanças efetuadas na derivação da versão 2.2 a partir da versão 2.1, ver a versão 2.2 do Manual de Medição, Apêndice E.)

## Da versão 2.2 para a versão 3.0

Na tabela abaixo, mostrando as principais mudanças efetuadas na derivação da v3.0 a partir da v2.2, são referenciados dois ‘Boletins de Atualização do Método’ (ou ‘MUB’s’ – ‘Method Update Bulletins’). Um MUB é publicado pelo COSMIC para propor melhorias no método, no intervalo de tempo entre publicações mais importantes sobre a definição do método. Os dois MUBs são:

- MUB 1 “Melhorias propostas para a definição e características de uma ‘Camada’ de software, publicado em maio de 2003.
- MUB 2 “Melhoria proposta para a definição de um ‘objeto de interesse’, publicado em março de 2005.

No processo de atualização do método da v2.2 para a v3.0, foi feito um esforço para racionalizar as orientações em ‘princípios’ e ‘regras’ e separar todos os exemplos dos princípios e regras. Mudanças como essas e várias melhorias editoriais não foram descritas a seguir.

| Ref V2.2 | Ref V3.0 | Mudança |
|---|---|---|
| **Reestruturação do Método COSMIC** |  |  |
| 2.2, 2.7, 3.1, 3.2 | 1.5, Capítulo 2 | Uma fase ‘Estratégia de Medição’ foi destacada como a primeira fase do que é agora um método composto por três fases.<br>A fase Estratégia de Medição agora inclui a consideração de ‘camadas’, ‘fronteiras’ e ‘usuários (funcionais)’, que eram considerados parte da fase de Mapeamento no MM v2.2 |
| **Reestruturação do Manual de Medição** |  |  |
|  |  | Durante a produção da v3.0 do Método COSMIC, o MM V2.2 foi dividido em quatro documentos para facilitar o uso<br>• ‘Método COSMIC v3.0: Visão Geral da Documentação e Glossário de Termos’ (novo)<br>• ‘Método COSMIC v3.0: Visão Geral do Método’ (Capítulos 1 e 2 do MM v2.2)<br>• ‘Método COSMIC v3.0: Manual de Medição’ (Capítulos 3, 4 e 5 e os Apêndices do MM v2.2<br>• ‘Método COSMIC v3.0: Tópicos Avançados e Relacionados’ (Capítulos 6 e 7 do MM v2.2)<br>As referências a artigos de suporte e de pesquisa foram removidas do MM. Estão agora disponíveis em www.cosmicon.com. As únicas referências que permaneceram nesses quatro documentos estão em notas de pé de página |
| Capítulo 4 | Capítulo 4 | O capítulo sobre a Fase de Medição foi consideravelmente reestruturado para fornecer uma exposição mais lógica |
| Apêndice D | -- | Este Apêndice sobre ‘Mais informações sobre camadas de software’ foi removido, por ser incompatível com o MUB 1 e agregar pouco valor. Ver também as notas abaixo sobre as mudanças ligadas ao MUB 1 |
| **Mudanças de nomes e terminologia** |  |  |
| Geral |  | O nome do método ‘COSMIC-FFP’ foi simplificado para método ‘COSMIC’ |
| 5.1 | 4.2 | O nome da unidade de medida, ‘medida de tamanho funcional COSMIC’ (abreviada ‘Cfsu’) foi alterada para ‘Ponto de Função COSMIC’ (abreviada ‘PFC’). Ver as Notas Introdutórias neste MM v3.0 para uma explicação desta mudança |
| 4.1 | 4.1.7 | A regra ‘Desduplicação de movimentação de dados’ foi renomeada regra da ‘Unicidade na movimentação de dados’ |
| **Conceitos novos, substituídos e removidos** |  |  |
| 2.7 | 2.3 | Os conceitos de ‘abstração’, ‘ponto de vista’, ‘Ponto de Vista da Medição’, ‘Ponto de Vista do Usuário Final na Medição’ e ‘Ponto de Vista do Desenvolvedor na Medição’ foram removidos. Foram substituídos pelo conceito mais genérico de que o tamanho funcional de um pedaço de software a ser medido depende da funcionalidade disponível para o(s) ‘usuário(s) final(is)’ do software. Tais devem ser identificáveis nos Requisitos Funcionais do Usuário para o software a ser medido. A definição do(s) ‘usuário(s) funcional(is)’ é portanto um pré-requisito para a definição de qual tamanho deve ser medido ou para a interpretação de uma medida de tamanho existente. Ver as Notas Introdutórias a este MM v3.0 para uma explicação mais detalhada desta mudança |
| 3.2 | 2.3 | O conceito de ‘usuário’ (conforme definido na ISO/IEC 14143/1) foi substituído pelo conceito de ‘usuário funcional’ que é um conceito mais restrito. Ver as Notas Introdutórias a este MM v3.0 para uma explicação mais detalhada desta mudança.<br>No item 2.3.2, dois exemplos foram introduzidos de quando o tamanho funcional varia com o tipo de usuário funcional definido no RFU, para um telefone celular e para um pacote de software de aplicação de negócio. |
| -- | 2.2.2 | O ‘nível de decomposição’ do software a ser medido foi introduzido na discussão do escopo da medição |
| -- | 2.4 | O ‘nível de granularidade’ dos requisitos funcionais do usuário do software a ser medido foi introduzido na discussão da estratégia de medição. Um exemplo abrangente é fornecido. Ver as Notas Introdutórias deste MM v3.0 para uma explicação mais detalhada para esta mudança |
| -- | 2.4.3 | Um ‘nível de granularidade do processo funcional’ foi definido, assim como foram fornecidas regras e uma recomendação a respeito |
| 3.4 | 4.2 | O conceito de ‘persistência de um grupo de dados’ incluindo três níveis de persistência, nominalmente ‘transiente’, ‘curto’ e ‘indefinido’ foram removidos por terem sido demonstrados desnecessários. O conceito de ‘armazenamento persistente’ foi introduzido |
| 4.1 | -- | O conceito de ‘desduplicação’ foi removido por ter sido demonstrado desnecessário |
| **Definições, princípios e regras melhorados e refinados** |  |  |
| 2.3 | 2.2 | A definição de ‘Requisitos Funcionais do Usuário’ foi alterada para manter conformidade com a edição de 2007 da ISO/IEC 14143/1 |
| 2.4.1 | 1.3 | O ‘Modelo de Contexto de Software’ foi ampliado e refinado como uma declaração de princípios |
| 2.4.2 | 1.4 | O ‘Modelo Genérico de Software’ foi ampliado e refinado como uma declaração de princípios |
| 2.4, 3.1 | 2.2.3, 2.2.4, 3.1 | A definição de ‘camada’ foi atualizada para levar em conta o MUB 1.<br>As Figuras 2.4.1.1, 2.4.1.2 e 2.4.1.3 do MM v2.2 que foram usadas para ilustrar a interação dos usuários com o software em ‘camadas’ foram substituídas na v3.0 pelas Figuras 2.2.3.1 e 2.2.3.2 ilustrando arquiteturas em camadas típicas e as Figuras 3.1.1 e 3.1.2 ilustrando a interação lógica dos usuários funcionais com o software em camadas. O objetido desta mudança é distinguir mais claramente a visão *física* das arquiteturas de software em camadas típicas da visão *lógica* de um usuário funcional interagindo com um pedaço de software a ser medido de acordo com o modelo COSMIC |
| -- | 3.2.4 | O conceito de ‘componente par’ foi definido e seus princípios foram estabelecidos levando em conta o MUB 1 |
| 2.5 | 4.2, 4.3 | As ‘Características’ do processo de medição descritas na v2.2 foram reescritas como um conjunto de princípios e regras na v3.0 |
| 2.6 | 2.4 | O material sobre ‘dimensionamento no início da vida de um projeto: escalonamento da medição’ foi tratado parcialmente no MM v3.0 seção 2.4 sob ‘Nível de Granularidade’ e está detalhado no documento ‘Método COSMIC v3.0: Tópicos Avançados e Relacionados’ |
| 2.7 | 2.2 | Uma nota foi acrescentada à definição de ‘escopo’ para distinguir o ‘escopo global’ de um exercício de medição (o qual pode incluir diversos pedaços distintos de software cujo tamanho precise ser medido) do ‘escopo’ de uma medição individual de tamanho. |
| 3.2 | 4.1.8 | Três Exemplos que ilustram a interação dos usuários através de uma fronteira com o software em diferentes camadas e de diferentes ‘pontos de vista da medição’ foram mudados de lugar e reescritos tendo em vista a remoção dos ‘pontos de vista da medição’. Ver 4.1.8 (do MM v3.0) abaixo |
| -- | 3.1 | Um princípio foi acrescentado a respeito da aplicação do Modelo Genérico de Software ao software a ser medido |
| 3.3 | 3.2.1 | A definição de ‘processo funcional’ foi refinada para levar em conta a introdução do conceito de ‘usuário funcional’ que substitui ‘ator’ nesta definição |
| 3.3 | 3.2.1 | A definição de ‘evento disparador’ foi refinada |
| -- | 3.2.1 | A relação entre um evento disparador, um usuário funcional, uma Entry disparadora e um processo funcional foi clarificada na Figura 3.1.1 |
| 3.1 | 3.2.2 | Os princípios e regras para um ‘processo funcional’ foram fundidos em um conjunto de regras revisadas |
| -- | 3.2.3, 3.2.4, 3.2.5 | Muitos exemplos de processos funcionais e de como distinguí-los foram introduzidos |
| -- | 3.3.1 | A definição de um ‘objeto de interesse’ foi introduzida, alinhada com o MUB 2 |
| 3.4 | 3.3.3 | Exemplos da identificação de objetos de interesse e grupos de dados foram separados das regras para grupos de dados. Algum material de domínios específicos sobre convenções da análise de dados de entidades-relacionamentos foi transferido para o ‘Guia para dimensionamento de Software de Aplicação de Negócio v1.0’. |
| -- | 3.3.4 | Foram incluídas orientações sobre ‘dados ou grupos de dados que não são candidatos a movimentações de dados’ |
| -- | 3.3.5 | Foram incluídas orientações sobre quando, tipicamente em software ‘real-time’, não deve valer a pena distinguir um ‘usuário funcional’ de um ‘objeto de interesse’ sobre o qual dados são movimentados |
| 3.5 | 3.4 | A discussão de ‘atributos de dados’ foi reduzida e simplificada já que a consideração de atributos de dados não é uma parte obrigatória do método |
| 4.1 | 4.1.1 | A definição de ‘movimentação de dados’ foi racionalizada |
| 4.1 | 4.1.7 | Foram esclarecidas as regras sobre ‘desduplicação de movimentações de dados’ (agora renomeadas como regras sobre ‘unicidade na movimentação de dados e possíveis exceções’) com a inclusão de vários exemplos |
| 4.1 | -- | As regras para domínios específicos sobre as movimentações de dados Read e Write em Processos Funcionais de ‘Atualização’ foram transferidas para o ‘Guia para o Dimensionamento de Software de Aplicações de Negócio v1.0’. |
| 4.1 | 4.1.8 | As ‘Regras para correspondência de dados através de fronteiras’ (que no MM v2.2 eram aplicáveis no ‘Ponto de Vista do Desenvolvedor na Medição’, agora eliminado) foram excluídas, mas os conceitos foram combinados com os Casos anteriormente fornecidos no MM v2.2 seção 3.2, para produzir uma nova seção sobre ‘quando um processo funcional movimenta dados de ou para o armazenamento persistente’ |
| 4.1 | 4.1.6 | Foi definida a ‘Manipulação de dados’ e incluído um princípio sobre ‘manipulação de dados associada à movimentação de dados’. As orientações sobre a manipulação de dados associada aos diversos tipos de movimentações de dados foram expandidas |
| 4.1.1 | 4.1.2 | Os princípios e regras para uma Entry foram racionalizados. Um novo princípio foi acrescentado sobre funcionalidade ‘solicitação para submeter’. |
| 4.1.2 | 4.1.3 | Os princípios e regras sobre uma Exit foram racionalizados, incluindo a remoção da referência ao ‘ponto de vista do usuário final na medição’ |
| 4.1.3 | 4.1.4 | Os princípios para um Read foram racionalizados. Um novo princípio foi acrescentado sobre funcionalidade ‘solicitação de leitura’ |
| 4.1.4 | 4.1.5 | Os princípios para um Write foram racionalizados |
| -- | 4.1.9 | Foram incluídas novas regras sobre ‘quando um processo funcional requer dados de um usuário funcional’ |
| -- | 4.1.10 | Uma definição e uma regra foram introduzidas para o conceito de um ‘comando de controle’ que é válido somente no domínio de software de aplicação de negócio |
| 4.1.5 | 4.5 | A discussão de ‘extensões locais para o método’ foi expandida |
| 4.3 | 4.3 | Os princípios de ‘agregação de resultados da medição’ foram alterados para ‘regras’ e expandidos para cobrir as regras para a obtenção do tamanho de um pedaço de software através da soma dos tamanhos dos seus componentes. O MM v2.2 referia-se a essas regras somente no contexto do ‘ponto de vista do desenvolvedor’. Tal restrição foi removida |
| -- | 4.4 | Uma nova seção sobre ‘medição do tamanho de mudanças no software’ e novas regras foram acrescentadas |
| 5.1 | 5.1 | As regras para rotular os resultados da medição foram alteradas para reconhecer a mudança da unidade de medida de ‘Cfsu’ para ‘PFC’ |
| 5.2 | 5.2 | As regras sobre ‘reporte da medição’ foram expandidas para listar mais itens |
| Ap. B | Ap. B | Atualizado para os Princípios da v3.0 |
| Ap. C | Ap. C | Atualizado para as Regras da v3.0 |

## Da versão 3.0 para a versão 3.0.1

As mudanças mais importantes na derivação da versão 3.0.1 a partir da versão 3.0 ocorreram onde foi desejável melhorar a escrita de algumas definições, princípios e regras, bem como algumas partes do texto. Com a exceção de um erro, as melhorias foram todas feitas por razão de clareza. A maior parte das mudanças foi publicada em três Boletins de Atualização do Método antes da versão 3.0.1.

- MUB 3: ‘Correção de um erro na Fig. 4.1.8.1 (b) do Manual de Medição do Método COSMIC v3.0’, publicado em junho de 2008
- MUB 4: ‘Clarificação do princípio e regras para funcionalidade ‘Solicitação de submissão’ no ‘Manual de Medição do Método COSMIC v3.0’, publicado em junho de 2008
- MUB 5: ‘Melhorias propostas para (a) Definições de ‘Nível de Decomposição’ e de ‘Componente Par’, e (b) Princípio (c) para um ‘Componente Par’, publicado em fevereiro de 2009

Diversas melhorias editoriais também foram efetuadas. Estas envolvem, principalmente, separar os Exemplos mais claramente do texto principal, com um tipo diferente de fonte e mais subseções.

Resumo das principais mudanças:

| Ref V3.0.1 | Mudança |
|---|---|
| 2.2.3 | A definição de ‘Nível de Decomposição’ foi alterada para maior clareza (MUB 5). |
| 2.2.4 | Na definição de ‘Camada’ o termo ‘arquitetura de software’ foi substituído por ‘sistema de software’, pois o termo ‘arquitetura’ implica que o software já está particionado.<br>Regra (c) removida. Esta era uma regra geral de projeto de software e não específica de camadas e medição. A referência ao ‘Apêndice D’ na v3.0 estava incorreta. |
| 2.2.5 | A definição de ‘Par’ foi inserida e a definição de ‘Componente Par’ modificada para maior clareza. O princípio (c) para ‘Componente Par’ foi alterado para um princípio que é mais relevante para MFT. A Figura 2.2.5.1 foi incluída para esclarecer o relacionamento entre componentes pares e pedaços de software pares. (MUB 5). |
| 2.3.2 | A regra (c) para Fronteira foi alterada para maior clareza. (Consequência de MUB 5). |
| 2.4.3 | Na Figura 2.4.3.1, nas duas caixas do lado inferior direito, ‘método de pagamento’ foi alterado para ‘meios de pagamento’, pois este é um melhor termo para cheque, cartão de crédito, etc. |
| 3.2.2 | A regra (e) para um processo funcional foi restringida pelas palavras em itálico acrescentadas. Agora se lê: ‘Um processo funcional deve pertencer inteiramente ao *escopo de medição de um pedaço de* software em uma e apenas uma camada’. Esta restrição já existia no ‘Guia para Dimensionamento de Software de Aplicação de Negócio’ v1.1, mas é válida para software de qualquer domínio. |
| 3.2.6 | Acrescentada nova seção, com título ‘Os processos funcionais de componentes pares’. Este texto foi, em grande parte, obtido do ‘Guia para o Dimensionamento de Software Aplicativo de Negócio’ v1.1, mas é válido para software de qualquer domínio. Isto tem relação com a mudança na Regra (e) em 3.2.2. |
| 4.1.2 | O princípio (c) para uma Entry foi alterado para esclarecer como levar em conta uma funcionalidade ‘Solicitação de submissão’ (MUB 4). |
| 4.1.7 | A sentença de abertura desta seção sobre ‘Unicidade dos dados e possíveis exceções’ foi alterada para esclarecer o significado pretendido e torná-lo consistente com a Regra (a). O exemplo 2 também foi extensamente modificado para maior clareza. |
| 4.1.8 | A Figura 4.1.8.1 (b) foi alterada para corrigir um erro sobre como um software gerenciador de dispositivo interage com o hardware (MUB 3). |
| 4.1.9 | As regras para ‘Quando um processo funcional requer dados de um usuário funcional’ e os exemplos relacionados foram alterados para maior clareza (MUB 4). |
