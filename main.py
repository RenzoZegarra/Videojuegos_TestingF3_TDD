# main.py — Tetris en consola (sin interfaz gráfica)
# Propósito: verificar que toda la lógica funciona antes de agregar Pygame.
# Cada llamada corresponde a un RF definido en el PDF de requerimientos.

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from logic.rf01_inicializar_tablero  import inicializar_tablero
from logic.rf02_generar_pieza        import generar_pieza, get_imagen_pieza
from logic.rf03_detectar_colision    import detectar_colision
from logic.rf04_mover_abajo          import mover_abajo
from logic.rf05_mover_lateral        import mover_lateral
from logic.rf06_rotar_pieza          import rotar_pieza
from logic.rf07_caida_instantanea    import caida_instantanea
from logic.rf08_congelar_pieza       import congelar_pieza
from logic.rf09_eliminar_lineas      import eliminar_lineas
from logic.rf10_detectar_game_over   import detectar_game_over


# ── Utilidades de consola ─────────────────────────────────────────────────────

def imprimir_tablero(juego: dict, pieza: dict = None):
    """Dibuja el tablero en consola con la pieza activa superpuesta."""
    field  = [fila[:] for fila in juego["field"]]  # copia superficial
    height = juego["height"]
    width  = juego["width"]

    # superponer pieza activa (solo visual, no modifica el field real)
    if pieza:
        imagen = get_imagen_pieza(pieza)
        for i in range(4):
            for j in range(4):
                if i * 4 + j in imagen:
                    fila = i + pieza["y"]
                    col  = j + pieza["x"]
                    if 0 <= fila < height and 0 <= col < width:
                        field[fila][col] = pieza["color"]

    borde = "+" + "-" * (width * 2) + "+"
    print(borde)
    for fila in field:
        celda = "".join("██" if c > 0 else "  " for c in fila)
        print(f"|{celda}|")
    print(borde)
    print(f"  Score: {juego['score']}   Estado: {juego['state']}")
    print()


def pedir_accion() -> str:
    print("Acciones: [w] rotar  [a] izq  [d] der  [s] bajar  [espacio] caída  [q] salir")
    return input(">> ").strip().lower()


# ── Bucle principal ───────────────────────────────────────────────────────────

def main():
    print("=== TETRIS (modo consola — sin interfaz gráfica) ===\n")

    # RF-01: Inicializar tablero
    juego = inicializar_tablero(height=20, width=10)
    if juego is None:
        print("[ERROR] No se pudo inicializar el tablero.")
        return

    # RF-02: Generar primera pieza
    pieza = generar_pieza(x=3, y=0)

    # RF-10: Verificar game over al generar la primera pieza
    juego = detectar_game_over(pieza, juego)

    while juego["state"] != "gameover":
        imprimir_tablero(juego, pieza)
        accion = pedir_accion()

        if accion == "q":
            print("Juego terminado por el jugador.")
            break

        elif accion == "a":
            # RF-05: mover izquierda
            pieza = mover_lateral(pieza, juego, dx=-1)

        elif accion == "d":
            # RF-05: mover derecha
            pieza = mover_lateral(pieza, juego, dx=1)

        elif accion == "w":
            # RF-06: rotar
            pieza = rotar_pieza(pieza, juego)

        elif accion == "s":
            # RF-04: bajar una celda
            resultado = mover_abajo(pieza, juego)
            pieza = resultado["pieza"]
            juego = resultado["juego"]
            if resultado["congelada"]:
                # RF-02: nueva pieza
                pieza = generar_pieza(x=3, y=0)
                # RF-10: verificar game over
                juego = detectar_game_over(pieza, juego)

        elif accion == " ":
            # RF-07: caída instantánea
            resultado = caida_instantanea(pieza, juego)
            pieza = resultado["pieza"]
            juego = resultado["juego"]
            if resultado["congelada"]:
                # RF-02: nueva pieza
                pieza = generar_pieza(x=3, y=0)
                # RF-10: verificar game over
                juego = detectar_game_over(pieza, juego)

    # Fin de partida
    imprimir_tablero(juego, pieza)
    print("╔══════════════════╗")
    print("║    GAME  OVER    ║")
    print(f"║  Puntaje: {juego['score']:>6}  ║")
    print("╚══════════════════╝")
    print("\nReinicia el programa para jugar de nuevo.")


if __name__ == "__main__":
    main()
