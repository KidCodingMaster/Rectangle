import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

rect = pygame.Rect(100, 100, 50, 100)
text = pygame.font.SysFont("cosmicsans", 34).render("Hello", True, (0, 0, 0))

while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(screen, (0, 255, 0), rect)
    screen.blit(text, (1280 // 2, 720 // 2))

    pygame.display.update()
