# main.py

import pygame
import numpy as np

from modules.color import Color
from modules.config import Config

from modules.node import Node

pygame.init()
window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
pygame.display.set_caption("PathFinding")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

nodes = np.empty((Config.COLUMNS, Config.ROWS), dtype=object)

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

nodes[Config.START_POINT[0]][Config.START_POINT[1]].color = Color.YELLOW
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
            node.draw(window, font)

    if mouse_click[0] == 1:
        pygame.time.delay(500)
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
        pygame.time.delay(500)
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