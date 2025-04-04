import pygame
import time

screen = pygame.display.set_mode((1280, 720))

COLORS = [(0, 0, 0), (255, 0, 0), (0, 255, 0)]
color_idx = 0

color = COLORS[color_idx]
rect = pygame.Rect(0, 0, 50, 50)

end_time = time.time() + 1

side = 'left'

while True:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         color_idx = color_idx + 1 if color_idx + 1 < len(COLORS) else 0
        #         color = COLORS[color_idx]
        #     if event.key == pygame.K_RIGHT:
        #         color_idx = color_idx - 1 if color_idx - 1 >= 0 else len(COLORS) - 1
        #         color = COLORS[color_idx]

    if side == 'left':
        rect.y += 1

        if rect.bottom > 720:
            side = 'down'
    elif side == 'down':
        rect.x += 1

        if rect.right > 1280:
            side = 'right'
    elif side == 'right':
        rect.y -= 1

        if rect.top < 0:
            side = 'up'
    elif side == 'up':
        rect.x -= 1

        if rect.left < 0:
            side = 'left'

    if time.time() >= end_time:
        color_idx = color_idx - 1 if color_idx - 1 >= 0 else len(COLORS) - 1
        color = COLORS[color_idx]
        end_time = time.time() + 1

    pygame.draw.rect(screen, color, rect)

    pygame.display.update()
