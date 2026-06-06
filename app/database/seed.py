from app.database.connection import SessionLocal
from app.database.models import Cliente, Reserva, Pagamento

db = SessionLocal()

natan = Cliente(
    nome="Natanael Queiroz",
    telefone="85999999997",
    email="natanael@email.com"
)

db.add(natan)
db.commit()
db.refresh(natan)

reserva = Reserva(
    cliente_id=natan.id,
    destino="São Paulo",
    data_viagem="2026-11-29",
    status="Confirmada",
    valor=500.0
)

db.add(reserva)
db.commit()
db.refresh(reserva)

pagamento = Pagamento(
    reserva_id=reserva.id,
    valor=500.0,
    status="Pago",
    vencimento="2026-06-10"
)

db.add(pagamento)
db.commit()


#vlad


vlad = Cliente(
    nome="Vladyslaw Horbatenko",
    telefone="85999999996",
    email="vlad@email.com"
)

db.add(vlad)
db.commit()
db.refresh(vlad)

reserva = Reserva(
    cliente_id=vlad.id,
    destino="Barcelona",
    data_viagem="2026-07-12",
    status="Confirmada",
    valor=1000.0
)

db.add(reserva)
db.commit()
db.refresh(reserva)

pagamento = Pagamento(
    reserva_id=reserva.id,
    valor=1000.0,
    status="Pago",
    vencimento="2026-06-05"
)

db.add(pagamento)
db.commit()



db.close()

print(f"Dados inseridos! {vlad} cadastrado")