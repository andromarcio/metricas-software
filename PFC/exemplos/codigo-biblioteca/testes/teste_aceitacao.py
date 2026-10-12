#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testes de aceitação por processo (PFC: evidência de aceite, RP-03).

Uso: python3 -I testes/teste_aceitacao.py v1   (ou v2)
Cada função teste_Pnn exercita um processo do modelo; a saída lista o resultado por processo.
"""
import os
import sys
from datetime import date

VERSAO = sys.argv[1] if len(sys.argv) > 1 else "v2"
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", VERSAO))
from biblioteca import api, email_cliente, repositorio, servicos  # noqa: E402

LIVRO = {"isbn": "978-1", "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "quantidade": 1}
LEITOR = {"cpf": "111", "nome": "Ana", "email": "ana@exemplo.br", "telefone": "61 9999", "situacao": "ativo"}


def teste_P01_cadastrar_livro():
    assert api.tratar("POST /livros", LIVRO) == {"mensagem": "Livro cadastrado"}
    assert "erro" in api.tratar("POST /livros", LIVRO)  # ISBN único -> desfecho ISBN_DUPLICADO


def teste_P02_alterar_livro():
    assert api.tratar("PUT /livros/{isbn}", {"quantidade": 2}, {"isbn": "978-1"}) == {"mensagem": "Livro alterado"}


def teste_P03_excluir_livro():
    api.tratar("POST /livros", dict(LIVRO, isbn="978-2", titulo="Quincas Borba"))
    assert api.tratar("DELETE /livros/{isbn}", None, {"isbn": "978-2"}) == {"mensagem": "Livro excluído"}


def teste_P04_consultar_livros():
    assert len(api.tratar("GET /livros", None, {"titulo": "Casmurro"})["livros"]) == 1
    assert "mensagem" in api.tratar("GET /livros", None, {"titulo": "inexistente"})


def teste_P05_cadastrar_leitor():
    assert api.tratar("POST /leitores", LEITOR) == {"mensagem": "Leitor cadastrado"}
    assert "erro" in api.tratar("POST /leitores", LEITOR)


def teste_P06_registrar_emprestimo():
    r = api.tratar("POST /emprestimos", {"cpf": "111", "isbn": "978-1", "data": "2026-01-01"})
    assert r["data_prevista"] == "2026-01-15" and r["id"] == 1


def teste_P07_registrar_devolucao():
    corpo = {"data_devolucao": "2026-01-20"}
    if VERSAO != "v1":
        corpo.update({"isencao_multa": True, "justificativa_isencao": "greve dos ônibus"})
    r = api.tratar("POST /emprestimos/{id}/devolucao", corpo, {"id": 1})
    assert r["multa"] == (0.0 if VERSAO != "v1" else 5 * 1.5), r


def teste_P08_relatorio_atrasos():
    api.tratar("POST /emprestimos", {"cpf": "111", "isbn": "978-1", "data": "2026-01-21"})
    r = servicos.relatorio_atrasos(date(2026, 2, 10))
    assert r["linhas"][0]["dias_atraso"] == 6 and r["linhas"][0]["leitor"] == "Ana"
    assert ("multa_estimada" in r["linhas"][0]) == (VERSAO == "v1")


def teste_P09_notificar_atrasos():
    assert servicos.notificar_atrasos(date(2026, 2, 10), email_cliente.enviar) == {"notificacoes": 1}


def teste_P10_consultar_leitor():
    if VERSAO == "v1":
        return "n/a"
    assert api.tratar("GET /leitores/{cpf}", None, {"cpf": "111"})["leitor"]["nome"] == "Ana"
    assert "mensagem" in api.tratar("GET /leitores/{cpf}", None, {"cpf": "999"})


if __name__ == "__main__":
    repositorio.conectar()
    falhas = 0
    for nome, fn in sorted((k, v) for k, v in globals().items() if k.startswith("teste_P")):
        try:
            res = fn()
            print(f"{nome[6:9]} {'n/a' if res == 'n/a' else 'ok':3s}  {nome}")
        except AssertionError as e:
            falhas += 1
            print(f"{nome[6:9]} FALHA {nome}: {e}")
    print(f"\n{VERSAO}: {'todos os processos aceitos' if not falhas else str(falhas) + ' falha(s)'}")
    sys.exit(1 if falhas else 0)
