from app.tools.cliente_tool import consultar_cliente
from app.tools.reserva_tool import consultar_reserva
print(
    consultar_cliente("Natanael"),
    consultar_reserva("2")
)