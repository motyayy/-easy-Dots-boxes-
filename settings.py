import pygame

SCREEN = WIDTH, HEIGHT = 1400, 700
CELLSIZE = int(WIDTH/6)
PADDING = int(WIDTH/12)
ROWS = COLS = (WIDTH - 4 * PADDING) // CELLSIZE


WHITE = (255, 255, 255)
RED = (252, 91, 122)
BLUE = (78, 193, 246)
GREEN = (0, 255, 0)
BLACK = (12, 12, 12)

font = pygame.font.SysFont('cursive', 25)
