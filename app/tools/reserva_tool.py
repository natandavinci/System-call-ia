from app.database.connection import SessionLocal
from app.database.models import Reserva
from langchain_core.tools import tool


@tool 
def consultar_reserva(codigo_reserva: int) -> str:
    """
    Consulta reserva pelo código da reserva.
    """
    db = SessionLocal()

    reserva = (
        db.query(Reserva)
        .filter(Reserva.codigo_reserva == codigo_reserva)
        .first()
    )
    db.close()

    if not reserva:
        return "Nenhuma reserva encontrada."

    return f"""
    Codigo da reserva: {reserva.codigo_reserva}
    Data da Viagem: {reserva.data_viagem}
    Origem: {reserva.origem}
    Destino: {reserva.destino}
    Status: {reserva.status}
    Valor: {reserva.valor}
"""