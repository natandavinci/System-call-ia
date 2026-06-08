from app.tools.cliente_tool import consultar_cliente
from app.tools.reserva_tool import consultar_reserva
from app.tools.pagamento_tool import consulta_pagamento
from app.agent.travel_agent import agent

resposta = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Consulte o cliente Natanael  ,email: natanael@email.com"
            }
        ]
    }
)

print(resposta["messages"][-1].content)