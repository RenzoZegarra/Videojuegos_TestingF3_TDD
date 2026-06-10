import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.rf01_inicializar_tablero import inicializar_tablero
from logic.rf02_generar_pieza import generar_pieza
from logic.rf05_mover_lateral import mover_lateral

def _juego():
    return inicializar_tablero(20, 10)

def _pieza(x=5, y=5):
    p = generar_pieza(x=x, y=y)
    p["type"] = 6
    p["rotation"] = 0
    return p

def test_mover_izquierda_con_espacio_libre():
    pieza = _pieza(x=5)
    pieza = mover_lateral(pieza, _juego(), dx=-1)
    assert pieza["x"] == 4

def test_mover_derecha_con_espacio_libre():
    pieza = _pieza(x=5)
    pieza = mover_lateral(pieza, _juego(), dx=1)
    assert pieza["x"] == 6

def test_no_sale_por_borde_izquierdo():
    # cuadrado en x=-1: celdas en col 0 y 1, aun valido
    # al mover dx=-1 -> x=-2: col -2+1=-1 -> COLISION, debe quedarse en -1
    pieza = _pieza(x=-1)
    pieza = mover_lateral(pieza, _juego(), dx=-1)
    assert pieza["x"] == -1

def test_no_sale_por_borde_derecho():
    # cuadrado en x=7: col 7+2=9 OK
    # al mover dx=1 -> x=8: col 8+2=10 >= width=10 -> COLISION, debe quedarse en 7
    pieza = _pieza(x=7)
    pieza = mover_lateral(pieza, _juego(), dx=1)
    assert pieza["x"] == 7

def test_no_se_mueve_si_celda_lateral_ocupada():
    juego = _juego()
    juego["field"][5][8] = 3
    pieza = _pieza(x=5, y=5)
    pieza = mover_lateral(pieza, juego, dx=1)
    assert pieza["x"] == 5