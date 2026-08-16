# Apêndice C — Resumo das Regras do Método COSMIC

> Método COSMIC v3.0.1 — Manual de Medição

A tabela abaixo identifica cada regra encontrada no Método de Medição COSMIC, para fins de referência precisa.

> **R-01 — Escopo**
>
> a) O escopo de uma Medição de Tamanho Funcional (MTF) deve ser derivado do propósito da medição.
>
> b) O escopo de uma medição qualquer não deve contemplar mais do que uma camada do software a ser medido

> **R-02 — Camada**
>
> a) Se o software for concebido utilizando-se uma arquitetura de camadas estabelecida de acordo com o modelo COSMIC, então aquela arquitetura deveria ser utilizada para identificar as camadas para fins de medição
>
> b) No domínio de SIG ou software de negócio, a camada ‘topo’, i.e., a camada que não é subordinada a nenhuma outra camada, é normalmente referenciada como a camada ‘da aplicação’.  O software (aplicativo) desta camada apoia-se, em última instância, nos serviços provido pelo software de todas as outras camadas para poder executar adequadamente.  No domínio de software ‘real-time’, o software da ‘camada topo’ é comumente referenciado como sendo um ‘sistema’, por exemplo, ‘software de sistema de controle de processo’, ‘software de sistema de controle de vôo’, etc.
>
> c) Não assumir que qualquer software que tenha evoluído sem a consideração de um projeto arquitetural ou estruturação possa ser particionado em camadas de acordo com o modelo COSMIC.

> **R-03 — Usuários Funcionais**
>
> a) Os usuários funcionais de um pedaço de software a ser medido devem ser derivados do propósito da medição
>
> b) Quando o propósito da medição de um pedaço de software estiver relacionado ao esforço para desenvolver ou modificar o pedaço de software, então os usuários funcionais deverão ser aqueles para quem a funcionalidade nova ou modificada deverá ser fornecida.

> **R-04 — Fronteira**
>
> a) Identificar o(s) usuário(s) funcional(is) que interagem com o software sendo medido.  A fronteira reside entre os usuários funcionais e o referido software.
>
> b) Por definição, existe uma fronteira entre cada par de camadas identificado, onde o software em uma camada é o usuário funcional do software na outra camada, e este último é o software a ser medido.
>
> c) Há uma fronteira entre quaisquer dois pedaços de software, incluindo quaisquer dois componentes que sejam pares um do outro; neste caso cada pedaço de software e/ou cada componente pode ser um usuário funcional de seu par.

> **R-05 — Nível de granularidade do processo funcional**
>
> a) A medição de tamanho funcional deve ser feita ao nível de granularidade do processo funcional
>
> b) Quando é necessária uma medição de tamanho funcional de alguns RFU que ainda não evoluíram até o nível no qual todos os processos funcionais foram identificados e todos os detalhes de suas movimentações de dados definidos, as medições devem ser feitas sobre as funcionalidades que foram definidas e, então, escalonadas para o nível de granularidade dos processos funcionais. (Ver o documento ‘Tópicos Avançados e Relacionados’ para métodos de ‘dimensionamento aproximado’, i.e., para estimar um tamanho funcional no início do processo de estabelecimento dos RFU.)

