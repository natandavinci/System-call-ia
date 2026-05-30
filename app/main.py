from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

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

#Testar comunicação
class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):

    return {
        "response": f"Você disse: {message.text}"
    }
