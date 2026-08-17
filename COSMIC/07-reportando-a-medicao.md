# 5 Reportando a Medição

> Método COSMIC v3.0.1 — Manual de Medição

O Modelo Genérico de Software pode ser apresentado em forma de matriz, onde as linhas representam processos funcionais (os quais podem ser agrupados por camadas), as colunas representam grupos de dados e as células contêm os subprocessos identificados (Entry, Exit, Read e Write). Esta representação do Modelo Genérico de Software é apresentada no apêndice A.

Os resultados de medições COSMIC devem ser reportados e arquivados de acordo com as convenções seguintes.

## 5.1 Rotulando

Ao reportar um tamanho funcional COSMIC, o mesmo deve ser rotulado de acordo com a seguinte convenção, em conformidade com o padrão ISO/IEC 14143-1: 2007:

> **REGRA – Rótulos das medições COSMIC**
>
> Um resultado de medição COSMIC deve ser designado como “**x** CFP (v.**y**)”, onde:
>
> - “**x**” representa o valor numérico do tamanho funcional,
>
> - “v.**y**” representa a identificação da versão do padrão COSMIC utilizado para obter o valor numérico do tamanho funcional “x”.
>
> NOTA:  Se um método de aproximação local foi utilizado para obter a medição, mas no demais a medição foi realizada utilizando as convenções de uma versão padrão COSMIC, a convenção acima deverá ser usada, mas a utilização do método de aproximação deverá ser anotada em outro lugar – ver seção 5.2.

EXEMPLO: Um resultado obtido utilizando-se as regras deste Manual de Medição é designado como ‘x CFP (v3.0.1)’

Quando forem utilizadas extensões locais, conforme definido na seção 4.5 acima, o resultado da medição deverá ser reportado conforme definido abaixo.

> **REGRA – Rótulos em extensões locais COSMIC**
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

## 5.2 Arquivando os resultados de medição COSMIC

Ao arquivar resultados de medições COSMIC, as seguintes informações devem ser mantidas para garantir que o resultado sempre seja interpretável:

> **REGRA– Reporte de medições COSMIC**
>
> Além das próprias medições, registradas conforme em 5.1, os seguintes atributos de cada medição deveriam ser registrados.
>
> a) Identificação do componente de software medido (nome, ID da versão ou ID da configuração).
>
> b) As fontes de informação utilizadas para identificar os RFU usados na medição
>
> c) O domínio do software
>
> d) Uma declaração do propósito da medição
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
> j) Uma indicação se o método padrão de medição COSMIC foi utilizado e/ou uma aproximação local para o método padrão, e/ou se extensões locais foram utilizadas (ver seção 4.5). Utilizar as convenções para rótulos das seções 5.1 ou 5.2.
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
