"""Processos do sistema (MFO: RI-04). Cada função pública é um processo disparado por api.py ou jobs.py."""
from datetime import date, timedelta
from typing import Callable, Dict, List, Optional

from . import repositorio
from .modelos import Emprestimo, Leitor, Livro, Notificacao

PRAZO_DIAS = 14
LIMITE_EMPRESTIMOS = 3


class ErroDeNegocio(Exception):
    """Mensagens de validação e recusa devolvidas ao usuário funcional (MFO: desfechos, RI-12)."""


# ---- P01 Cadastrar livro ----------------------------------------------------

def cadastrar_livro(dados: dict) -> dict:
    """RF-01. E Livro; R Livro (ISBN único); W Livro; desfechos (recusas)."""
    if repositorio.buscar_livro_por_isbn(dados["isbn"]):
        raise ErroDeNegocio("ISBN já cadastrado")
    repositorio.salvar_livro(Livro(**dados))
    return {"mensagem": "Livro cadastrado"}


# ---- P02 Alterar livro ------------------------------------------------------

def alterar_livro(isbn: str, dados: dict) -> dict:
    """RF-02. E Livro; R Livro; W Livro; desfechos (recusas)."""
    atual = repositorio.buscar_livro_por_isbn(isbn)
    if atual is None:
        raise ErroDeNegocio("Livro não encontrado")
    novo = Livro(isbn=isbn, **{k: dados.get(k, getattr(atual, k)) for k in ("titulo", "autor", "ano", "quantidade")})
    repositorio.salvar_livro(novo)
    return {"mensagem": "Livro alterado"}


# ---- P03 Excluir livro ------------------------------------------------------

def excluir_livro(isbn: str) -> dict:
    """RF-03. E Livro; R Emprestimo (ativos do livro); W Livro; desfechos (recusas)."""
    if repositorio.emprestimos_ativos(livro=isbn):
        raise ErroDeNegocio("Livro com empréstimo ativo não pode ser excluído")
    repositorio.excluir_livro(isbn)
    return {"mensagem": "Livro excluído"}


# ---- P04 Consultar livros ---------------------------------------------------

def consultar_livros(titulo: Optional[str] = None, autor: Optional[str] = None) -> dict:
    """RF-04. E Livro (filtros); R Livro; X Livro; desfechos (recusas)."""
    livros = repositorio.listar_livros(titulo, autor)
    if not livros:
        return {"livros": [], "mensagem": "Nenhum livro encontrado"}
    return {"livros": [vars(l) for l in livros]}


# ---- P05 Cadastrar leitor ---------------------------------------------------

def cadastrar_leitor(dados: dict) -> dict:
    """RF-05. E Leitor; R Leitor (CPF único); W Leitor; desfechos (recusas)."""
    if repositorio.buscar_leitor_por_cpf(dados["cpf"]):
        raise ErroDeNegocio("CPF já cadastrado")
    repositorio.salvar_leitor(Leitor(**dados))
    return {"mensagem": "Leitor cadastrado"}


# ---- P06 Registrar empréstimo -----------------------------------------------

def registrar_emprestimo(cpf: str, isbn: str, data_emprestimo: date) -> dict:
    """RF-06. E Emprestimo; R Leitor; R Livro; R Emprestimo; W Emprestimo; X Emprestimo; desfechos (recusas)."""
    leitor = repositorio.buscar_leitor_por_cpf(cpf)
    if leitor is None or leitor.situacao != "ativo":
        raise ErroDeNegocio("Leitor inexistente ou inativo")
    livro = repositorio.buscar_livro_por_isbn(isbn)
    if livro is None:
        raise ErroDeNegocio("Livro não encontrado")
    if len(repositorio.emprestimos_ativos(livro=isbn)) >= livro.quantidade:
        raise ErroDeNegocio("Nenhum exemplar disponível")
    if len(repositorio.emprestimos_ativos(leitor=cpf)) >= LIMITE_EMPRESTIMOS:
        raise ErroDeNegocio("Leitor atingiu o limite de empréstimos")
    emprestimo = Emprestimo(id=None, leitor=cpf, livro=isbn, data_emprestimo=data_emprestimo,
                            data_prevista=data_emprestimo + timedelta(days=PRAZO_DIAS))
    repositorio.salvar_emprestimo(emprestimo)
    return {"id": emprestimo.id, "data_prevista": emprestimo.data_prevista.isoformat(), "mensagem": "Empréstimo registrado"}


