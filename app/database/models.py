# Define as tabelas

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    email = Column(String)

    reservas = relationship("Reserva", back_populates="cliente")

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    
    codigo_reserva = Column(
    String,
    unique=True,
    nullable=False,
    index=True
)

    destino = Column(String)
    data_viagem = Column(String)

    status = Column(String)

    valor = Column(Float)

    quantidade_passageiros = Column(Integer)

    origem = Column(String)

    destino = Column(String)

    cliente = relationship("Cliente", back_populates="reservas")

    pagamentos = relationship("Pagamento", back_populates="reserva")

class Pagamento(Base):
    __tablename__ = "pagamentos"

    id = Column(Integer, primary_key=True, index=True)

    reserva_id = Column(Integer, ForeignKey("reservas.id"))


    valor = Column(Float)

    status = Column(String)

    vencimento = Column(String)

    reserva = relationship("Reserva", back_populates="pagamentos")

