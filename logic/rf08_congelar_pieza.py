# RF-08: Congelar pieza en el tablero
# Entrada : pieza (dict), juego (dict)
# Salida  : juego (dict) — field actualizado con el color de la pieza

from logic.rf02_generar_pieza import get_imagen_pieza
from logic.rf09_eliminar_lineas import eliminar_lineas

def congelar_pieza(pieza: dict, juego: dict) -> dict:
    """
    Escribe los bloques de la pieza en el field con su color.
    Luego llama a eliminar_lineas para limpiar filas completas.
    Retorna el juego actualizado.
    """
    field = juego["field"]

    for i in range(4):
        for j in range(4):
            if i * 4 + j in get_imagen_pieza(pieza):
                fila = i + pieza["y"]
                col  = j + pieza["x"]
                if 0 <= fila < juego["height"] and 0 <= col < juego["width"]:
                    field[fila][col] = pieza["color"]

    juego["field"] = field
    juego = eliminar_lineas(juego)
    return juego
