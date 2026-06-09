from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.services.ai_services import pergunte_ai
from app.services.langchain_service import perguntar_lang
from app.services.agent_service import perguntar_agente
app = FastAPI()

app.mount(

    "/static",

    StaticFiles(directory="app/static"),
    
    name="static"

)

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def home(request: Request):
   
    return templates.TemplateResponse(
        
        request=request,
        
        name="index.html"

    )

#Dado que se espera
class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(message: Message):

    #Envia para o Agente-service
    resposta = await perguntar_agente(
        message.text,
        "usuario_1")

    #Recebe e envia a resposta para o Frontend
    return {
        "response": resposta
    }
