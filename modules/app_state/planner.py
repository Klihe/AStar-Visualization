# planner.py

import pygame

from modules.color import Color
from modules.config import Config

def planner(mouse_click, mouse_pos, keys, all_nodes, color_value) -> int:
    color = [Color.WHITE, Color.BLACK, Color.BLUE, Color.YELLOW]

    for i in range(Config.COLUMNS):
        for j in range(Config.ROWS):

            if all_nodes[i][j].rect.collidepoint(mouse_pos):
                if mouse_click[0] == 1:

                    all_nodes[i][j].color = color[color_value]

    if keys[pygame.K_TAB]:
        pygame.time.delay(200)
        if color_value < len(color) -1:
            color_value += 1
        else:
            color_value = 0

    print(color[color_value])

    return color_value