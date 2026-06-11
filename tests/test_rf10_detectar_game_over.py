import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.rf01_inicializar_tablero import inicializar_tablero
from logic.rf02_generar_pieza import generar_pieza
from logic.rf10_detectar_game_over import detectar_game_over

def _juego():
    return inicializar_tablero(20, 10)

def _pieza(x=3, y=0):
    p = generar_pieza(x=x, y=y)
    p["type"] = 6
    p["rotation"] = 0
    return p

def test_estado_no_cambia_si_hay_espacio():
    juego = _juego()
    pieza = _pieza()
    juego = detectar_game_over(pieza, juego)
    assert juego["state"] == "start"

def test_estado_cambia_a_gameover_si_colisiona():
    juego = _juego()
    juego["field"][0][4] = 1
    juego["field"][0][5] = 1
    pieza = _pieza()
    juego = detectar_game_over(pieza, juego)
    assert juego["state"] == "gameover"

def test_state_es_string_gameover():
    juego = _juego()
    juego["field"][0][4] = 1
    pieza = _pieza()
    juego = detectar_game_over(pieza, juego)
    assert isinstance(juego["state"], str)
    assert juego["state"] == "gameover"

def test_tablero_no_se_modifica_al_detectar_game_over():
    juego = _juego()
    juego["field"][0][4] = 1
    pieza = _pieza()
    field_antes = [fila[:] for fila in juego["field"]]
    juego = detectar_game_over(pieza, juego)
    assert juego["field"] == field_antes

#Ejecutor de pruebas
def ejecutar_prueba(nombre, prueba):
    try:
        prueba()
        print(f"{nombre}: True")
    except AssertionError:
        print(f"{nombre}: False")

if __name__ == "__main__":
    ejecutar_prueba(
        "test_estado_no_cambia_si_hay_espacio",
        test_estado_no_cambia_si_hay_espacio
    )

    ejecutar_prueba(
        "test_estado_cambia_a_gameover_si_colisiona",
        test_estado_cambia_a_gameover_si_colisiona
    )

    ejecutar_prueba(
        "test_state_es_string_gameover",
        test_state_es_string_gameover
    )

    ejecutar_prueba(
        "test_tablero_no_se_modifica_al_detectar_game_over",
        test_tablero_no_se_modifica_al_detectar_game_over
    )