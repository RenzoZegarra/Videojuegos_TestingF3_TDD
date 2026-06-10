# RF-02: Generar pieza aleatoria
# Entrada : x=3 (int), y=0 (int)
# Salida  : dict con keys: type, color, rotation, x, y

import random

FIGURES = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],           # palo  (tipo 0)
    [[4, 5, 9, 10], [2, 6, 5, 9]],            # S     (tipo 1)
    [[6, 7, 9, 10], [1, 5, 6, 10]],           # Z     (tipo 2)
    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],   # J (tipo 3)
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]], # L (tipo 4)
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],    # T (tipo 5)
    [[1, 2, 5, 6]],                            # cuadrado (tipo 6)
]

NUM_COLORS = 6  # colores válidos: 1..6

def generar_pieza(x: int = 3, y: int = 0) -> dict:
    """
    Genera una nueva pieza con tipo y color aleatorios.
    Retorna None si no hay figuras definidas.
    """
    if not FIGURES:
        return None

    tipo = random.randint(0, len(FIGURES) - 1)
    color = random.randint(1, NUM_COLORS)

    return {
        "type": tipo,
        "color": color,
        "rotation": 0,
        "x": x,
        "y": y,
    }

def get_imagen_pieza(pieza: dict) -> list:
    """Devuelve la lista de celdas activas para la rotación actual de la pieza."""
    return FIGURES[pieza["type"]][pieza["rotation"]]

def get_num_rotaciones(pieza: dict) -> int:
    """Devuelve cuántas rotaciones tiene el tipo de pieza."""
    return len(FIGURES[pieza["type"]])
