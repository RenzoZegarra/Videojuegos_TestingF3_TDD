# RF-10: Detectar Game Over
# Entrada : pieza recién generada (dict), juego (dict)
# Salida  : juego (dict) — state cambia a "gameover" si la nueva pieza colisiona

from logic.rf03_detectar_colision import detectar_colision

def detectar_game_over(pieza: dict, juego: dict) -> dict:
    """
    Verifica si la nueva pieza generada colisiona al aparecer.
    Si colisiona, cambia el estado del juego a "gameover".
    Retorna el juego actualizado.
    """
    if detectar_colision(pieza, juego):
        juego["state"] = "gameover"

    return juego
