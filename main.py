import pygame
import sys

from modules.color import Color

pygame.init()

window = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

start_point = (0, 0)
end_point = (10, 5)

class Rect:
    def __init__(self, x, y, color=Color.WHITE):
        self.rect = pygame.Rect(x, y, 100, 100)
        self.color = color

        self.point = (x/100, y/100)

        self.g = (start_point[1])
        self.h = ()
        self.f = ()

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

# Create a list of Rect instances
rectangles = [Rect(i*100, j*100) for i in range(10) for j in range(5)]

rectangles[0].color = Color.BLUE
rectangles[49].color = Color.BLUE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(Color.BLACK)

    # Check for collision with mouse cursor
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    for rect in rectangles:
        rect.draw()

        # Check for collision with mouse cursor
        if rect.rect.collidepoint(mouse_pos):
            pygame.draw.rect(window, Color.BLACK, rect.rect, 3)  # Highlight the colliding rectangle
            if mouse_click[0] == 1:
                clicked_rect = rect

                # Update the color of the surrounding rectangles
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        neighbor_x = clicked_rect.rect.x + i * 100
                        neighbor_y = clicked_rect.rect.y + j * 100

                        # Check if the neighbor is within the boundaries
                        if 0 <= neighbor_x < 1000 and 0 <= neighbor_y < 500:
                            neighbor_rect = next(
                                (r for r in rectangles if r.rect.collidepoint((neighbor_x, neighbor_y))),
                                None
                            )
                            if neighbor_rect and neighbor_rect.color == Color.WHITE:
                                neighbor_rect.color = Color.GREEN

                if rect.color != Color.BLUE and rect.color != Color.BLACK:
                    clicked_rect.color = Color.RED

    pygame.display.flip()
    clock.tick(60)

