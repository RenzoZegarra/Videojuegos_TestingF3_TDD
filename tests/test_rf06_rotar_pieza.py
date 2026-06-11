import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.rf01_inicializar_tablero import inicializar_tablero
from logic.rf02_generar_pieza import generar_pieza, get_imagen_pieza, get_num_rotaciones
from logic.rf06_rotar_pieza import rotar_pieza

def _juego():
    return inicializar_tablero(20, 10)

def _pieza(tipo=0, x=4, y=5):
    p = generar_pieza(x=x, y=y)
    p["type"] = tipo
    p["rotation"] = 0
    return p

def test_rotacion_avanza_en_campo_libre():
    pieza = _pieza(tipo=0)
    pieza = rotar_pieza(pieza, _juego())
    assert pieza["rotation"] == 1

def test_rotacion_es_ciclica():
    pieza = _pieza(tipo=0)   # palo: 2 rotaciones → 0→1→0
    juego = _juego()
    pieza = rotar_pieza(pieza, juego)
    pieza = rotar_pieza(pieza, juego)
    assert pieza["rotation"] == 0

def test_imagen_coincide_con_rotacion_actual():
    pieza = _pieza(tipo=0)
    juego = _juego()
    pieza = rotar_pieza(pieza, juego)
    from logic.rf02_generar_pieza import FIGURES
    esperada = FIGURES[0][pieza["rotation"]]
    assert get_imagen_pieza(pieza) == esperada

def test_rotacion_se_revierte_si_colisiona():
    juego = _juego()
    for col in range(10):
        juego["field"][6][col] = 1
    pieza = _pieza(tipo=0, x=4, y=5)
    rotacion_original = pieza["rotation"]
    pieza = rotar_pieza(pieza, juego)
    assert pieza["rotation"] == rotacion_original

def test_cuadrado_no_cambia_visualmente_pero_no_falla():
    pieza = _pieza(tipo=6)
    pieza = rotar_pieza(pieza, _juego())
    assert pieza["rotation"] == 0

#Ejecutor de pruebas
def ejecutar_prueba(nombre, prueba):
    try:
        prueba()
        print(f"{nombre}: True")
    except AssertionError:
        print(f"{nombre}: False")

if __name__ == "__main__":
    ejecutar_prueba(
        "test_rotacion_avanza_en_campo_libre",
        test_rotacion_avanza_en_campo_libre
    )

    ejecutar_prueba(
        "test_rotacion_es_ciclica",
        test_rotacion_es_ciclica
    )

    ejecutar_prueba(
        "test_imagen_coincide_con_rotacion_actual",
        test_imagen_coincide_con_rotacion_actual
    )

    ejecutar_prueba(
        "test_rotacion_se_revierte_si_colisiona",
        test_rotacion_se_revierte_si_colisiona
    )

    ejecutar_prueba(
        "test_cuadrado_no_cambia_visualmente_pero_no_falla",
        test_cuadrado_no_cambia_visualmente_pero_no_falla
    )