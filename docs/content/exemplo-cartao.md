<!-- Gerado por scripts/gera-docs.py a partir de MFO/exemplos/cartao/autorizacao-requisitos.md. Não edite: edite a fonte e gere de novo. -->
# Autorização de compra com cartão — requisitos ilustrativos

Exemplo hipotético, simplificado, de um autorizador de compras com cartão, usado no
capítulo 12 para comparar as duas dimensões da MFO. Os códigos de resposta são
ilustrativos e seguem o espírito da ISO 8583, não uma tabela de bandeira específica.

## RF-01 Autorizar compra

A rede ou adquirente envia a mensagem de autorização (dados do cartão, valor, moeda, estabelecimento, canal, criptograma, dados de senha quando houver). O autorizador decide em tempo real e responde à rede com código de resposta, valor autorizado e código de autorização.

### Regras de negócio

1. O cartão deve existir e estar ativo.
2. O cartão não pode estar vencido.
3. O cartão não pode constar da lista de bloqueio.
4. O portador deve estar ativo.
5. O estabelecimento não pode estar bloqueado.
6. A categoria do estabelecimento (MCC) deve ser permitida para o produto do cartão.
7. O limite disponível deve cobrir o valor, considerando as reservas vigentes.
8. Em cartão de débito, o saldo da conta deve cobrir o valor.
9. O valor não pode exceder o limite por transação do produto.
10. A quantidade de transações do cartão no período não pode exceder o parâmetro de velocidade.
11. O criptograma da transação deve ser válido.
12. Quando houver senha, ela deve ser válida e o número de tentativas não pode exceder três.
13. O score de fraude devolvido pelo motor antifraude deve ficar abaixo do limiar do produto.
14. Compra em moeda estrangeira é convertida pela cotação do dia (cálculo).
15. Quando o saldo for menor que o valor e o produto permitir, autoriza-se parcialmente pelo saldo disponível (cálculo).
16. A reserva de limite é igual ao valor autorizado (cálculo).
17. Transação repetida (mesmo identificador na janela de duplicidade) é recusada.
18. O canal da compra (presencial, não presencial) deve estar habilitado para o cartão.
19. Toda negativa incrementa o contador de negativas do cartão no dia, sem resposta própria (regra de estado).

### Regras de prevenção à fraude

Todas respondem com o mesmo código 59, por decisão de segurança: a rede e o portador não devem saber qual regra recusou. Cada regra tem teste de aceite próprio, com a entrada que a dispara.

20. Mais de cinco compras em dez minutos no mesmo cartão.
21. Compras em países diferentes com intervalo incompatível com deslocamento.
22. Primeiro uso do cartão em categoria de alto risco com valor acima do limiar.
23. Sequência de valores crescentes no mesmo estabelecimento em uma hora (teste de cartão).
24. Estabelecimento e dispositivo presentes na lista de associação a fraude.
25. Valor exatamente igual ao limite disponível após três recusas por limite.

### Códigos de resposta à rede

| Código | Desfecho |
|---|---|
| 00 | aprovada |
| 10 | aprovada parcialmente |
| 14 | cartão inválido |
| 54 | cartão vencido |
| 62 | cartão bloqueado |
| 41 | portador bloqueado |
| 03 | estabelecimento inválido |
| 57 | categoria não permitida |
| 51 | saldo ou limite insuficiente |
| 61 | excede limite por transação |
| 65 | excede frequência de transações |
| 88 | criptograma inválido |
| 55 | senha inválida |
| 75 | tentativas de senha excedidas |
| 59 | suspeita de fraude (score acima do limiar e qualquer regra de prevenção, 20 a 25) |
| 94 | transação duplicada |
| 58 | canal não permitido |
| 30 | erro de formato |

### Dados lidos e gravados

| Entidade | Papel |
|---|---|
| Transacao | grava e devolve |
| Cartao | lê |
| Portador | lê |
| Conta | lê e grava (reserva de limite) |
| Estabelecimento | lê |
| ParametroAutorizacao | lê |
| ListaBloqueio | lê |
| Cotacao | lê |
| ScoreFraude | recebido do motor antifraude |
