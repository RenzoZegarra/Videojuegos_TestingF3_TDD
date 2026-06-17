# ui/colores.py
# Paleta de colores e configuración visual del tablero.
# Separado en su propio archivo para que el renderer no mezcle
# datos visuales con lógica de dibujado.

COLORS = [
    (0, 0, 0),        # índice 0 — no se usa (celda vacía)
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY  = (128, 128, 128)
ORANGE = (255, 125, 0)
GOLD   = (255, 215, 0)

GRID_X = 100
GRID_Y = 60
ZOOM   = 20

WINDOW_SIZE = (400, 500)
FPS = 25