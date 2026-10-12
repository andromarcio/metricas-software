"""Acesso ao armazenamento persistente (PFC: movimentos R e W). SQLite em memória por padrão."""
import sqlite3
from datetime import date
from typing import List, Optional

from .modelos import Emprestimo, Leitor, Livro, Notificacao, ParametroMulta

_conexao: Optional[sqlite3.Connection] = None


def conectar(caminho: str = ":memory:") -> sqlite3.Connection:
    global _conexao
    _conexao = sqlite3.connect(caminho)
    _conexao.row_factory = sqlite3.Row
    criar_esquema(_conexao)
    return _conexao


def criar_esquema(cx: sqlite3.Connection) -> None:
    cx.executescript(
        """
        CREATE TABLE IF NOT EXISTS livro (isbn TEXT PRIMARY KEY, titulo TEXT, autor TEXT, ano INTEGER, quantidade INTEGER);
        CREATE TABLE IF NOT EXISTS leitor (cpf TEXT PRIMARY KEY, nome TEXT, email TEXT, telefone TEXT, situacao TEXT);
        CREATE TABLE IF NOT EXISTS emprestimo (id INTEGER PRIMARY KEY AUTOINCREMENT, leitor TEXT, livro TEXT,
            data_emprestimo TEXT, data_prevista TEXT, data_devolucao TEXT, multa REAL, status TEXT);
        CREATE TABLE IF NOT EXISTS parametro_multa (valor_dia REAL);
        CREATE TABLE IF NOT EXISTS notificacao (id INTEGER PRIMARY KEY AUTOINCREMENT, emprestimo INTEGER, data_envio TEXT, status_envio TEXT);
        INSERT INTO parametro_multa (valor_dia) SELECT 1.5 WHERE NOT EXISTS (SELECT 1 FROM parametro_multa);
        """
    )


def _cx() -> sqlite3.Connection:
    return _conexao if _conexao is not None else conectar()


# ---- Livro -----------------------------------------------------------------

def buscar_livro_por_isbn(isbn: str) -> Optional[Livro]:
    r = _cx().execute("SELECT * FROM livro WHERE isbn = ?", (isbn,)).fetchone()
    return Livro(**dict(r)) if r else None


def salvar_livro(livro: Livro) -> None:
    _cx().execute(
        "INSERT OR REPLACE INTO livro (isbn, titulo, autor, ano, quantidade) VALUES (?, ?, ?, ?, ?)",
        (livro.isbn, livro.titulo, livro.autor, livro.ano, livro.quantidade),
    )


def excluir_livro(isbn: str) -> None:
    _cx().execute("DELETE FROM livro WHERE isbn = ?", (isbn,))


def listar_livros(titulo: Optional[str] = None, autor: Optional[str] = None) -> List[Livro]:
    sql, params = "SELECT * FROM livro WHERE 1=1", []
    if titulo:
        sql += " AND titulo LIKE ?"
        params.append(f"%{titulo}%")
    if autor:
        sql += " AND autor LIKE ?"
        params.append(f"%{autor}%")
    return [Livro(**dict(r)) for r in _cx().execute(sql, params).fetchall()]


# ---- Leitor ----------------------------------------------------------------

def buscar_leitor_por_cpf(cpf: str) -> Optional[Leitor]:
    r = _cx().execute("SELECT * FROM leitor WHERE cpf = ?", (cpf,)).fetchone()
    return Leitor(**dict(r)) if r else None


def salvar_leitor(leitor: Leitor) -> None:
    _cx().execute(
        "INSERT OR REPLACE INTO leitor (cpf, nome, email, telefone, situacao) VALUES (?, ?, ?, ?, ?)",
        (leitor.cpf, leitor.nome, leitor.email, leitor.telefone, leitor.situacao),
    )


# ---- Empréstimo ------------------------------------------------------------

def _para_emprestimo(r) -> Emprestimo:
    d = dict(r)
    d["data_emprestimo"] = date.fromisoformat(d["data_emprestimo"])
    d["data_prevista"] = date.fromisoformat(d["data_prevista"])
    d["data_devolucao"] = date.fromisoformat(d["data_devolucao"]) if d["data_devolucao"] else None
    return Emprestimo(**d)


def emprestimos_ativos(livro: Optional[str] = None, leitor: Optional[str] = None) -> List[Emprestimo]:
    sql, params = "SELECT * FROM emprestimo WHERE status = 'ativo'", []
    if livro:
        sql += " AND livro = ?"
        params.append(livro)
    if leitor:
        sql += " AND leitor = ?"
        params.append(leitor)
    return [_para_emprestimo(r) for r in _cx().execute(sql, params).fetchall()]


def buscar_emprestimo(id_emprestimo: int) -> Optional[Emprestimo]:
    r = _cx().execute("SELECT * FROM emprestimo WHERE id = ?", (id_emprestimo,)).fetchone()
    return _para_emprestimo(r) if r else None


def salvar_emprestimo(e: Emprestimo) -> int:
    cx = _cx()
    if e.id is None:
        cur = cx.execute(
            "INSERT INTO emprestimo (leitor, livro, data_emprestimo, data_prevista, data_devolucao, multa, status)"
            " VALUES (?, ?, ?, ?, ?, ?, ?)",
            (e.leitor, e.livro, e.data_emprestimo.isoformat(), e.data_prevista.isoformat(),
             e.data_devolucao.isoformat() if e.data_devolucao else None, e.multa, e.status),
        )
        e.id = cur.lastrowid
    else:
        cx.execute(
            "UPDATE emprestimo SET data_devolucao = ?, multa = ?, status = ? WHERE id = ?",
            (e.data_devolucao.isoformat() if e.data_devolucao else None, e.multa, e.status, e.id),
        )
    return e.id


def emprestimos_em_atraso(hoje: date) -> List[dict]:
    """Empréstimos ativos vencidos, com nome do leitor e título do livro (R Emprestimo, R Leitor, R Livro)."""
    sql = (
        "SELECT e.id, e.leitor, e.livro, e.data_prevista, l.nome AS nome_leitor, l.email AS email_leitor,"
        " v.titulo AS titulo_livro FROM emprestimo e JOIN leitor l ON l.cpf = e.leitor JOIN livro v ON v.isbn = e.livro"
        " WHERE e.status = 'ativo' AND e.data_prevista < ?"
    )
    return [dict(r) for r in _cx().execute(sql, (hoje.isoformat(),)).fetchall()]


# ---- Parâmetro de multa e Notificação ---------------------------------------

def parametro_multa() -> ParametroMulta:
    r = _cx().execute("SELECT valor_dia FROM parametro_multa").fetchone()
    return ParametroMulta(valor_dia=r["valor_dia"])


def salvar_notificacao(n: Notificacao) -> int:
    cur = _cx().execute(
        "INSERT INTO notificacao (emprestimo, data_envio, status_envio) VALUES (?, ?, ?)",
        (n.emprestimo, n.data_envio.isoformat(), n.status_envio),
    )
    n.id = cur.lastrowid
    return n.id
