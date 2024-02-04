import pygame

win = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()

choose_color = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    
    if keys[pygame.K_LEFT] and choose_color < 30:
        choose_color += 10
        pygame.time.delay(100)
    elif keys[pygame.K_RIGHT] and choose_color > 0:
        choose_color -= 10
        pygame.time.delay(100)

    win.fill((255,255,255))
    image = pygame.image.load("source/colors.png")
    image_2 = pygame.image.load("source/frame.png")
    win.blit(image, (mouse_pos[0]-25, mouse_pos[1]))
    win.blit(image_2, (mouse_pos[0]-27, mouse_pos[1]-2+choose_color))

    clock.tick(60)
    pygame.display.flip()

pygame.QUIT()