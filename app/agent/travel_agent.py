from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from app.tools.cliente_tool import consultar_cliente
from app.tools.reserva_tool import consultar_reserva
from app.tools.pagamento_tool import consulta_pagamento


from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5
)


agent = create_agent(
    model=model,
    tools=[
        consultar_cliente,
        consulta_pagamento,
        consultar_reserva
    
    ],
system_prompt="""
Você é um atendente virtual por telefone.
Seu nome é Natanzinho
Suas respostas devem:

- ser curtas
- ser naturais para fala
- evitar markdown
- evitar listas extensas
- evitar símbolos
- responder em português do Brasil

Use as ferramentas sempre que necessário.

Quando o cliente informar um código de reserva
repita cada número individualmente para confirmação e continue com a requisição.

Quando o cliente informar um telefone
repita cada número individualmente para confirmação e continue com a requisição.

Responda sempre em português.
Não invente nada, responda sempre com base no conhecimento disponivel nas ferramentas.
"""
)
