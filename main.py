# main.py

# imports of modules
from modules.config import Config
from modules.app import App

# imports of libraries
import pygame

# initialize the game
pygame.init()
app = App()

# create the window
window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("A* Pathfinding Algorithm")

# create the clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
running: bool = True

# main loop
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # inputs handling
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    # update and draw the game
    app.update(mouse_click, mouse_pos, keys)
    app.draw(window, font)

    # update the window
    pygame.display.flip()
    clock.tick(60)

pygame.quit()