# ---- P07 Registrar devolução ------------------------------------------------

def registrar_devolucao(id_emprestimo: int, data_devolucao: date, isencao_multa: bool = False,
                        justificativa_isencao: str = "") -> dict:
    """RF-07 (v2). E Emprestimo (com isenção); R Emprestimo; R ParametroMulta; W Emprestimo; X Emprestimo; desfechos (recusas)."""
    emprestimo = repositorio.buscar_emprestimo(id_emprestimo)
    if emprestimo is None or emprestimo.status != "ativo":
        raise ErroDeNegocio("Empréstimo não encontrado ou já devolvido")
    dias_atraso = max(0, (data_devolucao - emprestimo.data_prevista).days)
    if isencao_multa and not justificativa_isencao.strip():
        raise ErroDeNegocio("Isenção de multa exige justificativa")
    emprestimo.multa = 0.0 if isencao_multa else dias_atraso * repositorio.parametro_multa().valor_dia
    emprestimo.isencao_multa = isencao_multa
    emprestimo.justificativa_isencao = justificativa_isencao
    emprestimo.data_devolucao = data_devolucao
    emprestimo.status = "devolvido"
    repositorio.salvar_emprestimo(emprestimo)
    return {"multa": emprestimo.multa, "mensagem": "Devolução registrada"}


# ---- P08 Relatório de atrasos -----------------------------------------------

def relatorio_atrasos(hoje: date) -> dict:
    """RF-08 (v2). E DISPARO; R Emprestimo; R Leitor; R Livro; X Emprestimo; X Leitor; X Livro; desfechos (recusas)."""
    linhas: List[dict] = []
    for e in repositorio.emprestimos_em_atraso(hoje):
        dias = (hoje - date.fromisoformat(e["data_prevista"])).days
        linhas.append({"leitor": e["nome_leitor"], "livro": e["titulo_livro"], "data_prevista": e["data_prevista"],
                       "dias_atraso": dias})
    if not linhas:
        return {"linhas": [], "mensagem": "Não há empréstimos em atraso"}
    return {"linhas": linhas}


# ---- P10 Consultar leitor ---------------------------------------------------

def consultar_leitor(cpf: str) -> dict:
    """RF-10 (v2). E Leitor (cpf); R Leitor; X Leitor; desfechos (recusas)."""
    leitor = repositorio.buscar_leitor_por_cpf(cpf)
    if leitor is None:
        return {"mensagem": "Leitor não encontrado"}
    return {"leitor": vars(leitor)}


# ---- P09 Notificar atrasos --------------------------------------------------

def notificar_atrasos(hoje: date, enviar: Callable[[str, str, str], str]) -> Dict[str, int]:
    """RF-09. E DISPARO; R Emprestimo; R Leitor; R Livro; X Emprestimo; X Leitor; X Livro; E Notificacao; W Notificacao."""
    enviadas = 0
    for e in repositorio.emprestimos_em_atraso(hoje):
        dias = (hoje - date.fromisoformat(e["data_prevista"])).days
        corpo = (f"Olá {e['nome_leitor']}, o livro '{e['titulo_livro']}' deveria ter sido devolvido em "
                 f"{e['data_prevista']} e está {dias} dia(s) em atraso.")
        status = enviar(e["email_leitor"], "Empréstimo em atraso", corpo)
        repositorio.salvar_notificacao(Notificacao(id=None, emprestimo=e["id"], data_envio=hoje, status_envio=status))
        enviadas += 1
    return {"notificacoes": enviadas}