> **R-06 — Processo Funcional**
>
> a) Um processo funcional deve ser derivado de pelo menos um Requisito Funcional do Usuário identificável dentro do escopo acordado.
>
> b) Um processo funcional (tipo) deve ser executado quando um evento disparador identificável (tipo) ocorre.
>
> c) Um evento específico (tipo) pode disparar um ou mais processos funcionais (tipos) que executem em paralelo.  Um processo funcional específico (tipo) pode ser disparado por mais de um evento (tipo).
>
> d) Um processo funcional deve compreender pelo menos duas movimentações de dados, uma Entry mais (uma Exit ou um Write).
>
> e) Um processo funcional deve pertencer completamente ao escopo de medição de um pedaço de software em uma e somente uma camada.
>
> f) No contexto de software ‘real-time’, um processo funcional deve ser considerado concluído quando o mesmo entra em um estado de espera auto-induzido (i.e., o processo funcional já fez tudo o que é requerido como resposta ao evento disparador e espera até receber a próxima Entry disparadora).
>
> g) Um processo funcional (tipo) deve ser identificado mesmo quando seus RFU permitirem que o referido processo funcional ocorra com diferentes subconjuntos de seu número máximo de atributos de dados de entrada, e mesmo que tais variações e/ou diferentes valores de dados de entrada possam dar origem a diferentes caminhos de processamento através do processo funcional.
>
> h) Eventos distintos (tipos) e consequentemente processos funcionais distintos (tipos) devem ser identificados separadamente nos seguintes casos:
>
> - Quando as decisões resultarem em eventos separados e desacoplados no tempo (p.ex., entrar com os dados do pedido hoje e mais tarde confirmar o aceite do pedido, requerendo uma decisão separada, deveria ser considerado como indicação de processos funcionais distintos),
> - Quando as responsabilidades pelas atividades estão separadas (p.ex., em um sistema de pessoal onde a responsabilidade pela manutenção dos dados básicos de pessoal e dos dados de pagamento estão separadas, indicando processos funcionais distintos; ou no caso de um pacote de software implementado onde há funcionalidades disponíveis para que um administrador de sistema mantenha os parâmetros do pacote, separadas das funcionalidades disponíveis para os usuários funcionais ‘normais’.)

> **R-07 — Entry (E)**
>
> a) O grupo de dados de uma Entry disparadora pode consistir de apenas um atributo de dados que simplesmente informe o software que ‘um evento Y ocorreu’.  Muitas vezes, principalmente em software de aplicações de negócio, o grupo de dados da Entry disparadora possui diversos atributos que informam o software que ‘um evento Y ocorreu e aqui estão os dados sobre aquele evento específico’.
>
> b) Tiques de relógio que sejam eventos disparadores devem ser sempre externos ao software sendo medido.  Assim, por exemplo, um evento tique de relógio ocorrendo a cada 3 segundos deve estar associado a uma Entry movimentando um grupo de dados com um atributo de dados.  Notar que não faz diferença se o evento disparador é gerado periodicamente pelo hardware ou por outro pedaço de software fora da fronteira do software sendo medido.
>
> c) A não ser que um processo funcional específico seja necessário, obter a hora a partir do relógio do sistema não deve ser considerado como causa de uma Entry.
>
> d) Se uma ocorrência de um evento específico dispara a Entry de um grupo de dados compreendendo até ‘n’ atributos de dados de certo objeto de interesse e o RFU permitir que outras ocorrências do mesmo evento possam disparar uma Entry de um grupo de dados com valores apenas para um subconjunto dos ‘n’ atributos do objeto de interesse, então uma Entry deverá ser identificada compreendendo todos os ‘n’ atributos de dados.

> **R-08 — Exit (X)**
>
> a) Todas as mensagens geradas e enviadas por software sem dados do usuário (p.ex., mensagens de erro) devem ser consideradas como valores de um atributo de um objeto de interesse (o qual poderia ser denominado ‘indicação de erro’).  Dessa forma, uma única Exit deve ser identificada para representar todas essas ocorrências de mensagens dentro de cada processo funcional onde as mesmas sejam requeridas pelo RFU.
>
> b) Se uma Exit de um processo funcional movimenta um grupo de dados compreendendo até ‘n’ atributos de dados de certo objeto de interesse e o RFU permite que o processo funcional possua uma ocorrência de uma Exit que movimente um grupo de dados com valores apenas para um subconjunto dos ‘n’ atributos do objeto de interesse, então uma Exit deverá ser identificada, compreendendo todos os ‘n’ atributos de dados.

