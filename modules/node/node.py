# node.py

# imports of modules
from modules.color import Color
from modules.config import Config

# imports of libraries
import math
import pygame

# Node class to create the nodes of the grid
class Node:
    def __init__(self, x: int, y: int, node_start: tuple[int], node_end: tuple[int], color: Color=Color.WHITE) -> None:
        # basic attributes of the node
        self.x = x
        self.y = y 
        self.point = (x, y)
        self.color = color

        # rectangle to draw the node
        self.rect = pygame.Rect(x*Config.NODE_SIZE, y*Config.NODE_SIZE, Config.NODE_SIZE, Config.NODE_SIZE)

        # attributes to calculate the path
        self.node_start = node_start
        self.node_end = node_end
        self.g = 0

    # function to update the values of the node
    def update_values(self, calc_point: tuple[int], calc_g: int = 0) -> None:
        # form start to current node
        self.g = round(calc_g + math.sqrt((calc_point[0] - self.point[0])**2 + (calc_point[1] - self.point[1])**2) * 10)

        # from current node to end
        self.h = round(math.sqrt((self.node_end[0] - self.x)**2 + (self.node_end[1] - self.y)**2) * 10)

        # total distance
        self.f = self.g + self.h

    # function to draw the node
    def draw(self, surface: pygame.surface.Surface, font: pygame.font.Font) -> None:
        # draw the node
        pygame.draw.rect(surface, self.color, self.rect)

        # draw the values of the node
        if self.color == Color.GREEN or self.color == Color.RED:
            text_g = font.render(f"{round(self.g)}", None, Color.BLACK)
            text_h = font.render(f"{round(self.h)}", None, Color.BLACK)
            text_f = font.render(f"{round(self.f)}", None, Color.BLACK)
            surface.blit(text_g, (self.rect.x + Config.NODE_SIZE/20, self.rect.y + Config.NODE_SIZE/20))
            surface.blit(text_h, (self.rect.x + Config.NODE_SIZE/2, self.rect.y + Config.NODE_SIZE/20))
            surface.blit(text_f, (self.rect.x + Config.NODE_SIZE/3, self.rect.y + Config.NODE_SIZE/2))