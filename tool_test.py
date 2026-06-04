from app.tools.viagem_tool import (
    buscar_viagem
)
resultado = buscar_viagem.invoke(
    "Paris"
)

print(resultado)