> **R-09 — Unicidade nas movimentações de dados e possíveis exceções**
>
> a) A não ser que os Requisitos Funcionais do Usuário especifiquem de outra forma, todos os atributos de dados descrevendo qualquer objeto de interesse que precisem ser submetidos a um processo funcional, bem como todas as manipulações de dados associadas devem ser identificados e contados como uma Entry (tipo).
>
> (Nota: Um processo funcional pode, é claro, precisar tratar diversos tipos de Entry, cada uma movimentando um grupo de dados descrevendo um objeto de interesse (tipo) diferente.)
>
> A mesma regra equivalente aplica-se a qualquer movimentação de dados Read, Write ou Exit em qualquer processo funcional.
>
> b) Pode ser identificada e contada mais que uma movimentação de dados Entry (tipo), cada uma movimentando um grupo de dados descrevendo o mesmo objeto de interesse (tipo) em um dado processo funcional (tipo), se houver um Requisito Funcional do Usuário para essas diversas Entries.  Similarmente, pode ser identificada e contada mais que uma Entry (tipo) movimentando o mesmo grupo de dados (tipo) no mesmo processo funcional, cada uma com uma manipulação de dados diferente associada (tipo) se houver um Requisito Funcional do Usuário para essas diversas Entries.
>
> Tais RFU podem surgir quando, em um processo funcional, as diversas Entries tiverem origem em diferentes usuários funcionais que submetam diferentes grupos de dados (cada um descrevendo o mesmo objeto de interesse).
>
> A mesma regra equivalente aplica-se a qualquer movimentação de dados Read, Write ou Exit em qualquer processo funcional.
>
> c) Ocorrências repetidas de um tipo de movimentação de dados (i.e., cada ocorrência movimentando o mesmo tipo de grupo de dados com a mesma manipulação de dados) não serão identificadas e contadas mais de uma vez em nenhum processo funcional
>
> d) Se as diversas *ocorrências* de um tipo de movimentação de dados em um processo funcional diferirem quanto à respectiva manipulação de dados porque diferentes valores dos atributos do grupo de dado movimentado conduzem a diferentes caminhos de processamento, o tipo de movimentação de dados não deve ser identificado e contado mais de uma vez naquele processo.

> **R-10 — Quando um processo funcional requer dados de um usuário funcional**
>
> a) Um processo funcional deve obter um grupo de dados através uma movimentação de dados Entry de um usuário funcional, quando a Entry *não precisa dizer ao usuário funcional quais dados devem ser enviados*, como em cada um dos seguintes quatro casos:
>
> - um usuário funcional envia uma Entry disparadora que inicia o processo funcional;
> - um processo funcional, tendo recebido uma Entry disparadora, entra em espera, aguardando a chegada de uma outra Entry enviada pelo usuário funcional (pode ocorrer quando um usuário funcional humano submete dados a um software aplicativo de negócio);
> - um processo funcional, tendo iniciado, solicita ao usuário funcional: ‘envie-me seus dados agora, se tiver algum’ e o usuário funcional envia seus dados;
> - um processo funcional, tendo iniciado, inspeciona o estado de um usuário funcional e recupera os dados de que necessita.
>
> Nos últimos dois casos (tipicamente ocorrendo em software ‘real-time’ fazendo ‘polling’), por convenção nenhuma Exit do processo funcional deve ser identificada na obtenção dos dados requeridos.  O processo funcional precisa apenas de enviar uma mensagem de aviso ao usuário funcional e a funcionalidade da mensagem de aviso é considerada parte da Entry.  O processo funcional sabe quais dados vai receber.  Apenas uma Entry é necessária neste caso.
>
> b) Quando um processo funcional precisa obter os serviços de um usuário funcional (por exemplo, para obter dados) e o usuário funcional precisa ser informado sobre o que enviar (normalmente quando o usuário funcional é outro pedaço de software fora do escopo do software sendo medido), um par de movimentações de dados Exit/Entry deve ser identificado.  A Exit contém a solicitação dos dados específicos; a Entry contém os dados retornados.

