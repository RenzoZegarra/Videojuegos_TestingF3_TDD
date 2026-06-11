import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.rf01_inicializar_tablero import inicializar_tablero
from logic.rf09_eliminar_lineas import eliminar_lineas

def _juego():
    return inicializar_tablero(20, 10)

def _llenar_fila(juego, fila, valor=1):
    for col in range(juego["width"]):
        juego["field"][fila][col] = valor

def test_fila_completa_se_elimina():
    juego = _juego()
    _llenar_fila(juego, 19)
    juego = eliminar_lineas(juego)
    assert all(juego["field"][19][c] == 0 for c in range(10))

def test_filas_superiores_bajan():
    juego = _juego()
    juego["field"][18][0] = 3
    _llenar_fila(juego, 19)
    juego = eliminar_lineas(juego)
    assert juego["field"][19][0] == 3

def test_score_aumenta_con_1_linea():
    juego = _juego()
    _llenar_fila(juego, 19)
    juego = eliminar_lineas(juego)
    assert juego["score"] == 1   # 1² = 1

def test_score_aumenta_con_2_lineas_simultaneas():
    juego = _juego()
    _llenar_fila(juego, 18)
    _llenar_fila(juego, 19)
    juego = eliminar_lineas(juego)
    assert juego["score"] == 4   # 2² = 4

def test_sin_lineas_completas_score_no_cambia():
    juego = _juego()
    juego["field"][19][0] = 1
    juego = eliminar_lineas(juego)
    assert juego["score"] == 0

def test_sin_lineas_completas_field_no_cambia():
    juego = _juego()
    juego["field"][19][0] = 1
    juego = eliminar_lineas(juego)
    assert juego["field"][19][0] == 1

#Ejecutor de pruebas
def ejecutar_prueba(nombre, prueba):
    try:
        prueba()
        print(f"{nombre}: True")
    except AssertionError:
        print(f"{nombre}: False")

if __name__ == "__main__":
    ejecutar_prueba(
        "test_fila_completa_se_elimina",
        test_fila_completa_se_elimina
    )

    ejecutar_prueba(
        "test_filas_superiores_bajan",
        test_filas_superiores_bajan
    )

    ejecutar_prueba(
        "test_score_aumenta_con_1_linea",
        test_score_aumenta_con_1_linea
    )

    ejecutar_prueba(
        "test_score_aumenta_con_2_lineas_simultaneas",
        test_score_aumenta_con_2_lineas_simultaneas
    )

    ejecutar_prueba(
        "test_sin_lineas_completas_score_no_cambia",
        test_sin_lineas_completas_score_no_cambia
    )

    ejecutar_prueba(
        "test_sin_lineas_completas_field_no_cambia",
        test_sin_lineas_completas_field_no_cambia
    )