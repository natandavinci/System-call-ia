from app.database.connection import SessionLocal
from app.database.models import Pagamento
from app.database.models import Reserva
from langchain_core.tools import tool

@tool
def consulta_pagamento (codigo_reserva : int ) -> int:
    """
    Consulta os pagamentos associados a uma reserva
    """

    db = SessionLocal()

    try:

        pagamento = (
        db.query(Pagamento)
        .join(Reserva)
        .filter(Reserva.codigo_reserva == codigo_reserva)
        ).first()


        if pagamento is None:
            return "Nenhum pagamento encontrado"
        
        return f"""
        Codigo da Reserva: {pagamento.reserva.codigo_reserva}
        Valor: {pagamento.valor}
        Status: {pagamento.status}
        Vencimento: {pagamento.vencimento}
    """
    finally:
        db.close()



