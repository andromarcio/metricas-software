"""Entidades do domínio (MFO: RI-03). Cada classe corresponde a uma tabela em repositorio.py."""
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Livro:
    isbn: str
    titulo: str
    autor: str
    ano: int
    quantidade: int


@dataclass
class Leitor:
    cpf: str
    nome: str
    email: str
    telefone: str
    situacao: str  # "ativo" | "inativo"


@dataclass
class Emprestimo:
    id: Optional[int]
    leitor: str            # cpf do leitor
    livro: str             # isbn do livro
    data_emprestimo: date
    data_prevista: date
    data_devolucao: Optional[date] = None
    multa: float = 0.0
    status: str = "ativo"  # "ativo" | "devolvido"


@dataclass
class ParametroMulta:
    valor_dia: float


@dataclass
class Notificacao:
    id: Optional[int]
    emprestimo: int
    data_envio: date
    status_envio: str
