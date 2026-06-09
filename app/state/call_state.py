from typing import TypedDict, Optional

class CallState(TypedDict):

    call_id: str

    mensagem_usuario: str

    resposta: str

    telefone: Optional[str]

    codigo_reserva: Optional[str]

    cliente_id: Optional[int]

    cliente_nome: Optional[str]

    reserva_id: Optional[int]

    etapa: Optional[str]

    ultima_intencao: Optional[str]

    telefone_confirmado: bool

    reserva_confirmada: bool



