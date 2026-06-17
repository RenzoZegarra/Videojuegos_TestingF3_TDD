# Código mínimo
def rotar_pieza(pieza: dict, juego: dict) -> dict:
    pieza["rotation"] += 1
    return pieza

# Test
def test_rotar_pieza_sin_colision():
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
        "type": 2,
        "rotation": 0,
        "x": 1,
        "y": 1
    }

    resultado = rotar_pieza(pieza.copy(), juego)

    # La pieza debe haber rotado (de 0 a 1)
    assert resultado["rotation"] == 1

    # Debe ser la misma pieza actualizada
    assert resultado != pieza

    return True

print("Test de Rotación de pieza: ", test_rotar_pieza_sin_colision())