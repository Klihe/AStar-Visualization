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
from modules.app_state.get_plan import get_plan

class App:
    def __init__(self) -> None:
        self.state = State.PLANNER
        self.nodes = np.empty((Config.COLUMNS, Config.ROWS), dtype=object)
        self.color_value = 0

        self.barriers = []
        self.start = None
        self.end = None

        self.calc = False
        self.result = False

        for i in range(Config.COLUMNS):
            for j in range(Config.ROWS):
                self.nodes[i][j] = Node(i, j, self.start, self.end)

    def update(self, mouse_click, mouse_pos, keys) -> None:

        if keys[pygame.K_1]:
            for i in range(Config.COLUMNS):
                for j in range(Config.ROWS):
                    self.nodes[i, j].color = Color.WHITE
            self.calc = False
            self.state = State.PLANNER
            pygame.time.delay(200)

        elif keys[pygame.K_2]:
            self.barriers, self.start, self.end = get_plan(self.nodes)
            for i in range(Config.COLUMNS):
                for j in range(Config.ROWS):
                    self.nodes[i, j].node_start = self.start
                    self.nodes[i, j].node_end = self.end
            self.result = False
            self.state = State.CALC
            pygame.time.delay(200)

        elif keys[pygame.K_3]:
            self.state = State.RESULT
            pygame.time.delay(200)
            
        if self.state == State.PLANNER:
            self.color_value = planner(mouse_click, mouse_pos, keys, self.nodes, self.color_value)

        elif self.state == State.CALC:
            if self.calc == False:
                calc(self.nodes[self.start[0]][self.start[1]], self.end, self.nodes)
                self.calc = True

        elif self.state == State.RESULT:
            if not self.result:
                result(self.nodes[self.end[0]][self.end[1]], self.start, self.nodes)
                self.result = True

    def draw(self, surface, font) -> None:
        for i in range(Config.COLUMNS):
            for j in range(Config.ROWS):
                node = self.nodes[i, j]
                node.draw(surface, font)


        if self.start and self.end:
            for point in self.barriers:
                self.nodes[point[0]][point[1]].color = Color.BLACK

                self.nodes[self.end[0]][self.end[1]].color = Color.BLUE
            
            if self.state == State.RESULT:
                self.nodes[self.start[0]][self.start[1]].color = Color.BLUE
            elif self.state == State.PLANNER or self.state == State.CALC:
                self.nodes[self.start[0]][self.start[1]].color = Color.YELLOW
    
        grid(surface)