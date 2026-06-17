# ui/renderer.py
# Funciones de dibujado en pantalla usando Pygame.
# Solo se encargan de PINTAR el estado del juego, no contienen
# lógica del juego — esa vive en logic/ y ya está probada con tests.

import pygame
from ui.colores import COLORS, BLACK, WHITE, GRAY, ORANGE, GOLD, GRID_X, GRID_Y, ZOOM
from logic.rf02_generar_pieza import get_imagen_pieza


def dibujar_tablero(screen, juego):
    height = juego["height"]
    width  = juego["width"]
    field  = juego["field"]

    for i in range(height):
        for j in range(width):
            rect = [GRID_X + ZOOM * j, GRID_Y + ZOOM * i, ZOOM, ZOOM]
            pygame.draw.rect(screen, GRAY, rect, 1)

            if field[i][j] > 0:
                relleno = [
                    GRID_X + ZOOM * j + 1,
                    GRID_Y + ZOOM * i + 1,
                    ZOOM - 2,
                    ZOOM - 1,
                ]
                pygame.draw.rect(screen, COLORS[field[i][j]], relleno)


def dibujar_pieza_activa(screen, pieza):
    if pieza is None:
        return

    imagen = get_imagen_pieza(pieza)

    for i in range(4):
        for j in range(4):
            if i * 4 + j in imagen:
                rect = [
                    GRID_X + ZOOM * (j + pieza["x"]) + 1,
                    GRID_Y + ZOOM * (i + pieza["y"]) + 1,
                    ZOOM - 2,
                    ZOOM - 2,
                ]
                pygame.draw.rect(screen, COLORS[pieza["color"]], rect)


def dibujar_score(screen, juego, fuente):
    texto = fuente.render("Score: " + str(juego["score"]), True, BLACK)
    screen.blit(texto, [0, 0])


def dibujar_game_over(screen, fuente_grande):
    texto1 = fuente_grande.render("Game Over", True, ORANGE)
    texto2 = fuente_grande.render("Press ESC", True, GOLD)
    screen.blit(texto1, [20, 200])
    screen.blit(texto2, [25, 265])


def dibujar_frame(screen, juego, pieza, fuente, fuente_grande):
    screen.fill(WHITE)
    dibujar_tablero(screen, juego)
    dibujar_pieza_activa(screen, pieza)
    dibujar_score(screen, juego, fuente)

    if juego["state"] == "gameover":
        dibujar_game_over(screen, fuente_grande)

    pygame.display.flip()