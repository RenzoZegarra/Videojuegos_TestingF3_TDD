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


#-------------

def test_valores_iniciales_del_juego(height, width):
    juego = inicializar_tablero(height, width)
    esperado = {
        "field": [
            [0, 0, 0],
            [0, 0, 0]
        ],
        "score": 0,
        "state": "start",
        "height": 2,
        "width": 3
    }

    assert juego == esperado

def test_dimensiones_invalidas_retornan_none():
    assert inicializar_tablero(0, 10) is None
    assert inicializar_tablero(20, 0) is None
    assert inicializar_tablero(-1, -1) is None

def test_tablero_tiene_20_filas():
    juego = inicializar_tablero(20, 10)
    assert len(juego["field"]) == 20

def test_cada_fila_tiene_10_columnas():
    juego = inicializar_tablero(20, 10)
    for fila in juego["field"]:
        assert len(fila) == 10

print(test_valores_iniciales_del_juego(20, 10))
print(test_dimensiones_invalidas_retornan_none())
print(test_tablero_tiene_20_filas())
print(test_cada_fila_tiene_10_columnas)