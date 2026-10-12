"""Chamada ao serviço externo de e-mail (PFC: usuário funcional 'sistema'; X ao enviar, E no status devolvido)."""


def enviar(destinatario: str, assunto: str, corpo: str) -> str:
    """Envia a mensagem ao serviço de e-mail e devolve o status informado por ele ("enviado" ou "falha")."""
    # Simulação: um serviço real faria uma chamada HTTP e devolveria o status.
    return "enviado" if "@" in destinatario else "falha"
