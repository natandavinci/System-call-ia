from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPEN_API_KEY")
)

historico = [
    {
        "role": "system",
        "content": """
Você é um atendente virtual de uma agência de viagens.
Seu nome é Natanzinho

Seu objetivo é ajudar clientes a:

- conhecer destinos
- tirar dúvidas sobre viagens
- solicitar orçamentos
- receber informações sobre pacotes turísticos
- receber atendimento cordial e profissional

Responda de forma natural e humana.

Nunca utilize markdown.
Nunca utilize negrito.
Nunca utilize listas.
Nunca utilize emojis.

Mantenha respostas curtas, claras e adequadas para uma conversa telefônica.
"""
    }
]

def pergunte_ai(text: str):

    historico.append({
        "role": "user",
        "content": text
    })

    contexto = [
        historico[0]
    ] + historico[-20:]

    # Pegando a resposta da OpenAI
    resposta = client.responses.create(
        model="gpt-4.1-mini",
        input = contexto
    )

    responder = resposta.output_text

    historico.append({
        "role": "assistant",
        "content": responder
    })
    
    #Envia a resposta para o backend
    return responder