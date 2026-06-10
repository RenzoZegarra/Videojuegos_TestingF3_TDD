# RF-01: Inicializar tablero
# Entrada : height (int), width (int)
# Salida  : dict con keys: field (list[list[int]]), score (int), state (str)

def inicializar_tablero(height: int, width: int) -> dict:
    """
    Crea el estado inicial del juego.
    Retorna None si las dimensiones son inválidas (<= 0).
    """
    if height <= 0 or width <= 0:
        return None

    field = [[0] * width for _ in range(height)]

    return {
        "field": field,
        "score": 0,
        "state": "start",
        "height": height,
        "width": width,
    }
