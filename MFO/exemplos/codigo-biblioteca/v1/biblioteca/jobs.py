"""Processos disparados pelo relógio (MFO: usuário funcional 'relogio')."""
from datetime import date

from . import email_cliente, servicos


def job_diario() -> dict:
    """Executado uma vez por dia pelo agendador: P09 Notificar atrasos."""
    return servicos.notificar_atrasos(date.today(), email_cliente.enviar)
