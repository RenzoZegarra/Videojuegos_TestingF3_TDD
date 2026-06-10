# RF-07: Caída instantánea (hard drop)
# Entrada : pieza (dict), juego (dict)
# Salida  : dict con keys: pieza (dict), juego (dict actualizado), congelada (True siempre)

from logic.rf03_detectar_colision import detectar_colision
from logic.rf08_congelar_pieza import congelar_pieza

def caida_instantanea(pieza: dict, juego: dict) -> dict:
    """
    Baja la pieza hasta la posición más baja posible sin colisionar
    y la congela inmediatamente.
    Retorna: { "pieza": None, "juego": ..., "congelada": True }
    Si no existe pieza activa, retorna el juego sin cambios.
    """
    if pieza is None:
        return {"pieza": None, "juego": juego, "congelada": False}

    while not detectar_colision(pieza, juego):
        pieza["y"] += 1
    pieza["y"] -= 1  # retrocede a la última posición válida

    juego = congelar_pieza(pieza, juego)
    return {"pieza": None, "juego": juego, "congelada": True}
