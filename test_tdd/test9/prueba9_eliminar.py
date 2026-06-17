#CODIGO MINIMO
juego = {}

def eliminar_lineas(juego):
    return juego

#PRUEBA
def test_eliminar_lineas():
    juego_actualizado = eliminar_lineas(juego)
    assert juego_actualizado is not None
    return True

print("Prueba de eliminacion de lineas: ",test_eliminar_lineas())
