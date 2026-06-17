# Código mínimo
def detectar_colision(pieza: dict, juego: dict) -> bool:
    return juego["field"][pieza["y"]][pieza["x"]] == 1

def mover_abajo(pieza: dict, juego: dict) -> dict:
    pieza["y"] += 1

    if detectar_colision(pieza, juego):
        pieza["y"] -= 1
        juego["field"][pieza["y"]][pieza["x"]] = pieza["type"]
        return {"pieza": None, "juego": juego, "congelada": True}

    return {"pieza": pieza, "juego": juego, "congelada": False}




# Prueba
def test_mover_abajo_colision_congela():
    juego = {
        "field": [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0]  # Bloque que provocará colisión
        ],
        "height": 4,
        "width": 4
    }

    pieza = {
        "type": 6,
        "rotation": 0,
        "x": 0,
        "y": 2  # Al bajar intentará ir a y=3 donde hay un 1
    }

    resultado = mover_abajo(pieza.copy(), juego)

    # Debe detectarse colisión y congelarse
    assert resultado["congelada"] == True

    # La pieza activa debe desaparecer (porque se congeló)
    assert resultado["pieza"] is None

    return True

print("Test para bajar la pieza y se congele por colisión: ", test_mover_abajo_colision_congela())