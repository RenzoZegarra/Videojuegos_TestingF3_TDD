#Código minimo
pieza = {"y": 0}
juego = {}

def congelar_pieza(pieza, juego):
    juego["pieza"] = pieza
    return juego


# Prueba
def test_congelar_pieza():
    resultado = congelar_pieza(pieza, juego)
    assert resultado is not None
    return True

print("Prueba de fijar pieza: ", test_congelar_pieza())
