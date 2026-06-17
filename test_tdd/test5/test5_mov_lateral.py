# Código mínimo
def mover_lateral(pieza: dict, juego: dict, dx: int) -> dict:
    pieza["x"] += dx
    return pieza


# Test
def test_mover_lateral_sin_colision():
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
        "y": 1
    }

    resultado = mover_lateral(pieza.copy(), juego, dx=1)

    # La pieza debe haberse movido a la derecha
    assert resultado["x"] == 2

    # Debe haber cambiado correctamente
    assert resultado != pieza

    return True

print("Prueba de movimiento lateral: ", test_mover_lateral_sin_colision())