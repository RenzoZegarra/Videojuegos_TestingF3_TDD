# RF-05: Mover pieza lateralmente
# Entrada : pieza (dict), juego (dict), dx (int: -1 izquierda / +1 derecha)
# Salida  : pieza (dict) — x modificado si no hubo colisión, igual si hubo

from logic.rf03_detectar_colision import detectar_colision

def mover_lateral(pieza: dict, juego: dict, dx: int) -> dict:
    """
    Desplaza la pieza un paso a la izquierda (dx=-1) o derecha (dx=+1).
    Si la nueva posición colisiona, restaura x al valor original.
    Retorna la pieza con x actualizado (o sin cambio si hubo colisión).
    """
    old_x = pieza["x"]
    pieza["x"] += dx

    if detectar_colision(pieza, juego):
        pieza["x"] = old_x

    return pieza
