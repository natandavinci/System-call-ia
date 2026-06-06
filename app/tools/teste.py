from app.tools.cliente_tool import consultar_cliente
from app.tools.reserva_tool import consultar_reserva
from app.tools.pagamento_tool import consulta_pagamento

cliente = consultar_cliente.invoke(
    {"telefone": "85999999998"}
)

reserva = consultar_reserva.invoke(
    {"codigo_reserva": "12000001"}
)

pagamento = consulta_pagamento.invoke(
    {"codigo_reserva": "12000001"}
)


print(cliente)
print(reserva)
print(pagamento)