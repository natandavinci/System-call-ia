from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPEN_API_KEY")
)

historico = []

def pergunte_ai(text: str):

    historico.append({
        "role": "user",
        "content": text
    })

    resposta = client.responses.create(
        model="gpt-4.1-mini",
        input = historico
    )

    responder = resposta.output_text

    historico.append({
        "role": "assistant",
        "content": responder
    })

    return responder