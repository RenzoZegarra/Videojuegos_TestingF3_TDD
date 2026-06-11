import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.rf02_generar_pieza import generar_pieza, get_imagen_pieza, FIGURES, NUM_COLORS

def test_pieza_es_un_diccionario():
    pieza = generar_pieza()
    assert isinstance(pieza, dict)

def test_tipo_en_rango_valido():
    for _ in range(20):
        pieza = generar_pieza()
        assert 0 <= pieza["type"] <= len(FIGURES) - 1

def test_color_en_rango_valido():
    for _ in range(20):
        pieza = generar_pieza()
        assert 1 <= pieza["color"] <= NUM_COLORS

def test_posicion_inicial_es_3_0():
    pieza = generar_pieza()
    assert pieza["x"] == 3
    assert pieza["y"] == 0

def test_rotacion_inicial_es_cero():
    pieza = generar_pieza()
    assert pieza["rotation"] == 0

def test_imagen_retorna_lista_de_4_celdas():
    pieza = generar_pieza()
    imagen = get_imagen_pieza(pieza)
    assert isinstance(imagen, list)
    assert len(imagen) == 4

#Ejecutor de pruebas
def ejecutar_prueba(nombre, prueba):
    try:
        prueba()
        print(f"{nombre}: True")
    except AssertionError:
        print(f"{nombre}: False")
    except Exception as e:
        print(f"{nombre}: Error ({e})")

if __name__ == "__main__":
    ejecutar_prueba("test_pieza_es_un_diccionario", test_pieza_es_un_diccionario)
    ejecutar_prueba("test_tipo_en_rango_valido", test_tipo_en_rango_valido)
    ejecutar_prueba("test_color_en_rango_valido", test_color_en_rango_valido)
    ejecutar_prueba("test_posicion_inicial_es_3_0", test_posicion_inicial_es_3_0)
    ejecutar_prueba("test_rotacion_inicial_es_cero", test_rotacion_inicial_es_cero)
    ejecutar_prueba("test_imagen_retorna_lista_de_4_celdas", test_imagen_retorna_lista_de_4_celdas)