> **R-11 — Comandos de controle no domínio de aplicações de negócio**
>
> No domínio de aplicações de negócio ‘comandos de controle’ devem ser ignorados, pois os mesmos não envolvem movimentação de dados sobre um objeto de interesse.

> **R-12 — Agregação de resultados da medição**
>
> a) Para qualquer processo funcional, os tamanhos funcionais das movimentações de dados individuais devem ser agregados em um único valor de tamanho funcional em unidades de PFC, somando-os aritmeticamente:
>
> Tamanho (processo funcional<sub>i</sub>) = Σ tamanho(Entries<sub>i</sub>) + Σ tamanho(Exits<sub>i</sub>) + Σ tamanho(Reads<sub>i</sub>) + Σ tamanho(Writes<sub>i</sub>)
>
> b) Para qualquer processo funcional, o tamanho funcional das alterações em seus Requisitos Funcionais do Usuário deve ser agregado a partir dos tamanhos das movimentações de dados que tiverem sido incluídas, alteradas ou excluídas no processo funcional, produzindo como resultado o tamanho da mudança em unidades de PFC, de acordo com a seguinte fórmula:
>
> Tamanho (Mudança(processo funcional<sub>i</sub>)) = Σ tamanho (movimentações de dados incluídas <sub>i</sub>) + Σ tamanho (movimentações de dados alteradas <sub>i</sub>) + Σ tamanho (movimentações de dados excluídas <sub>i</sub>)
>
> Para mais informações sobre a agregação do tamanho funcional, ver seção 4.3.2.  Para a medição de software alterado, ver seção 4.4.
>
> c) O tamanho de um pedaço de software em um escopo definido deve ser obtido pela agregação dos tamanhos dos processos funcionais referentes ao pedaço de software, conforme as regras (e) e (f) abaixo
>
> d) O tamanho de qualquer mudança em um pedaço de software dentro de um escopo definido deve ser obtido agregando-se os tamanhos de todas as mudanças em todos os processos funcionais correspondentes ao pedaço, de acordo com as regras (e) e (f) abaixo.
>
> e) Os tamanhos de pedaços de software ou das mudanças em pedaços de software dentro de camadas podem ser somados somente se forem medidos no mesmo nível de granularidade de processo funcional de seu RFU.
>
> f) Os tamanhos de pedaços de software e/ou de mudanças em tamanhos de pedaços de software dentro de qualquer camada, ou de diferentes camadas devem ser somados somente se isso fizer sentido para o propósito da medição.
>
> g) O tamanho de um pedaço de software não pode ser obtido pela soma dos tamanhos de seus componentes (independentemente de como o item for decomposto) *a não ser que* as contribuições de tamanho das movimentações de dados entre componentes sejam eliminadas.
>
> h) Se o método COSMIC for ampliado localmente (por exemplo, para medir algum aspecto do tamanho não coberto pelo método padrão), então o tamanho medido através da extensão local deverá ser reportado separadamente conforme descrito na seção 5.1 e NÃO poderá ser somado ao tamanho obtido pelo método padrão medido em PFC (ver mais na seção 4.5)

> **R-13 — Alterando uma movimentação de dados**
>
> a) Se uma movimentação de dados deve ser alterada devido a uma mudança na manipulação de dados a ela associada, e/ou devido a uma mudança no número ou tipo de atributos no grupo de dados movimentado, um PFC alterado deve ser medido, independentemente do número de modificações na movimentação de dados.
>
> b) Se um grupo de dados deve ser modificado, as movimentações de dados movimentando o grupo de dados alterado cuja funcionalidade não for afetada pela alteração no grupo de dados não devem ser identificadas como movimentações de dados alteradas.
>
> NOTA 1:  Uma modificação no valor de uma ocorrência, tal como uma alteração em um código membro de um atributo cujos valores são um sistema de codificação não é uma alteração no tipo do atributo.
>
> NOTA 2:  Uma modificação em qualquer dado aparecendo nas telas de entrada ou saída que não seja relacionado a um objeto de interesse para um usuário funcional não deve ser identificada como um PFC alterado (ver seção 3.3.4 para exemplos de tais dados.)

