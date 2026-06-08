from app.agent.travel_agent import agent

def perguntar_agente(pergunta: str, session_id: str) :

    resposta = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content":pergunta
                }
            ]
        },
        config={
            "configurable": {
                "thread_id": session_id
            }
        }
    )

    #Tratamento
    texto = resposta["messages"][-1].content
    texto = texto.replace("*", "")
    texto = texto.replace("#", "")
    texto = texto.replace("\n", " ")

    return texto.strip()

