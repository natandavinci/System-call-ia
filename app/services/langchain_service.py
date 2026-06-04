from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)

load_dotenv()

llm = ChatOpenAI(
    model = "gpt-4.1-mini"
)

#prompt 
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
    Você é um especialista de viagens.

    responda em português.
        """
    ),
    (
        "human",
        "{pergunta}"
    )
])


#Função perguntar
def perguntar_lang(texto):

    mensagens = prompt.format_messages(
        pergunta = texto
    )

    resposta = llm.invoke(
        mensagens
    )

    return resposta.content