> **R-14 — Rótulos das medições COSMIC**
>
> Um resultado de medição COSMIC deve ser designado como “**x** CFP (v.**y**)”, onde:
>
> - “**x**” representa o valor numérico do tamanho funcional,
>
> - “v.**y**” representa a identificação da versão do padrão COSMIC utilizado para obter o valor numérico do tamanho funcional “x”.
>
> NOTA:  Se um método de aproximação local foi utilizado para obter a medição, mas no demais a medição foi realizada utilizando as convenções de uma versão padrão COSMIC, a convenção acima deverá ser usada, mas a utilização do método de aproximação deverá ser anotada em outro lugar – ver seção 5.2.

> **R-15 — Rótulos em extensões locais COSMIC**
>
> Um resultado de medição COSMIC utilizando extensões locais deve ser designado como:
>
> “**x** CFP (v. **y**)  +  z PF Local”, onde:
>
> - “**x**” representa o valor numérico obtido agregando-se todos os resultados individuais de medição de acordo com o método padrão COSMIC, versão v.y,
>
> - “v.**y**” representa a identificação da versão padrão do método COSMIC utilizada para obter o valor numérico do tamanho funcional “x”.
>
> - “z” representa o valor numérico obtido agregando-se todos os resultados individuais de medição obtidos através de extensões locais para o método COSMIC.

> **R-16 — Reporte de medições COSMIC**
>
> Além das próprias medições, registradas conforme em 5.1, os seguintes atributos de cada medição deveriam ser registrados.
>
> a) Identificação do componente de software medido (nome, ID da versão ou ID da configuração).
>
> b) As fontes de informação utilizadas para identificar os RFU usados na medição
>
> c) O domínio do software
>
> d) Uma declaração do propósito da medição.
>
> e) Uma descrição do escopo da medição, bem como de sua relação com o escopo global de um conjunto de medições relacionadas, se existir.  (Utilizar as categorias de escopo genéricas na seção 2.2)
>
> f) Os usuários funcionais do software
>
> g) O nível de granularidade do RFU e o nível de decomposição do software.
>
> h) O ponto no ciclo de vida do projeto onde a medição foi feita (especialmente se a medição for uma estimativa baseada em RFU incompletos, ou se foi feita com base em funcionalidade realmente entregue).
>
> i) O alvo ou margem de erro imaginada para a medição.
>
> j) Uma indicação se o método padrão de medição COSMIC foi utilizado e/ou uma aproximação local para o método padrão, e/ou extensões locais foram utilizadas (ver seção 4.5). Utilizar as convenções para rótulos das seções 5.1 ou 5.2.
>
> k) Uma indicação se a medição é de funcionalidade desenvolvida ou entregue (funcionalidade ‘desenvolvida’ é obtida criando-se novo software; funcionalidade ‘entregue’ inclui funcionalidade ‘desenvolvida’ e também inclui funcionalidade obtida por outros meios além da criação de novo software, i.e., incluindo-se todas as formas de reuso de software existente, utilização de parâmetros existentes para incluir ou alterar funcionalidades, etc.).
>
> l) Uma indicação se a medição é de funcionalidade nova ou é o resultado de uma atividade de ‘melhoria’ (i.e., a soma de funcionalidade incluída, alterada e excluída – ver 4.4).
>
> m) A descrição de uma arquitetura de camadas nas quais a medição é feita, se aplicável.
>
> n) O número de componentes principais, se aplicável, cujos tamanhos foram somados para obter o tamanho total registrado.
>
> o) Uma matriz de medição para cada escopo dentro do escopo global da medição, conforme especificado no apêndice A.
>
> p) O nome do medidor e quaisquer qualificações referentes à certificação COSMIC.
