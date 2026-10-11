<!-- Gerado por scripts/gera-docs.py a partir de MFO/exemplos/codigo-biblioteca/README.md. Não edite: edite a fonte e gere de novo. -->
# Código de exemplo — sistema de biblioteca (v1 e v2)

Implementação mínima, em Python sem dependências, dos requisitos do capítulo 6
(RF-01 a RF-09 na `v1/`; RF-07 e RF-08 revisados e RF-10 na `v2/`). Serve para
demonstrar a medição a partir do código e do diff (capítulo 8):

- cada função pública de `servicos.py` é um processo; `api.py` e `jobs.py` são os
  disparadores (rotas e job diário);
- `repositorio.py` concentra os movimentos R e W; `email_cliente.py` é o usuário
  funcional externo (X ao enviar, E no status devolvido);
- as evidências do modelo [`../biblioteca-v2.mfc.json`](https://github.com/andromarcio/metricas-software/blob/main/MFO/exemplos/biblioteca-v2.mfc.json)
  apontam para estes arquivos no formato `COD:v2/biblioteca/<arquivo>#<trecho>` e são
  verificadas por `mfo.py auditar`.

Teste rápido (a partir da raiz do repositório):

```bash
python3 -I -c "
import sys; sys.path.insert(0, 'MFO/exemplos/codigo-biblioteca/v2')
from datetime import date
from biblioteca import api, repositorio
repositorio.conectar()
print(api.tratar('POST /livros', {'isbn': '1', 'titulo': 'Dom Casmurro', 'autor': 'Machado', 'ano': 1899, 'quantidade': 1}))
print(api.tratar('POST /leitores', {'cpf': '1', 'nome': 'Ana', 'email': 'ana@x.br', 'telefone': '', 'situacao': 'ativo'}))
print(api.tratar('POST /emprestimos', {'cpf': '1', 'isbn': '1', 'data': '2026-01-01'}))
print(api.tratar('POST /emprestimos/{id}/devolucao', {'data_devolucao': '2026-01-20', 'isencao_multa': True, 'justificativa_isencao': 'greve'}, {'id': 1}))
print(api.tratar('GET /leitores/{cpf}', None, {'cpf': '1'}))
"
```
