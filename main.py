# main.py

import pygame

from modules.config import Config
from modules.app import App

pygame.init()
app = App()

window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
pygame.display.set_caption("PathFinding")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    app.update(mouse_click, mouse_pos, keys)
    app.draw(window, font)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()