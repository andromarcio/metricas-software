<!-- Gerado por scripts/gera-docs.py a partir de MFO/prompts/extracao-mfc.md. Não edite: edite a fonte e gere de novo. -->
# Prompt de extração do Modelo Funcional Canônico (MFC) — MFO 1.0

Use este prompt com um modelo de linguagem para produzir o modelo JSON que a ferramenta
`mfo.py` valida e conta. Substitua os campos entre `<...>`. Anexe ou cole os artefatos
(requisitos, telas, contratos de API, código, esquema de banco). Em bases grandes, rode o
prompt por módulo e consolide os modelos (RC-04). Registre a versão deste prompt e o
modelo de IA usado no campo `agente` (o texto do prompt faz parte do agente).

---

```text
Você é um medidor de tamanho funcional de software que aplica o método MFO 1.0
(Medição Funcional Objetiva). Sua tarefa NÃO é calcular um número: é produzir um
Modelo Funcional Canônico (MFC) em JSON, com evidências, que uma ferramenta contará.
Qualquer elemento que você não consiga sustentar com evidência deve ser marcado como
inferido, com justificativa. Não invente processos, entidades ou movimentos.

## Contexto da medição
- Software: <nome e versão>
- Propósito: <por que se mede>
- Escopo: <o que está incluído; o que está excluído>
- Nível: <R | C | RC>  (R = a partir de requisitos; C = a partir de código/sistema; RC = ambos, conciliados)
- Fontes (id, tipo, referência com versão):
  - <REQ, requisitos, docs/requisitos.md@v1.2>
  - <COD, codigo, git:abc123>
- Usuários funcionais conhecidos: <lista, ou "identifique">
- Glossário de entidades (use exatamente estes nomes quando couber): <lista, ou "identifique">

## Conceitos e regras (resumo normativo)
1. Fronteira (RI-01): o software medido está de um lado; usuários funcionais do outro.
   O armazenamento que o software lê ou grava diretamente fica dentro (R/W), mesmo se
   mantido por outra aplicação. Sistemas acessados por chamada ou mensagem são usuários
   funcionais (E/X).
2. Usuário funcional (RI-02): pessoa, sistema, dispositivo ou relogio. Perfis que disparam
   os mesmos processos são um único usuário funcional.
3. Entidade (RI-03): grupo nomeado de atributos que descreve UMA coisa de interesse,
   persistida ou trocada como unidade. Projeções/DTOs/telas da mesma coisa = mesma
   entidade. Atributos pertencem à entidade que os persiste (coluna da tabela); o nome
   de uma entidade referenciada é atributo dela, não da que referencia. NÃO são
   entidades: tabelas de domínio código/descrição, configuração técnica, sessão, token,
   cache, índice, log técnico, tabela associativa sem atributos próprios. SÃO entidades:
   parâmetros de negócio com atributos próprios ou mantidos pelo usuário; trilha de
   auditoria exigida pelo usuário.
4. Processo (RI-04): menor unidade com (T1) disparador que carrega pelo menos uma E,
   (T2) efeito: pelo menos uma W ou X, (T3) autonomia: ao terminar, nada mais é
   obrigatório para o efeito valer. Criar, alterar, excluir, consultar e cada mudança de
   estado (aprovar, cancelar) são processos distintos. NÃO geram processos distintos:
   canal (tela/API/arquivo), formato (tela/PDF/CSV), filtros, ordenação, paginação,
   navegação, confirmações, subconjuntos opcionais de entrada, caminhos de validação.
   Etapas de um assistente que só gravam ao final = um processo. Lista e detalhe são
   distintos só se o detalhe mostra atributos ou entidades a mais. Comandos de controle
   (menu, sair, limpar, ordenar) não são processos. Um processo pode ter vários disparadores.
5. Movimentos — a chave é (processo, tipo, entidade); cada chave conta uma vez (RI-09):
   - E (RI-05): uma por entidade cujos atributos entram vindos de um usuário funcional,
     incluindo o disparador. Disparador sem atributos de entidade (tique de relógio,
     botão sem parâmetros) = E DISPARO. Resposta de sistema externo conta como E da
     entidade que descreve SOMENTE se o processo usa seus atributos.
   - X (RI-06): uma por entidade cujos atributos saem para um usuário funcional (tela,
     resposta, arquivo, mensagem, chamada a outro sistema). Saída com atributos de três
     entidades = três X. Mensagens de erro/validação/sucesso/estado e identificadores
     gerados (protocolo, token) = no máximo UMA X MENSAGEM por processo. Rótulos,
     títulos, textos fixos e navegação não geram X.
   - R (RI-07): uma por entidade da qual o processo obtém atributos do armazenamento para
     decidir, transformar ou enviar. Verificação de existência implícita na gravação não
     é R; verificação que lê atributos para decidir é R. Domínio, configuração, cache,
     sessão não são R.
   - W (RI-08): uma por entidade criada, alterada ou excluída no armazenamento persistente
     (as três ações na mesma entidade e processo = uma W). Log técnico, cache, sessão,
     intermediários não são W. Auditoria exigida pelo usuário é W de Auditoria.
6. Exclusões (RI-10): infraestrutura, framework, autenticação/autorização embutida em
   cada chamada (só o processo "autenticar" conta), erros técnicos, retentativas,
   transações, migrações, testes, build, telemetria, código morto, endpoints de saúde.
7. Evidência (RI-11): todo processo e todo movimento tem "evidencia": ["FONTE:localizador"]
   com FONTE declarada e localizador que permita abrir o artefato e confirmar (id de
   requisito, rota, símbolo com caminho, tabela/coluna, nome de tela ou mensagem).
   Sem evidência localizável: "inferido": true e "justificativa".
8. Decisões (RC-05, capítulo 12): cada processo leva o bloco "decisoes", contado à parte e
   nunca somado ao PFO. "desfechos" (D1, base contratual): o desfecho principal, cada
   variante de sucesso com efeito diferente e cada recusa ou erro de negócio distinto por
   código, por mensagem ou, sob o mesmo código, pela condição de entrada que o dispara,
   desde que declarada na fonte; esta última leva "oculto": true. "regras" (D2,
   diagnóstico): cada regra de negócio enumerada na fonte que valida, restringe, muda
   estado ou calcula. Erros técnicos (RI-10) e regras de apresentação ficam fora. Cada
   item tem "id" único na lista, "descricao" e "evidencia".

## Casos frequentes (decisões fixadas)
- Cadastro com unicidade (CPF único): E, R (verifica), W, X MENSAGEM.
- Alterar: E, R, W, X MENSAGEM (a exibição prévia é o processo de consulta).
- Excluir com bloqueio por dependentes: E, R (dependentes), W, X MENSAGEM. Sem verificação: E, W, X MENSAGEM.
- Lista com filtros: E (filtros), R, X, X MENSAGEM ("nenhum registro").
- Relatório sem parâmetros: E DISPARO, R..., X por entidade exibida, X MENSAGEM.
- Autenticar: E Usuario, R Usuario, X MENSAGEM. Logout: não é processo. Trocar senha: E, R, W, X MENSAGEM.
- Job que envia e-mails por serviço externo: E DISPARO, R..., X por entidade enviada, E (status devolvido, se usado), W (se registra).
- Consumidor de fila / webhook: E (entidade da mensagem), R..., W..., X MENSAGEM (se responde erro).
- Mesma função por tela e API: um processo, dois disparadores. Lote com relatório de rejeições além da entrada on-line: dois processos.

## Procedimento
1. Liste os usuários funcionais (id, nome, tipo).
2. Liste as entidades com atributos e evidência; aplique as exclusões.
3. Liste os candidatos a processo (pontos de entrada acessíveis a usuários funcionais) e
   aplique T1, T2, T3 e os desempates. Dê ids estáveis (P01, P02, ...) e nomes verbo+objeto.
4. Para cada processo, liste os movimentos na ordem E, R, W, X, com atributos quando
   conhecidos e evidência em cada um. Inclua a X MENSAGEM quando o processo emite
   mensagens. Não repita chaves.
5. Autoverifique: todo processo tem E; todo processo tem X ou W; toda entidade declarada é
   usada; MENSAGEM só em X e no máximo uma por processo; DISPARO só em E; nenhuma chave
   repetida; toda evidência tem prefixo de fonte declarada; dois processos com as mesmas
   chaves e atributos provavelmente são um só.
6. Responda SOMENTE com o JSON abaixo, sem comentários.

## Formato de saída
{
  "mfo": "1.0",
  "software": "<nome>", "versao": "<versão>",
  "proposito": "<...>", "escopo": "<...>", "nivel": "<R|C|RC>",
  "agente": { "tipo": "ia", "nome": "<modelo e versão>", "revisao_humana": false, "prompt": "extracao-mfc.md@1.0" },
  "fontes": [ { "id": "<REQ>", "tipo": "<requisitos|prototipo|api|codigo|banco|sistema|outro>", "ref": "<caminho@versão>" } ],
  "usuarios_funcionais": [ { "id": "UF1", "nome": "<...>", "tipo": "<pessoa|sistema|dispositivo|relogio>" } ],
  "entidades": [ { "id": "<Nome>", "descricao": "<...>", "atributos": ["<...>"], "evidencia": ["<FONTE:loc>"] } ],
  "processos": [
    {
      "id": "P01", "nome": "<Verbo objeto>",
      "disparadores": [ { "usuario": "UF1", "evento": "<o que acontece>" } ],
      "evidencia": ["<FONTE:loc>"],
      "movimentos": [
        { "tipo": "E", "entidade": "<Nome ou DISPARO>", "atributos": ["<...>"], "evidencia": ["<FONTE:loc>"] },
        { "tipo": "R", "entidade": "<Nome>", "atributos": ["<...>"], "evidencia": ["<FONTE:loc>"] },
        { "tipo": "W", "entidade": "<Nome>", "atributos": ["<...>"], "evidencia": ["<FONTE:loc>"] },
        { "tipo": "X", "entidade": "<Nome>", "atributos": ["<...>"], "evidencia": ["<FONTE:loc>"] },
        { "tipo": "X", "entidade": "MENSAGEM", "evidencia": ["<FONTE:loc>"] }
      ],
      "decisoes": {
        "desfechos": [
          { "id": "OK", "descricao": "<desfecho principal>", "tipo": "sucesso", "evidencia": ["<FONTE:loc>"] },
          { "id": "<CODIGO>", "descricao": "<causa da recusa>", "tipo": "recusa", "evidencia": ["<FONTE:loc>"] },
          { "id": "<CODIGO>/2", "descricao": "<outra causa sob o mesmo código>", "tipo": "recusa", "oculto": true, "evidencia": ["<FONTE:loc>"] }
        ],
        "regras": [ { "id": "R1", "descricao": "<regra>", "tipo": "<validacao|limite|estado|calculo>", "evidencia": ["<FONTE:loc>"] } ]
      }
    }
  ]
}

## Artefatos
<cole ou anexe aqui>
```

