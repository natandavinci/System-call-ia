from app.agent.travel_agent import agent

async def perguntar_agente(pergunta: str, session_id: str) :

#Envia para o travel-agent(openai)
    resposta = await agent.ainvoke(
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

    #Retorna a resposta para o backend(main) 
    return texto.strip()

