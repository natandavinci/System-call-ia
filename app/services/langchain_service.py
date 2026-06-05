from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_chroma.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings
import re
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)

load_dotenv()

llm = ChatOpenAI(
    model = "gpt-4.1-mini"
)

CAMINHO_DB = "db"
#prompt 
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
    Você é um especialista de viagens.

    responda em português.

    com base nessas informações:
    {base_conhecimento}

        """
    ),
    (
        "human",
        "{pergunta}"
    )
])


#Função perguntar
def perguntar_lang(texto):

    pergunta = texto
    #carregar Banco
    funcao_embedding = OpenAIEmbeddings()
    db = Chroma(persist_directory=CAMINHO_DB,embedding_function=funcao_embedding)

    resultados = db.similarity_search_with_relevance_scores(pergunta,k=3)
   
    if len(resultados) == 0 or resultados[0][1] < 0.7:
        return "Não encontrei informações sobre isso na base de conhecimento."
    
    texts_results = []

    for resultado in resultados:
        text = resultado[0].page_content
        texts_results.append(text)

    base_conhecimento = "\n\n---\n\n".join(texts_results)

    
    mensagens = prompt.format_messages(
        pergunta = pergunta,
        base_conhecimento=base_conhecimento
    )

   
    resposta = llm.invoke(
        mensagens
    )
   
    text = resposta.content
    
    limpo = sanitize_tts(text)

    return limpo

def sanitize_tts(text):
    text = re.sub(r'[*#_`]', '', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()