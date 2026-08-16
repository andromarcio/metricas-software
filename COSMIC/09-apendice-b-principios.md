# Apêndice B — Resumo dos Princípios do Método COSMIC

> Método COSMIC v3.0.1 — Manual de Medição

Para fins de referência precisa, a tabela abaixo identifica cada princípio encontrado no Método de Medição COSMIC.

> **P-01 — O Modelo de Contexto de Software COSMIC**
>
> a) O Software é delimitado pelo hardware
>
> b) O software é normalmente estruturado em **camadas**
>
> c) Uma camada pode conter um ou mais pedaços de software ‘**pares**’ distintos e qualquer pedaço de software pode ser composto de componentes pares distintos
>
> d) Qualquer pedaço de software a ser medido deverá ser definido por seu **escopo** de medição, o qual deve estar integralmente contido em uma única camada
>
> e) O escopo de um pedaço de software a ser medido depende do **propósito** da medição
>
> f) Os **usuários funcionais** de um pedaço de software devem ser identificados a partir dos requisitos funcionais do usuário do pedaço de software a ser medido, como fontes e/ou destinos pretendidos para os dados
>
> g) Um pedaço de software interage com os seus usuários funcionais por meio de **movimentações de dados** através de uma **fronteira**, e o pedaço de software pode mover dados de e para o **armazenamento persistente** dentro da fronteira
>
> h) Os RFU do software podem ser expressos a diferentes **níveis de granularidade**
>
> i) O nível de granularidade ao qual as medições devem ser normalmente efetuadas é o dos **processos funcionais**
>
> j) Se não for possível medir ao nível de granularidade dos processos funcionais, nesse caso os RFU do software devem ser medidos através de uma abordagem de aproximação e escalonados para o nível de granularidade dos processos funcionais

> **P-02 — O Modelo Genérico de Software COSMIC**
>
> a) O software recebe dados de **entrada** dos seus usuários funcionais e produz **saídas** e/ou outros resultados para os usuários funcionais
>
> b) Os requisitos dos usuários funcionais de um pedaço de software a ser medido podem ser mapeados para processos funcionais únicos
>
> c) Cada processo funcional consiste de **subprocessos**
>
> d) Um subprocesso pode ser uma movimentação de dados ou uma **manipulação de dados**
>
> e) Cada processo funcional é disparado por um movimento de dados do tipo **Entry** proveniente de um usuário funcional, o qual informa ao processo funcional que o usuário funcional identificou um **evento**
>
> f) Uma movimentação de dados movimenta um único **grupo de dados**
>
> g) Um grupo de dados consiste de um único conjunto de **atributos de dados** que descreve um único objeto de interesse
>
> h) Há quatro tipos de movimentação de dados. Uma **Entry** movimenta um grupo de dados para dentro do software, a partir de um usuário funcional. Uma **Exit** movimenta um grupo de dados para fora do software, em direção a um usuário funcional. Um **Write** movimenta um grupo de dados do software para o armazenamento persistente. Um **Read** movimenta um grupo de dados do armazenamento persistente para o software
>
> i) Um processo funcional deve incluir pelo menos uma movimentação de dados Entry e uma movimentação de dados Write ou Exit, ou seja, deve incluir um mínimo de duas movimentações de dados
>
> j) Como uma aproximação para fins de medição, os subprocessos de manipulação de dados não são medidos separadamente; assume-se que a funcionalidade de qualquer manipulação de dados será considerada na movimentação de dados com a qual a mesma esteja associada

> **P-03 — O princípio de medição COSMIC**
>
> O tamanho funcional de um pedaço de software é diretamente proporcional ao número de suas movimentações de dados.

> **P-04 — Camada**
>
> a) O software em uma camada troca dados com o software em outra camada através dos seus respectivos processos funcionais.
>
> b) A ‘dependência hierárquica’ entre camadas é tal que o software em qualquer camada pode utilizar os serviços funcionais de qualquer software em qualquer camada abaixo dele na hierarquia.  Onde há tais relações de uso, denominamos a camada que utiliza o software abaixo como ‘superior’ e qualquer camada contendo software utilizado como sua ‘subordinada’.  O software na camada superior apoia-se nos serviços de software dessas camadas subordinadas para rodar adequadamente; estas últimas apoiam-se por sua vez em suas camadas subordinadas para rodar adequadamente, e assim em toda a hierarquia.  Por outro lado, o software em uma camada subordinada, juntamente com o software em quaisquer camadas subordinadas da qual ele depende, pode rodar sem precisar dos serviços de nenhuma camada superior na hierarquia.
>
> c) O software em uma camada não utiliza, necessariamente, todos os serviços funcionais providos pelo software em uma camada subordinada.
>
> d) Os dados que são trocados entre pedaços de software em quaisquer duas camadas são definidos e interpretados diferentemente nos respectivos RFU dos dois pedaços de software, isto é, os dois pedaços de software reconhecem diferentes atributos de dados e/ou subgrupos de dados sendo trocados. Contudo, devem existir também um ou mais atributos de dados ou subgrupos definidos em comum, para permitir que o software na camada recebedora interprete os dados passados pelo software na camada remetente, de acordo com as necessidades do software recebedor.

> **P-05 — Componente par**
>
> a) Em um conjunto de componentes pares de um pedaço de software em uma camada não há dependência hierárquica entre os componentes pares da forma que há entre camadas.  Os RFU de todos os componentes pares de um pedaço de software em uma camada estão no mesmo ‘nível’ na hierarquia de camadas.
>
> b) Todos os componentes pares de um pedaço de software devem cooperar para que o pedaço de software execute com sucesso.
>
> c) Um grupo de dados pode ser diretamente trocado entre dois componentes pares de um pedaço de software, por um processo funcional de um primeiro componente emitindo uma Exit recebida como uma Entry por um processo funcional do segundo componente.  Alternativamente, a troca pode acontecer de forma indireta, com um processo funcional de um primeiro componente tornando um grupo de dados persistente através de um Write, que pode ser recuperado em seguida por um Read de um processo funcional do segundo componente.