---

## Prompt complementar: conciliação de duas medições

Após `mfo.py concordancia A.json B.json`, use o prompt abaixo para fechar as divergências
por regra. A saída esperada é um registro por divergência; a decisão final é humana
quando a medição tem efeito contratual.

```text
Você recebe duas medições MFO 1.0 do mesmo software (A e B) e a lista de chaves
(processo, tipo, entidade) presentes em apenas uma delas. Para cada chave divergente:
1. Localize a evidência citada em cada modelo e abra o artefato.
2. Decida se a chave deve existir aplicando a regra pertinente (RI-03 a RI-10), citando-a.
3. Responda no formato: "<chave> — <regra> — <decisão: manter|remover> — <evidência que decide>".
Não altere chaves que estão nas duas medições. Não proponha pesos nem ajustes no total.
```

---

## Prompt complementar: atribuição do modo de produção (capítulo 9)

Use depois da extração de nível C, com acesso ao histórico do repositório (git), às PRs
e, quando houver, aos logs de sessão de agentes. A saída alimenta `producao.modo` de cada
processo e é auditada por amostragem.

```text
Você recebe um Modelo Funcional Canônico (MFO 1.0) de nível C e o histórico do
repositório entre as versões <REF_A> e <REF_B>. Para cada processo do modelo:
1. Liste os commits que tocam os arquivos citados nas evidências COD do processo
   (git log <REF_A>..<REF_B> -- <arquivos>).
2. Para cada commit, registre: autor, trailers de coautoria (Co-Authored-By), PR de
   origem, quem aprovou a PR e se há log de sessão de agente associado.
3. Atribua o modo pela regra RP-01: M0 (nenhum commit com IA), M1 (minoria dos commits
   com IA, pessoa escreveu), M2 (maioria dos commits com coautoria de IA e revisão
   humana registrada), M3 (PR aberta por agente, testes gerados, intervenção humana só
   no aceite). Sem evidência suficiente: "nd".
4. Responda com um objeto JSON por processo:
   {"id": "<processo>", "producao": {"modo": "<M0|M1|M2|M3|nd>", "evidencia": ["PROC:<commits, PR e logs>"], "nota": "<como decidiu>"}}
Não altere movimentos nem tamanhos. Não infira modo pelo estilo do código: só por
evidência de autoria.
```
