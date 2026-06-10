# RF-03: Detectar colisión
# Entrada : pieza (dict), estado del juego (dict con field/height/width)
# Salida  : bool — True si hay colisión, False si el movimiento es válido

from logic.rf02_generar_pieza import get_imagen_pieza

def detectar_colision(pieza: dict, juego: dict) -> bool:
    """
    Verifica si la pieza actual colisiona con bordes del tablero
    o con celdas ya ocupadas.
    Retorna True si hay colisión, False si la posición es válida.
    Retorna True si la pieza es None (situación anormal).
    """
    if pieza is None:
        return True

    field  = juego["field"]
    height = juego["height"]
    width  = juego["width"]

    for i in range(4):
        for j in range(4):
            if i * 4 + j in get_imagen_pieza(pieza):
                fila = i + pieza["y"]
                col  = j + pieza["x"]
                # fuera de límites
                if fila >= height or col >= width or col < 0:
                    return True
                # celda ocupada
                if fila >= 0 and field[fila][col] > 0:
                    return True

    return False
