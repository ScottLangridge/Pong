import pygame
from time import sleep

pygame.init()

size = width, height = 500, 500
BLACK = 0, 0, 0
WHITE = 255, 255, 255

bPos = [100, 100]
bVel = [1, 1]

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, bPos, 10)
    pygame.display.update()

    for i in range(2):
        bPos[i] += bVel[i]

    sleep(0.01)
