from app.services.langchain_service import perguntar_lang

print(
    perguntar_lang(
        "Quais os pacotes de viagens para o Brasil? me Dê as informações "
    )
)

'''PARA USAR DEPOIS NO AGENTE:
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "travel_server": {
                "transport": "streamable_http",
                "url": "https://mcp.kiwi.com"
            }
    }
)

tools = await client.get_tools()




from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    "gpt-5-nano",
    tools=tools,
    checkpointer=InMemorySaver(),
    system_prompt="You are a travel agent. No follow up questions."
)



from langchain.messages import HumanMessage

config = {"configurable": {"thread_id": "1"}}

response = await agent.ainvoke(
    {"messages": [HumanMessage(content="Ok talk aboutthe first option, explain everything")]},
    config
    )


from pprint import pprint

pprint(response)



print(response["messages"][-1].content)




 '''