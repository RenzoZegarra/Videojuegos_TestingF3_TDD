import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.rf01_inicializar_tablero import inicializar_tablero
from logic.rf02_generar_pieza import generar_pieza
from logic.rf04_mover_abajo import mover_abajo

def _juego():
    return inicializar_tablero(20, 10)

def _pieza_cuadrado(x=3, y=5):
    p = generar_pieza(x=x, y=y)
    p["type"] = 6
    p["rotation"] = 0
    return p

def test_pieza_baja_una_celda_si_hay_espacio():
    pieza = _pieza_cuadrado(y=5)
    resultado = mover_abajo(pieza, _juego())
    assert resultado["pieza"]["y"] == 6

def test_pieza_no_se_congela_si_hay_espacio():
    pieza = _pieza_cuadrado(y=5)
    resultado = mover_abajo(pieza, _juego())
    assert resultado["congelada"] == False

def test_pieza_se_congela_al_llegar_al_fondo():
    # cuadrado en y=18: ocupa filas 18,19. Al intentar y=19 -> fila 20 >= height -> colisiona
    pieza = _pieza_cuadrado(y=18)
    resultado = mover_abajo(pieza, _juego())
    assert resultado["congelada"] == True

def test_field_se_actualiza_al_congelarse():
    juego = _juego()
    pieza = _pieza_cuadrado(x=3, y=18)
    resultado = mover_abajo(pieza, juego)
    field = resultado["juego"]["field"]
    zona = [field[r][c] for r in range(18, 20) for c in range(4, 6)]
    assert any(v > 0 for v in zona)

def test_pieza_retorna_none_tras_congelarse():
    pieza = _pieza_cuadrado(y=18)
    resultado = mover_abajo(pieza, _juego())
    assert resultado["pieza"] is None

#Ejecutor de pruebas
def ejecutar_prueba(nombre, prueba):
    try:
        prueba()
        print(f"{nombre}: True")
    except AssertionError:
        print(f"{nombre}: False")

if __name__ == "__main__":
    ejecutar_prueba(
        "test_pieza_baja_una_celda_si_hay_espacio",
        test_pieza_baja_una_celda_si_hay_espacio
    )

    ejecutar_prueba(
        "test_pieza_no_se_congela_si_hay_espacio",
        test_pieza_no_se_congela_si_hay_espacio
    )

    ejecutar_prueba(
        "test_pieza_se_congela_al_llegar_al_fondo",
        test_pieza_se_congela_al_llegar_al_fondo
    )

    ejecutar_prueba(
        "test_field_se_actualiza_al_congelarse",
        test_field_se_actualiza_al_congelarse
    )

    ejecutar_prueba(
        "test_pieza_retorna_none_tras_congelarse",
        test_pieza_retorna_none_tras_congelarse
    )