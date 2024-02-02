# main.py

import pygame
import numpy as np
import math

from modules.color import Color
from modules.config import Config

pygame.init()
window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
pygame.display.set_caption("PathFinding")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

nodes = np.empty((Config.COLUMNS, Config.ROWS), dtype=object)

class Node:
    def __init__(self, x, y, color=Color.WHITE) -> None:
        self.x = x
        self.y = y 
        self.point = (x, y)
        self.color = color

        self.rect = pygame.Rect(x*Config.NODE_SIZE, y*Config.NODE_SIZE, Config.NODE_SIZE, Config.NODE_SIZE)

        self.g = round(math.sqrt((Config.START_POINT[0] - self.x)**2 + (Config.START_POINT[1] - self.y)**2) * 10)
        self.h = round(math.sqrt((Config.END_POINT[0] - self.x)**2 + (Config.END_POINT[1] - self.y)**2) * 10)
        self.f = self.g + self.h

    def update_values(self, calc_point, calc_g):
        self.g = round(calc_g + math.sqrt((calc_point[0] - self.point[0])**2 + (calc_point[1] - self.point[1])**2) * 10)
        self.f = self.g + self.h

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

        if self.color == Color.GREEN or self.color == Color.RED:
            text_g = font.render(f"{round(self.g)}", None, Color.BLACK)
            text_h = font.render(f"{round(self.h)}", None, Color.BLACK)
            text_f = font.render(f"{round(self.f)}", None, Color.BLACK)
            window.blit(text_g, (self.rect.x + Config.NODE_SIZE/20, self.rect.y + Config.NODE_SIZE/20))
            window.blit(text_h, (self.rect.x + Config.NODE_SIZE/2, self.rect.y + Config.NODE_SIZE/20))
            window.blit(text_f, (self.rect.x + Config.NODE_SIZE/3, self.rect.y + Config.NODE_SIZE/2))

def grid():
    for i in range(Config.COLUMNS):
        pygame.draw.line(window, Color.BLACK, (i*Config.NODE_SIZE,0), (i*Config.NODE_SIZE, Config.WINDOW_HEIGHT), Config.GRID_THICKNESS)
    for i in range(Config.ROWS):
        pygame.draw.line(window, Color.BLACK, (0, i*Config.NODE_SIZE), (Config.WINDOW_WIDTH, i*Config.NODE_SIZE), Config.GRID_THICKNESS)

def barriers(cors):
    for pos in cors:
        nodes[pos[0]][pos[1]].color = Color.BLACK

for i in range(Config.COLUMNS):
    for j in range(Config.ROWS):
        nodes[i][j] = Node(i, j)

nodes[Config.START_POINT[0]][Config.START_POINT[1]].color = Color.BLUE
nodes[Config.END_POINT[0]][Config.END_POINT[1]].color = Color.BLUE

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    for i in range(Config.COLUMNS):
        for j in range(Config.ROWS):
            node = nodes[i, j]
            node.draw()

    if mouse_click[0] == 1:
        pygame.time.delay(100)
        last_node = Config.START_POINT
        green_nodes = []
        end = False

        while not end:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbor_x = last_node[0] + i
                    neighbor_y = last_node[1] + j

                    if 0 <= neighbor_x < Config.COLUMNS and 0 <= neighbor_y < Config.ROWS:
                        neighbor_node = nodes[neighbor_x, neighbor_y]


                        if neighbor_node.point == Config.END_POINT:
                            end = True

                        elif neighbor_node.color == Color.WHITE:
                            neighbor_node.color = Color.GREEN
                            neighbor_node.update_values(nodes[last_node[0]][last_node[1]].point, nodes[last_node[0]][last_node[1]].g)
                            green_nodes.append(neighbor_node)

                        
            if not end:
                green_nodes = sorted(green_nodes, key=lambda x: x.f)
                for l in green_nodes:
                    print(f"h: {l.f}")
                green_nodes[0].color = Color.RED
                last_node = green_nodes[0].point
                green_nodes.pop(0)
                print(f"{last_node}")

    if mouse_click[2] == 1:
        pygame.time.delay(100)
        last_node = Config.END_POINT
        red_nodes = []
        start = False
        
        while not start:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbor_x = last_node[0] + i
                    neighbor_y = last_node[1] + j

                    if 0 <= neighbor_x < Config.COLUMNS and 0 <= neighbor_y < Config.ROWS:
                        neighbor_node = nodes[neighbor_x, neighbor_y]

                        if neighbor_node.point == Config.START_POINT:
                            start = True

                        elif neighbor_node.color == Color.RED:
                            red_nodes.append(neighbor_node)

            if not start:
                red_nodes = sorted(red_nodes, key=lambda x: x.g)
                red_nodes[0].color = Color.BLUE
                last_node = red_nodes[0].point
                red_nodes.pop(0)


    barriers(Config.BARRIERS_POS)
    grid()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()