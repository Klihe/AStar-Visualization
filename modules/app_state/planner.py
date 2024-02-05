# planner.py

# imports of modules
from modules.color import Color
from modules.config import Config

# imports of libraries
import pygame

# Planner class to handle the planner state of the game
class Planner:
    def __init__(self, nodes: list) -> None:
        # colors to draw the nodes
        self.colors = [Color.BLACK, Color.YELLOW, Color.BLUE, Color.WHITE]
        self.choosen_color: int = 0
        self.nodes: list = nodes

        self.node_start: tuple[int] = None
        self.node_end: tuple[int] = None

    # function to draw the nodes
    def drawing(self, mouse_click, mouse_pos) -> None:
        for i in range(Config.COLUMNS):
            for j in range(Config.ROWS):

                # check if the mouse is clicked on the node
                if self.nodes[i][j].rect.collidepoint(mouse_pos):
                    if mouse_click[0] == 1:

                        # if start, end was already choosen, change the color of the previous node
                        if self.choosen_color == 1:
                            if self.node_start is not None:
                                self.nodes[self.node_start[0]][self.node_start[1]].color = Color.WHITE
                            self.node_start = self.nodes[i][j].point
                        elif self.choosen_color == 2:
                            if self.node_end is not None:
                                self.nodes[self.node_end[0]][self.node_end[1]].color = Color.WHITE
                            self.node_end = self.nodes[i][j].point
                            
                        # change the color of the node
                        self.nodes[i][j].color = self.colors[self.choosen_color]

    # function to change the painting color
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
    
    # function to draw the color palette
    def draw(self, surface, mouse_pos):
        image = pygame.image.load("source/colors.png")
        image_2 = pygame.image.load("source/frame.png")
        surface.blit(image, (mouse_pos[0]-25, mouse_pos[1]))
        surface.blit(image_2, (mouse_pos[0]-27, mouse_pos[1]-2+self.choosen_color*10))