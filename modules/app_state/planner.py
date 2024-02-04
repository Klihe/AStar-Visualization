# planner.py

import pygame

from modules.color import Color
from modules.config import Config

class Planner:
    def __init__(self, nodes) -> None:
        self.colors = [Color.WHITE, Color.BLACK, Color.BLUE, Color.YELLOW]
        self.choosen_color = 0
        self.nodes = nodes

    def drawing(self, mouse_click, mouse_pos) -> None:
        for i in range(Config.COLUMNS):
            for j in range(Config.ROWS):
                if self.nodes[i][j].rect.collidepoint(mouse_pos):
                    if mouse_click[0] == 1:
                        self.nodes[i][j].color = self.colors[self.choosen_color]

    def change_color(self, keys) -> None:
        if keys[pygame.K_TAB]:
            pygame.time.delay(200)
            if self.choosen_color < len(self.colors) -1:
                self.choosen_color += 1
            else:
                self.choosen_color = 0