# RF-09: Eliminar líneas completas
# Entrada : juego (dict con field, score, height, width)
# Salida  : juego (dict) — field sin filas completas, score actualizado

def eliminar_lineas(juego: dict) -> dict:
    """
    Detecta filas sin celdas vacías (ningún 0), las elimina y
    desplaza las filas superiores hacia abajo.
    El puntaje aumenta según n² donde n = líneas eliminadas en un turno.
    Retorna el juego actualizado.
    """
    field  = juego["field"]
    height = juego["height"]
    width  = juego["width"]
    lineas = 0

    for i in range(1, height):
        if all(field[i][j] != 0 for j in range(width)):
            lineas += 1
            for i1 in range(i, 1, -1):
                for j in range(width):
                    field[i1][j] = field[i1 - 1][j]
            field[0] = [0] * width  # fila superior queda vacía

    juego["field"] = field
    juego["score"] += lineas ** 2
    return juego
