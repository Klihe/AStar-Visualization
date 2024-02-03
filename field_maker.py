import pygame
import numpy as np

from modules.color import Color
from modules.config import Config

window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
clock = pygame.time.Clock()

color = [Color.WHITE, Color.BLACK, Color.BLUE, Color.YELLOW]
color_value = 0

class Node:
    def __init__(self, x, y, color=Color.WHITE) -> None:
        self.x = x
        self.y = y 
        self.point = (x, y)

        self.color = color

        self.rect = pygame.Rect(x*Config.NODE_SIZE, y*Config.NODE_SIZE, Config.NODE_SIZE, Config.NODE_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

nodes = np.empty((Config.COLUMNS, Config.ROWS), dtype=object)

for i in range(Config.COLUMNS):
    for j in range(Config.ROWS):
        nodes[i][j] = Node(i, j)


def grid():
    for i in range(Config.COLUMNS):
        pygame.draw.line(window, Color.BLACK, (i*Config.NODE_SIZE,0), (i*Config.NODE_SIZE, Config.WINDOW_HEIGHT), Config.GRID_THICKNESS)
    for i in range(Config.ROWS):
        pygame.draw.line(window, Color.BLACK, (0, i*Config.NODE_SIZE), (Config.WINDOW_WIDTH, i*Config.NODE_SIZE), Config.GRID_THICKNESS)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    print(color_value)
    window.fill(color[color_value])


    for i in range(Config.COLUMNS):
        for j in range(Config.ROWS):
            nodes[i][j].draw(window)

            if nodes[i][j].rect.collidepoint(mouse_pos):
                if mouse_click[0] == 1:

                    nodes[i][j].color = color[color_value]

    if keys[pygame.K_TAB]:
        pygame.time.delay(200)
        if color_value < len(color) -1:
            color_value += 1
        else:
            color_value = 0

    grid()

    pygame.display.flip()

with open("data/from_maker.txt", "w") as file:
    for i in range(Config.COLUMNS):
        for j in range(Config.ROWS):
            if nodes[i][j].color == Color.BLACK:
                file.write(f"BLACK: {nodes[i][j].point}\n")
            elif nodes[i][j].color == Color.BLUE:
                file.write(f"BLUE: {nodes[i][j].point}\n")
            elif nodes[i][j].color == Color.YELLOW:
                file.write(f"YELLOW: {nodes[i][j].point}\n")

pygame.quit()