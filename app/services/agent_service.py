from app.agent.travel_agent import agent

def perguntar_agente(pergunta: str) -> str:
    resposta = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content":pergunta
                }
            ]
        }
    )

    #Tratamento
    texto = resposta["messages"][-1].content
    texto = texto.replace("*", "")
    texto = texto.replace("#", "")
    texto = texto.replace("\n", " ")

    return texto.strip()

