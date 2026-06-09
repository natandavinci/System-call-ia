from app.graph.travel_graph import travel_graph

resultado = travel_graph.invoke({

    "call_id": "1",

    "mensagem_usuario":
        "Minha reserva é 12000001",

    "resposta": "",

    "telefone": None,

    "codigo_reserva": None,

    "cliente_id": None,

    "cliente_nome": None,

    "reserva_id": None,

    "etapa": "inicio",

    "ultima_intencao": None,

    "telefone_confirmado": False,

    "reserva_confirmada": False

})

print(resultado)