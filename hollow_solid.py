import pygame

screen = pygame.display.set_mode((1280, 720))

RADIUS = 100

while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.circle(screen, (0, 0, 255), (1280 // 2, 720 // 2), RADIUS)
    pygame.draw.circle(screen, (0, 0, 255), (150, 150), RADIUS, 3)

    pygame.display.update()
