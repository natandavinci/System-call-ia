from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.services.ai_services import pergunte_ai

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
def chat(message: Message):

    #Envia para a openAI
    resposta = pergunte_ai(message.text)

    #Envia a resposta para o Frontend
    return {
        "response": resposta
    }
