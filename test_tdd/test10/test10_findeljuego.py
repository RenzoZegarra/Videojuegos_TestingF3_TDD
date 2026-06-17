#MINIMO CODIGO
pieza = {}
juego = {}

def detectar_game_over(pieza, juego):
    return juego

#PRUEBA
def test_detectar_game_over():
    juego_actualizado = detectar_game_over(pieza, juego)
    assert juego_actualizado is not None
    return True

print("Prueba de fin del juego: ",test_detectar_game_over())
