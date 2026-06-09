from app.state.call_state import CallState

calls: dict[str, CallState] = {}

def create_call(call_id: str):

    calls[call_id] = {
        "call_id": call_id,
        "telefone": None,
        "codigo_reserva": None,
        "cliente_id": None,
        "cliente_nome": None,
        "reserva_id": None,
        "reserva_confirmada": False,
        "telefone_confirmado": False,
        "ultima_intencao": None,
        "etapa": "inicio"
    }


def get_state(call_id: str):
    return calls.get(call_id)


def update_state(call_id: str, **kwargs):

    if call_id not in calls:
        create_call(call_id)

    calls[call_id].update(kwargs)

def delete_call(call_id: str):

    calls.pop(call_id, None)