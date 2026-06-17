# main2.py — Tetris con interfaz gráfica (Pygame)
# Usa exactamente los mismos módulos de logic/ que ya pasaron
# las 52 pruebas unitarias. Este archivo solo conecta eventos
# de teclado con esas funciones y delega el dibujado a ui/renderer.py.

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pygame

from logic.rf01_inicializar_tablero import inicializar_tablero
from logic.rf02_generar_pieza        import generar_pieza
from logic.rf04_mover_abajo          import mover_abajo
from logic.rf05_mover_lateral        import mover_lateral
from logic.rf06_rotar_pieza          import rotar_pieza
from logic.rf07_caida_instantanea    import caida_instantanea
from logic.rf10_detectar_game_over   import detectar_game_over

from ui.colores import WINDOW_SIZE, FPS
from ui.renderer import dibujar_frame


def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Tetris")

    fuente        = pygame.font.SysFont('Calibri', 25, True, False)
    fuente_grande = pygame.font.SysFont('Calibri', 65, True, False)

    clock = pygame.time.Clock()

    # RF-01: Inicializar tablero
    juego = inicializar_tablero(height=20, width=10)

    # RF-02: Generar primera pieza
    pieza = generar_pieza(x=3, y=0)

    # RF-10: Verificar game over al generar la primera pieza
    juego = detectar_game_over(pieza, juego)

    nivel = 2
    counter = 0
    pressing_down = False
    done = False

    while not done:
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (FPS // nivel // 2) == 0 or pressing_down:
            if juego["state"] == "start" and pieza is not None:
                resultado = mover_abajo(pieza, juego)
                pieza = resultado["pieza"]
                juego = resultado["juego"]
                if resultado["congelada"]:
                    pieza = generar_pieza(x=3, y=0)
                    juego = detectar_game_over(pieza, juego)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if juego["state"] == "start" and pieza is not None:
                    if event.key == pygame.K_UP:
                        pieza = rotar_pieza(pieza, juego)

                    if event.key == pygame.K_DOWN:
                        pressing_down = True

                    if event.key == pygame.K_LEFT:
                        pieza = mover_lateral(pieza, juego, dx=-1)

                    if event.key == pygame.K_RIGHT:
                        pieza = mover_lateral(pieza, juego, dx=1)

                    if event.key == pygame.K_SPACE:
                        resultado = caida_instantanea(pieza, juego)
                        pieza = resultado["pieza"]
                        juego = resultado["juego"]
                        if resultado["congelada"]:
                            pieza = generar_pieza(x=3, y=0)
                            juego = detectar_game_over(pieza, juego)

                if event.key == pygame.K_ESCAPE:
                    juego = inicializar_tablero(height=20, width=10)
                    pieza = generar_pieza(x=3, y=0)
                    juego = detectar_game_over(pieza, juego)
                    pressing_down = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

        dibujar_frame(screen, juego, pieza, fuente, fuente_grande)
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()