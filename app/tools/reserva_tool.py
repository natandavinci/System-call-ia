from app.database.connection import SessionLocal
from app.database.models import Reserva

def consultar_reserva(cliente_id: int):
    db = SessionLocal()

    reserva = (
        db.query(Reserva)
        .filter(Reserva.cliente_id == cliente_id)
        .first()
    )
    db.close()

    if not reserva:
        return "Nenhuma reserva encontrada."

    return f"""
    Destino: {reserva.destino}
    Status: {reserva.status}
    Valor: {reserva.valor}
"""