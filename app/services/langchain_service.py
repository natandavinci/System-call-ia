from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)

load_dotenv()

llm = ChatOpenAI(
    model = "gpt-4.1-mini"
)

def perguntar_lang(texto):

    from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini"
)

def perguntar_lang(texto):

    mensagens = [

        SystemMessage(
            content="""
Você é um pirata que odeia a frança.

Responda como um pirata.
.
"""
        ),

        HumanMessage(
            content=texto
        )

    ]

    resposta = llm.invoke(
        mensagens
    )

    return resposta.content
