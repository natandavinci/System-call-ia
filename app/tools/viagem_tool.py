from langchain.tools import tool

@tool
def buscar_viagem(destino: str):
    
    """
    Busca viagens disponiveis
    """

    return (
        f"Pacote encontrado para"
        f"{destino} por 899euros"
    )