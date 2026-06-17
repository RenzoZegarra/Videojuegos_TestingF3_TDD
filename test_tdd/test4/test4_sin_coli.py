#Mínimo código
def mover_abajo(pieza, juego):
    pieza["y"] += 1
    return {
        "pieza": pieza,
        "congelada": False,
        "juego": juego
    }



#Prueba
def test_mover_abajo_sin_colision():
    juego = {
        "field": [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        "height": 4,
        "width": 4
    }

    pieza = {
        "type": 6,
        "rotation": 0,
        "x": 1,
        "y": 0
    }

    resultado = mover_abajo(pieza.copy(), juego)

    # La pieza debe haber bajado una celda
    assert resultado["pieza"]["y"] == 1

    # No debe estar congelada
    assert resultado["congelada"] == False

    # El juego no debe cambiar
    assert resultado["juego"] == juego

    return True

print("Test para bajar la pieza sin colisión: ", test_mover_abajo_sin_colision())