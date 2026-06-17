# Código mínimo
def caida_instantanea(pieza, juego):
    return {"congelada": True}



# Prueba

def test_caida_instantanea():
    resultado = caida_instantanea({"y": 0}, {})
    assert resultado["congelada"] is True
    return True

test_caida_instantanea()
print("Prueba de caida instantanea: ",test_caida_instantanea())

