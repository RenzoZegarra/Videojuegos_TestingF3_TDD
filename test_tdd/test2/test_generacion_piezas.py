# Código mínimo
def generar_pieza(x=3, y=0):
    return {
        "type": 0,
        "color": 6,
        "rotation": 0,
        "x": x,
        "y": y,
    }


# Prueba unitaria
def test_generacion_piezas(x, y):
    resultado = generar_pieza(x, y)

    esperado = {
        "type": 0,
        "color": 6,
        "rotation": 0,
        "x": 3,
        "y": 0,
    }
    assert resultado == esperado
    return True

print("Test de generación de piezas: ", test_generacion_piezas(3, 0))


