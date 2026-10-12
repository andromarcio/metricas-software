"""Pontos de entrada expostos ao bibliotecário (PFC: disparadores dos processos P01 a P08 e P10)."""
from datetime import date

from . import servicos

# Rota -> processo. A chave é a evidência citada no modelo PFC ("COD:...api.py#POST /livros").
ROTAS = {
    "POST /livros": lambda corpo, params: servicos.cadastrar_livro(corpo),
    "PUT /livros/{isbn}": lambda corpo, params: servicos.alterar_livro(params["isbn"], corpo),
    "DELETE /livros/{isbn}": lambda corpo, params: servicos.excluir_livro(params["isbn"]),
    "GET /livros": lambda corpo, params: servicos.consultar_livros(params.get("titulo"), params.get("autor")),
    "POST /leitores": lambda corpo, params: servicos.cadastrar_leitor(corpo),
    "POST /emprestimos": lambda corpo, params: servicos.registrar_emprestimo(
        corpo["cpf"], corpo["isbn"], date.fromisoformat(corpo["data"])),
    "POST /emprestimos/{id}/devolucao": lambda corpo, params: servicos.registrar_devolucao(
        int(params["id"]), date.fromisoformat(corpo["data_devolucao"]),
        bool(corpo.get("isencao_multa", False)), corpo.get("justificativa_isencao", "")),
    "GET /relatorios/atrasos": lambda corpo, params: servicos.relatorio_atrasos(date.today()),
    "GET /leitores/{cpf}": lambda corpo, params: servicos.consultar_leitor(params["cpf"]),
}


def tratar(rota: str, corpo: dict = None, params: dict = None) -> dict:
    """Despacha uma requisição; erros de negócio viram desfechos (RI-12)."""
    try:
        return ROTAS[rota](corpo or {}, params or {})
    except servicos.ErroDeNegocio as erro:
        return {"erro": str(erro)}
