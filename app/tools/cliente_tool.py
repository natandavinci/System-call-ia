from app.database.connection import SessionLocal
from app.database.models import Cliente

def consultar_cliente(nome: str):
    db = SessionLocal()

    cliente = (
        db.query(Cliente)
        .filter(Cliente.nome.ilike(f"%{nome}%"))
        .first()
    )

    db.close()

    if not cliente:
        return "Cliente não encontrado"

    return f""" 
    Nome: {cliente.nome}
    Email: {cliente.email}
    Telefone: {cliente.telefone}
"""
