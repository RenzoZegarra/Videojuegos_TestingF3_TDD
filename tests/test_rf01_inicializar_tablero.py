import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.rf01_inicializar_tablero import inicializar_tablero

def test_tablero_tiene_20_filas():
    juego = inicializar_tablero(20, 10)
    assert len(juego["field"]) == 20

def test_cada_fila_tiene_10_columnas():
    juego = inicializar_tablero(20, 10)
    for fila in juego["field"]:
        assert len(fila) == 10

def test_todas_las_celdas_inician_en_cero():
    juego = inicializar_tablero(20, 10)
    for fila in juego["field"]:
        for celda in fila:
            assert celda == 0

def test_score_inicial_es_cero():
    juego = inicializar_tablero(20, 10)
    assert juego["score"] == 0

def test_estado_inicial_es_start():
    juego = inicializar_tablero(20, 10)
    assert juego["state"] == "start"

def test_dimensiones_invalidas_retornan_none():
    assert inicializar_tablero(0, 10) is None
    assert inicializar_tablero(20, 0) is None
    assert inicializar_tablero(-1, -1) is None