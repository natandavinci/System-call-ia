from app.state.memory import (
    get_state,
    create_call,
    update_state
)

create_call("call_001")

update_state(
    "call_001",
    telefone="88999998888"
)

print(
    get_state("call_001")
)