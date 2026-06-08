from app.database.connection import SessionLocal
from app.database.models import Cliente
from langchain_core.tools import tool


@tool
def consultar_cliente(telefone: str) -> str:
    """
    Consulta informações de um cliente pelo telefone
    """
    print(telefone)
    print("Iniciando consulta")
    db = SessionLocal()

    cliente = (
        db.query(Cliente)
        .filter(Cliente.telefone == telefone)
        .first()
    )

    db.close()
    print("finalizando consulta")
    if not cliente:
        return "Cliente não encontrado"
    print(cliente.nome)
    return f""" 
    Nome: {cliente.nome}
    Email: {cliente.email}
    Telefone: {cliente.telefone}
"""
