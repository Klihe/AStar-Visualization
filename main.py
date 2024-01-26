import pygame
import sys
import math

from modules.color import Color
from modules.config import Config

pygame.init()

window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

class Rect:
    def __init__(self, x, y, color=Color.WHITE):
        self.rect = pygame.Rect(x, y, Config.RECT_SIZE, Config.RECT_SIZE)
        self.color = color

        self.point = (x/Config.RECT_SIZE, y/Config.RECT_SIZE)

        self.g = math.sqrt((Config.START_POINT[0] - self.point[0])**2 + (Config.START_POINT[1] - self.point[1])**2) * 10
        self.h = math.sqrt((Config.END_POINT[0] - self.point[0])**2 + (Config.END_POINT[1] - self.point[1])**2) * 10
        self.f = self.g + self.h

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)
        if self.color == Color.GREEN or self.color == Color.RED:
            text_g = font.render(f"{round(self.g)}", None, Color.BLACK)
            text_h = font.render(f"{round(self.h)}", None, Color.BLACK)
            text_f = font.render(f"{round(self.f)}", None, Color.BLACK)
            window.blit(text_g, (self.rect.x + Config.RECT_SIZE/20, self.rect.y + Config.RECT_SIZE/20))
            window.blit(text_h, (self.rect.x + Config.RECT_SIZE/2, self.rect.y + Config.RECT_SIZE/20))
            window.blit(text_f, (self.rect.x + Config.RECT_SIZE/3, self.rect.y + Config.RECT_SIZE/2))

def drawGrid():
    for i in range(Config.COLUMNS):
        pygame.draw.line(window, Color.BLACK, (i*Config.RECT_SIZE,0), (i*Config.RECT_SIZE, Config.WINDOW_HEIGHT), Config.GRID_THICKNESS)
    for i in range(Config.ROWS):
        pygame.draw.line(window, Color.BLACK, (0, i*Config.RECT_SIZE), (Config.WINDOW_WIDTH, i*Config.RECT_SIZE), Config.GRID_THICKNESS)

rectangles = [Rect(i*Config.RECT_SIZE, j*Config.RECT_SIZE) for i in range(Config.COLUMNS) for j in range(Config.ROWS)]

rectangles[Config.ROWS*Config.START_POINT[0]+Config.START_POINT[1]].color = Color.BLUE
rectangles[Config.ROWS*Config.END_POINT[0]+Config.END_POINT[1]].color = Color.BLUE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(Color.BLACK)

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    for rect in rectangles:
        rect.draw()

        if rect.rect.collidepoint(mouse_pos):
            if mouse_click[0] == 1:
                clicked_rect = rect

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        neighbor_x = clicked_rect.rect.x + i * Config.RECT_SIZE
                        neighbor_y = clicked_rect.rect.y + j * Config.RECT_SIZE

                        if 0 <= neighbor_x < Config.WINDOW_WIDTH and 0 <= neighbor_y < Config.WINDOW_HEIGHT:
                            neighbor_rect = next(
                                (r for r in rectangles if r.rect.collidepoint((neighbor_x, neighbor_y))),
                                None
                            )
                            if neighbor_rect and neighbor_rect.color == Color.WHITE:
                                neighbor_rect.color = Color.GREEN

                if rect.color != Color.BLUE and rect.color != Color.BLACK:
                    clicked_rect.color = Color.RED

        drawGrid()

    pygame.display.flip()
    clock.tick(60)

