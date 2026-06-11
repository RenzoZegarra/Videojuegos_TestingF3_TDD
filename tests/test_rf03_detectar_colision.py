import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.rf01_inicializar_tablero import inicializar_tablero
from logic.rf02_generar_pieza import generar_pieza
from logic.rf03_detectar_colision import detectar_colision

def _juego():
    return inicializar_tablero(20, 10)

def _pieza(tipo=6, x=3, y=0):
    p = generar_pieza(x=x, y=y)
    p["type"] = tipo
    p["rotation"] = 0
    return p

def test_sin_obstaculo_no_hay_colision():
    assert detectar_colision(_pieza(x=3, y=0), _juego()) == False

def test_colision_con_borde_inferior():
    pieza = _pieza(x=3, y=19)
    assert detectar_colision(pieza, _juego()) == True

def test_colision_con_borde_izquierdo():
    # cuadrado tipo 6: celdas activas en j=1,j=2
    # con x=-2: col = 1+(-2) = -1 → fuera del borde izquierdo
    pieza = _pieza(x=-2, y=5)
    assert detectar_colision(pieza, _juego()) == True

def test_colision_con_borde_derecho():
    pieza = _pieza(x=9, y=5)
    assert detectar_colision(pieza, _juego()) == True

def test_colision_con_celda_ocupada():
    juego = _juego()
    juego["field"][5][4] = 2
    pieza = _pieza(x=3, y=4)
    assert detectar_colision(pieza, juego) == True

def test_pieza_none_retorna_true():
    assert detectar_colision(None, _juego()) == True