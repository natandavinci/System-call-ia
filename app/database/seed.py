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
    codigo_reserva = "12000001",
    data_viagem="2026-11-29",
    status="Confirmada",
    valor=500.0,
    quantidade_passageiros = 2,
    origem = "Fortaleza",
    destino="São Paulo",

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


#Helio


helio = Cliente(
    nome="Helio Domingos",
    telefone="85999999996",
    email="helio@email.com"
)

db.add(helio)
db.commit()
db.refresh(helio)

reserva = Reserva(
    cliente_id=helio.id,
    codigo_reserva = "12000002",
    data_viagem="2026-11-30",
    status="Confirmada",
    valor=1000.0,
    quantidade_passageiros = 3,
    origem = "Lisboa",
    destino="Copenhagen",

)

db.add(reserva)
db.commit()
db.refresh(reserva)

pagamento = Pagamento(
    reserva_id=reserva.id,
    valor=1000.0,
    status="Pago",
    vencimento="2026-06-15"
)

db.add(pagamento)
db.commit()

#Vlad

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
    codigo_reserva = "12000003",
    data_viagem="2026-12-30",
    status="Confirmada",
    valor=2000.0,
    quantidade_passageiros = 5,
    origem = "Copenhagen",
    destino="Cairo",

)

db.add(reserva)
db.commit()
db.refresh(reserva)

pagamento = Pagamento(
    reserva_id=reserva.id,
    valor=2000.0,
    status="Pago",
    vencimento="2026-06-12"
)

db.add(pagamento)
db.commit()




db.close()

print(f"Dados inseridos! {vlad} cadastrado")