> **P-06 — Aplicando o Modelo Genérico de Software COSMIC**
>
> O Modelo Genérico de Software COSMIC deve ser aplicado aos requisitos funcionais do usuário de cada pedaço de software distinto para o qual um escopo de medição distinto tenha sido definido.
>
> 'Aplicando o Modelo Genérico de Software COSMIC' diz respeito à identificação do conjunto de eventos disparadores percebidos por cada um dos (tipos de) usuários funcionais identificados nos RFU, seguida pela identificação dos correspondentes processos funcionais, objetos de interesse, grupos de dados e movimentações de dados que devem ser providos como resposta a esses eventos.

> **P-07 — Grupo de dados**
>
> a) Cada grupo de dados identificado deve ser único e distinguível através de sua coleção única de atributos de dados
>
> b) Cada grupo de dados deve ser diretamente relacionado a um objeto de interesse nos Requisitos Funcionais do Usuário
>
> c) Um grupo de dados deve ser materializado dentro do sistema de computador que suporta o software.

> **P-08 — Entry (E)**
>
> a) Uma Entry deve movimentar um único grupo de dados descrevendo um único objeto de interesse de um usuário funcional através da fronteira e para dentro do processo funcional do qual a Entry faz parte.  Se a entrada para um processo funcional compreender mais de um grupo de dados, identificar uma Entry para cada grupo de dados distinto na entrada.  (Ver tambem a seção 4.1.7 sobre ‘Unicidade nas movimentações de dados’.)
>
> b) Uma Entry não deve enviar dados para fora da fronteira, ler ou gravar dados.
>
> c) Quando um processo funcional precisar obter dados de um usuário funcional e este último não precisar saber quais dados enviar, ou quando o usuário funcional for incapaz de reagir a uma mensagem a ele destinada, identificar uma Entry para o processo funcional pela obtenção dos dados.  Nenhuma mensagem do processo funcional ao usuário funcional procurando recuperar os dados deve ser contada como Exit nesses casos.
>
> Contudo, quando um processo funcional precisar obter dados de um usuário funcional e o processo funcional precisar fornecer dados ao usuário funcional, dos quais este último precise para atender ao solicitado, contar uma Exit para a solicitação e uma Entry para o retorno dos dados solicitados (ver seção 4.1.9 adiante).

> **P-09 — Exit (X)**
>
> a) Uma Exit deve movimentar um único grupo de dados descrevendo um único objeto de interesse do processo funcional do qual a Exit faz parte através da fronteira para um usuário funcional.  Se a saída de um processo funcional compreender mais de um grupo de dados, identificar uma Exit para cada grupo de dados distinto na saída. (Ver também a seção 4.1.7 sobre ‘Unicidade nas movimentações de dados’.)
>
> b) Uma Exit não deve enviar dados para dentro da fronteira, ler ou gravar dados.

> **P-10 — Read (R)**
>
> a) Um Read deve movimentar um único grupo de dados descrevendo um único objeto de interesse do armazenamento persistente para um processo funcional do qual o Read faz parte.  Se o processo funcional precisar recuperar mais do que um grupo de dados do armazenamento persistente, identificar um Read para cada grupo de dados distinto recuperado.  (Ver também seção 4.1.7 sobre ‘Unicidade na movimentação de dados’.)
>
> b) Um Read não deve receber ou enviar dados para fora da fronteira, ou gravar dados.
>
> c) Durante um processo funcional, a movimentação ou manipulação de constantes ou variáveis internas ao processo funcional que possam ser alteradas somente por um programador, o cálculo de resultados intermediários, ou de dados armazenados por um processo funcional como resultado apenas da implementação e não dos RFU não devem ser consideradas movimentações de dados Read.
>
> d) Uma movimentação de dados Read sempre inclui qualquer funcionalidade do tipo ‘solicitação de leitura’ (assim uma movimentação de dados distinta nunca será contada para uma funcionalidade do tipo ‘solicitação de leitura’). Ver também a seção 4.1.9.

> **P-11 — Write (W)**
>
> a) Um Write deve movimentar um único grupo de dados para o armazenamento persistente, descrevendo um único objeto de interesse do processo funcional do qual o Write faz parte.  Se o processo funcional precisar movimentar mais de um grupo de dados para o armazenamento persistente, identificar um Write para cada grupo de dados distinto que for movimentado para o armazenamento persistente. (Ver também a seção 4.1.7 sobre ‘Unicidade nas movimentações de dados’.)
>
> b) Um Write não deve receber ou enviar dados através da fronteira, ou ler dados.
>
> c) Um requisito para excluir um grupo de dados do armazenamento persistente deve ser medido como uma única movimentação de dados Write.
>
> d) No decorrer de um processo funcional, movimentações ou manipulações de dados que não persistirem quando o processo funcional estiver concluído, que atualizem variáveis internas ao processo funcional, ou que produzam resultados intermediários em um cálculo não devem ser consideradas movimentações de dados Write.

> **P-12 — Manipulações de dados associadas a movimentações de dados**
>
> Todas as manipulações de dados em um processo funcional devem estar associadas aos quatro tipos de movimentações de dados (E, X, R e W).  Por convenção, assume-se que as movimentações de dados de um processo funcional também representam as manipulações de dados do processo funcional.
