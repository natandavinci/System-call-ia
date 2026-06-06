from app.database.connection import SessionLocal
from app.database.models import Cliente

db = SessionLocal()

cliente = (
    db.query(Cliente)
    .filter(Cliente.id == 2)
    .first()
)

if cliente:
    cliente.telefone = "85999999998"
    db.commit()
    print("Telefone atualizado")

db.close()