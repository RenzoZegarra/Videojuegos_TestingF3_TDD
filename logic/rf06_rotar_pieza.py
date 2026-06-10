# RF-06: Rotar pieza
# Entrada : pieza (dict), juego (dict)
# Salida  : pieza (dict) — rotation avanzado si no colisiona, igual si colisiona

from logic.rf02_generar_pieza import get_num_rotaciones
from logic.rf03_detectar_colision import detectar_colision

def rotar_pieza(pieza: dict, juego: dict) -> dict:
    """
    Avanza la rotación de la pieza al siguiente estado cíclico.
    Si la nueva orientación colisiona, revierte al estado previo.
    Retorna la pieza con rotation actualizado (o sin cambio si hubo colisión).
    """
    old_rotation = pieza["rotation"]
    pieza["rotation"] = (pieza["rotation"] + 1) % get_num_rotaciones(pieza)

    if detectar_colision(pieza, juego):
        pieza["rotation"] = old_rotation

    return pieza
