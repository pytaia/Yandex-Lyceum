import pygame
from random import randrange

pygame.init()
pygame.display.set_caption('Git и случайные окружности')
screen = pygame.display.set_mode((720, 720))

width, height = screen.get_width(), screen.get_height()

screen.fill((0, 0, 0))

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.draw.circle(screen, pygame.Color((randrange(255), randrange(255), randrange(255))),
                                   (randrange(720), randrange(720)), randrange(500), 1)
                pygame.display.update()

    mouse = pygame.mouse.get_pos()

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, (170, 170, 170), [width / 2 - 70, height / 2 - 20, 140, 40])
    else:
        pygame.draw.rect(screen, (100, 100, 100), [width / 2 - 70, height / 2 - 20, 140, 40])

    pygame.display.update()
