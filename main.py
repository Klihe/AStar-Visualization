# main.py

# libraries
import pygame
import numpy as np
import sys
import math

# custom libraries
from modules.color import Color
from modules.config import Config

# init window
pygame.init()
window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
pygame.display.set_caption("A* - PathFinding - Visualization")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

nodes = np.empty((Config.COLUMNS, Config.ROWS), dtype=object)
clicked_node = []

# class for Nodes
class Node:
    def __init__(self, x, y, color=Color.WHITE):
        # common values
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x*Config.NODE_SIZE, y*Config.NODE_SIZE, Config.NODE_SIZE, Config.NODE_SIZE)
        self.point = (x, y)
        self.color = color

        # auxiliary values
        self.g = 0

    # update values
    def update_values(self, g_point=Config.START_POINT, g=0):
        # g = distance from start
        self.g = round(g + math.sqrt((g_point[0] - self.point[0])**2 + (g_point[1] - self.point[1])**2) * 10)
        # h = distance to end
        self.h = round(math.sqrt((Config.END_POINT[0] - self.point[0])**2 + (Config.END_POINT[1] - self.point[1])**2) * 10)
        # f = g value + h value
        self.f = self.g + self.h

    def draw(self):
        # display node
        pygame.draw.rect(window, self.color, self.rect)

        # update display UI values
        if self.color == Color.GREEN or self.color == Color.RED:
            text_g = font.render(f"{round(self.g)}", None, Color.BLACK)
            text_h = font.render(f"{round(self.h)}", None, Color.BLACK)
            text_f = font.render(f"{round(self.f)}", None, Color.BLACK)
            window.blit(text_g, (self.rect.x + Config.NODE_SIZE/20, self.rect.y + Config.NODE_SIZE/20))
            window.blit(text_h, (self.rect.x + Config.NODE_SIZE/2, self.rect.y + Config.NODE_SIZE/20))
            window.blit(text_f, (self.rect.x + Config.NODE_SIZE/3, self.rect.y + Config.NODE_SIZE/2))

# draw gird to surface
def draw_grid():
    for i in range(Config.COLUMNS):
        pygame.draw.line(window, Color.BLACK, (i*Config.NODE_SIZE,0), (i*Config.NODE_SIZE, Config.WINDOW_HEIGHT), Config.GRID_THICKNESS)
    for i in range(Config.ROWS):
        pygame.draw.line(window, Color.BLACK, (0, i*Config.NODE_SIZE), (Config.WINDOW_WIDTH, i*Config.NODE_SIZE), Config.GRID_THICKNESS)

# create 2d array of nodes
for i in range(Config.COLUMNS):
    for j in range(Config.ROWS):
        nodes[i][j] = Node(i, j)

# change color of start and end
nodes[Config.START_POINT[0]][Config.START_POINT[1]].color = Color.BLUE
nodes[Config.END_POINT[0]][Config.END_POINT[1]].color = Color.BLUE

# change color of barriers
def draw_barriers(data):
    for node in data:
        nodes[node[0]][node[1]].color = Color.BLACK

# main loop
while True:

    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # mouse input
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    # checking nodes
    for i in range(Config.COLUMNS):
        for j in range(Config.ROWS):
            node = nodes[i, j]
            node.draw()

            # collision between mouse and node
            if node.rect.collidepoint(mouse_pos):
                # selecting of node
                if mouse_click[0] == 1:
                    clicked_node.append(node)

                    # make surrounding nodes green
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            neighbor_x = clicked_node[-1].x + i
                            neighbor_y = clicked_node[-1].y + j

                            # checking borders
                            if 0 <= neighbor_x < Config.COLUMNS and 0 <= neighbor_y < Config.ROWS:
                                neighbor_node = nodes[neighbor_x, neighbor_y]

                                # update values
                                if neighbor_node and neighbor_node.color == Color.WHITE:
                                    neighbor_node.update_values(clicked_node[-1].point, clicked_node[-1].g)
                                    neighbor_node.color = Color.GREEN
                                # second update of values
                                elif neighbor_node.color == Color.GREEN and clicked_node[-1].g <= neighbor_node.g - 10:
                                    neighbor_node.update_values(clicked_node[-1].point, clicked_node[-1].g)
                                
                    # clicked node = RED
                    if node.color != Color.BLUE and node.color != Color.BLACK and node.color != Color.RED:
                        clicked_node[-1].color = Color.RED

        # call other functions
        draw_barriers(Config.BARRIERS_POS)
        draw_grid()

    # update display
    pygame.display.flip()
    clock.tick(60)