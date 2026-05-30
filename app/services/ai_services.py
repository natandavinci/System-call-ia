from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPEN_API_KEY")
)

def pergunte_ai(text: str):
    
    resposta = client.responses.create(
        model="gpt-4.1-mini",
        input = text
    )

    return resposta.output_text