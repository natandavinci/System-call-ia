from app.tools.cliente_tool import consultar_cliente
from app.tools.reserva_tool import consultar_reserva
from app.tools.pagamento_tool import consulta_pagamento

TOOLS = [
    consultar_cliente,
    consultar_reserva,
    consulta_pagamento
]