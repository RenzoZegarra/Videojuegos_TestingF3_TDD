# Código mínimo

def get_imagen_pieza(pieza):
    return []

def detectar_colision(pieza: dict, juego: dict) -> bool:
    return False

def test_sin_colision():
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
        "x": 0,
        "y": 0
    }

    assert detectar_colision(pieza, juego) == False
    return False

print("Test de sin colisión: ", test_sin_colision())

