# background.py

# imports of modules
from modules.config import Config
from modules.color import Color

# imports of libraries
import pygame

# grid function draws the grid on the window
def grid(surface) -> None:
    for i in range(Config.COLUMNS):
        pygame.draw.line(surface, Color.BLACK, (i*Config.NODE_SIZE,0), (i*Config.NODE_SIZE, Config.WINDOW_HEIGHT), Config.GRID_THICKNESS)
    for i in range(Config.ROWS):
        pygame.draw.line(surface, Color.BLACK, (0, i*Config.NODE_SIZE), (Config.WINDOW_WIDTH, i*Config.NODE_SIZE), Config.GRID_THICKNESS)
