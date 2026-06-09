from app.graph.travel_graph import travel_graph

resultado = travel_graph.invoke(
    {
        "call_id": "1",
        "mensagem_usuario": "Minha reserva é 12000001"
    }
)

print(resultado["resposta"])