# planner.py

import pygame

from modules.color import Color
from modules.config import Config

class Planner:
    def __init__(self, nodes: list) -> None:
        self.colors = [Color.BLACK, Color.YELLOW, Color.BLUE, Color.WHITE]
        self.choosen_color: int = 0
        self.nodes: list = nodes

    def drawing(self, mouse_click, mouse_pos) -> None:
        for i in range(Config.COLUMNS):
            for j in range(Config.ROWS):
                if self.nodes[i][j].rect.collidepoint(mouse_pos):
                    if mouse_click[0] == 1:
                        self.nodes[i][j].color = self.colors[self.choosen_color]

    def change_color(self, keys) -> None:
        if keys[pygame.K_RIGHT]:
            if self.choosen_color >= len(self.colors) - 1:
                self.choosen_color = 0
            else:
                self.choosen_color += 1
            pygame.time.delay(100)
        elif keys[pygame.K_LEFT]:
            if self.choosen_color <= 0:
                self.choosen_color = len(self.colors) - 1
            else:
                self.choosen_color -= 1
            pygame.time.delay(100)
    
    def draw(self, surface, mouse_pos):
        image = pygame.image.load("source/colors.png")
        image_2 = pygame.image.load("source/frame.png")
        surface.blit(image, (mouse_pos[0]-25, mouse_pos[1]))
        surface.blit(image_2, (mouse_pos[0]-27, mouse_pos[1]-2+self.choosen_color*10))