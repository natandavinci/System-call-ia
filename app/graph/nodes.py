from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import re
from app.state.call_state import CallState

load_dotenv()

def extract_information_node(state: CallState):

    texto = state["mensagem_usuario"]

    telefone = re.search(r"\d{10,11}", texto)

    codigo = re.search(r"12\d{4,8}", texto)

    if telefone:
        state["telefone"] = telefone.group()

    if codigo:
        state["codigo_reserva"] = codigo.group()

    return state

def router_node(state: CallState):

    texto = state["mensagem_usuario"].lower()

    if "telefone" in texto:
        state["ultima_intencao"] = "consultar_cliente"

    elif "reserva" in texto:
        state["ultima_intencao"] = "consultar_reserva"

    elif "pagamento" in texto:
        state["ultima_intencao"] = "consultar_pagamento"

    else:
        state["ultima_intencao"] = "conversa"

    return state


def response_node(state: CallState):

    state["resposta"] = state.get(
        "resultado_tool",
        "Nenhuma informação encontrada."
    )

    return state

from app.tools.reserva_tool import consultar_reserva
from app.tools.pagamento_tool import consulta_pagamento
from app.tools.cliente_tool import consultar_cliente

def execute_tool_node(state: CallState):

    if state["ultima_intencao"] == "consultar_reserva":

        resultado = consultar_reserva.invoke(
            {
                "codigo_reserva": state["codigo_reserva"]
            }
        )

        state["resultado_tool"] = resultado

    return state