# app.py

import pygame
import numpy as np

from modules.config import Config
from modules.color import Color
from modules.app_state.state import State
from modules.node.node import Node

from modules.background import grid
from modules.app_state.calc import calc
from modules.app_state.result import result
from modules.app_state.planner import planner

class App:
    def __init__(self) -> None:
        self.state = State.PLANNER
        self.nodes = np.empty((Config.COLUMNS, Config.ROWS), dtype=object)
        self.color_value = 0

        self.calc = False
        self.result = False

        for i in range(Config.COLUMNS):
            for j in range(Config.ROWS):
                self.nodes[i][j] = Node(i, j)

    def update(self, mouse_click, mouse_pos, keys) -> None:

        if keys[pygame.K_1]:
            for i in range(Config.COLUMNS):
                for j in range(Config.ROWS):
                    self.nodes[i, j].color = Color.WHITE
            pygame.time.delay(200)

        elif keys[pygame.K_2]:
            self.state = State.CALC
            pygame.time.delay(200)

        elif keys[pygame.K_3]:
            self.state = State.RESULT
            pygame.time.delay(200)
            
        if self.state == State.PLANNER:
            self.color_value = planner(mouse_click, mouse_pos, keys, self.nodes, self.color_value)

        elif self.state == State.CALC:
            if self.calc == False:
                calc(self.nodes[Config.START_POINT[0]][Config.START_POINT[1]], Config.END_POINT, self.nodes)
                self.calc = True

        elif self.state == State.RESULT:
            if not self.result:
                result(self.nodes[Config.END_POINT[0]][Config.END_POINT[1]], Config.START_POINT, self.nodes)
                self.result = True

    def draw(self, surface, font) -> None:
        for i in range(Config.COLUMNS):
            for j in range(Config.ROWS):
                node = self.nodes[i, j]
                node.draw(surface, font)

        for point in Config.BARRIERS_POS:
            self.nodes[point[0]][point[1]].color = Color.BLACK

            self.nodes[Config.END_POINT[0]][Config.END_POINT[1]].color = Color.BLUE
        
        if self.state == State.RESULT:
            self.nodes[Config.START_POINT[0]][Config.START_POINT[1]].color = Color.BLUE
        elif self.state == State.PLANNER or self.state == State.CALC:
            self.nodes[Config.START_POINT[0]][Config.START_POINT[1]].color = Color.YELLOW
        
        grid(surface)