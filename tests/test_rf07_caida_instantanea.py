import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.rf01_inicializar_tablero import inicializar_tablero
from logic.rf02_generar_pieza import generar_pieza
from logic.rf07_caida_instantanea import caida_instantanea

def _juego():
    return inicializar_tablero(20, 10)

def _pieza(x=3, y=0):
    p = generar_pieza(x=x, y=y)
    p["type"] = 6
    p["rotation"] = 0
    return p

def test_pieza_alcanza_posicion_mas_baja():
    resultado = caida_instantanea(_pieza(y=0), _juego())
    field = resultado["juego"]["field"]
    zona = [field[r][c] for r in range(17, 20) for c in range(3, 7)]
    assert any(v > 0 for v in zona)

def test_pieza_queda_congelada():
    resultado = caida_instantanea(_pieza(), _juego())
    assert resultado["congelada"] == True

def test_pieza_activa_es_none_tras_caida():
    resultado = caida_instantanea(_pieza(), _juego())
    assert resultado["pieza"] is None

def test_sin_pieza_activa_no_hace_nada():
    juego = _juego()
    resultado = caida_instantanea(None, juego)
    assert resultado["congelada"] == False
    assert resultado["pieza"] is None

def test_caida_respeta_obstaculos_en_campo():
    juego = _juego()
    for col in range(10):
        juego["field"][10][col] = 2
    resultado = caida_instantanea(_pieza(y=0), juego)
    field = resultado["juego"]["field"]
    assert all(field[r][c] == 0 or field[r][c] == 2
               for r in range(11, 20) for c in range(3, 7))

#Ejecutor de pruebas
def ejecutar_prueba(nombre, prueba):
    try:
        prueba()
        print(f"{nombre}: True")
    except AssertionError:
        print(f"{nombre}: False")

if __name__ == "__main__":
    ejecutar_prueba(
        "test_pieza_alcanza_posicion_mas_baja",
        test_pieza_alcanza_posicion_mas_baja
    )

    ejecutar_prueba(
        "test_pieza_queda_congelada",
        test_pieza_queda_congelada
    )

    ejecutar_prueba(
        "test_pieza_activa_es_none_tras_caida",
        test_pieza_activa_es_none_tras_caida
    )

    ejecutar_prueba(
        "test_sin_pieza_activa_no_hace_nada",
        test_sin_pieza_activa_no_hace_nada
    )

    ejecutar_prueba(
        "test_caida_respeta_obstaculos_en_campo",
        test_caida_respeta_obstaculos_en_campo
    )