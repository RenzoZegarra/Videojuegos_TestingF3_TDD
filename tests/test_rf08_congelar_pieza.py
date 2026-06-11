import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.rf01_inicializar_tablero import inicializar_tablero
from logic.rf02_generar_pieza import generar_pieza
from logic.rf08_congelar_pieza import congelar_pieza

def _juego():
    return inicializar_tablero(20, 10)

def _pieza_cuadrado(x=3, y=5, color=2):
    p = generar_pieza(x=x, y=y)
    p["type"] = 6
    p["rotation"] = 0
    p["color"] = color
    return p

def test_bloques_se_escriben_en_field():
    juego = _juego()
    pieza = _pieza_cuadrado(x=3, y=5, color=2)
    juego = congelar_pieza(pieza, juego)
    # cuadrado tipo 6: celdas [1,2,5,6]
    # i=0,j=1 -> fila=5, col=4 / i=0,j=2 -> fila=5, col=5
    # i=1,j=1 -> fila=6, col=4 / i=1,j=2 -> fila=6, col=5
    assert juego["field"][5][4] == 2
    assert juego["field"][5][5] == 2
    assert juego["field"][6][4] == 2
    assert juego["field"][6][5] == 2

def test_color_de_bloque_se_conserva():
    juego = _juego()
    pieza = _pieza_cuadrado(x=3, y=5, color=4)
    juego = congelar_pieza(pieza, juego)
    assert juego["field"][5][4] == 4

def test_celdas_vacias_no_se_modifican():
    juego = _juego()
    pieza = _pieza_cuadrado(x=3, y=5)
    juego = congelar_pieza(pieza, juego)
    assert juego["field"][0][0] == 0
    assert juego["field"][19][9] == 0

def test_congelar_no_lanza_error_en_borde():
    juego = _juego()
    pieza = _pieza_cuadrado(x=3, y=18)
    try:
        congelar_pieza(pieza, juego)
        assert True
    except IndexError:
        assert False, "congelar_pieza lanzó IndexError cerca del borde"

#Ejecutor de pruebas
def ejecutar_prueba(nombre, prueba):
    try:
        prueba()
        print(f"{nombre}: True")
    except AssertionError:
        print(f"{nombre}: False")

if __name__ == "__main__":
    ejecutar_prueba(
        "test_bloques_se_escriben_en_field",
        test_bloques_se_escriben_en_field
    )

    ejecutar_prueba(
        "test_color_de_bloque_se_conserva",
        test_color_de_bloque_se_conserva
    )

    ejecutar_prueba(
        "test_celdas_vacias_no_se_modifican",
        test_celdas_vacias_no_se_modifican
    )

    ejecutar_prueba(
        "test_congelar_no_lanza_error_en_borde",
        test_congelar_no_lanza_error_en_borde
    )