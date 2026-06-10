# RF-04: Mover pieza hacia abajo
# Entrada : pieza (dict), juego (dict)
# Salida  : dict con keys: pieza (dict actualizada), juego (dict actualizado), congelada (bool)

from logic.rf03_detectar_colision import detectar_colision
from logic.rf08_congelar_pieza import congelar_pieza

def mover_abajo(pieza: dict, juego: dict) -> dict:
    """
    Intenta bajar la pieza una celda.
    - Si no colisiona: actualiza pieza["y"] += 1.
    - Si colisiona   : congela la pieza en su posición actual.
    Retorna: { "pieza": ..., "juego": ..., "congelada": bool }
    """
    pieza["y"] += 1

    if detectar_colision(pieza, juego):
        pieza["y"] -= 1
        juego = congelar_pieza(pieza, juego)
        return {"pieza": None, "juego": juego, "congelada": True}

    return {"pieza": pieza, "juego": juego, "congelada": False}
