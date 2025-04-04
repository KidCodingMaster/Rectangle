import pygame

screen = pygame.display.set_mode((1280, 720))

square = pygame.Rect(200, 200, 50, 50)
rect = pygame.Rect(100, 100, 50, 100)

while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(screen, (255, 0, 0), square)
    pygame.draw.rect(screen, (0, 255, 0), rect)

    pygame.draw.circle(screen, (0, 0, 255), (1280 // 2, 720 // 2), 10)

    pygame.display.update()
