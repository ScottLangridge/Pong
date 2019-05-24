import pygame

from src.Pong.Ball import Ball
from src.Pong.Paddle import Paddle

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
SCREEN_SIZE = [1200, 800]


def main():
    screen, game_objects = initialisation()

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        draw_screen(screen, game_objects)


def draw_screen(screen, game_objects):
    screen.fill(BLACK)
    for obj in game_objects:
        obj.draw()
    pygame.display.update()


def initialisation():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    ball = Ball(screen, 10, [SCREEN_SIZE[0] // 2, 10], WHITE, [1, 1])
    pad1 = Paddle(screen, [10, 50], [10, SCREEN_SIZE[1] // 2], WHITE)
    pad2 = Paddle(screen, [10, 50], [SCREEN_SIZE[0] - 20, SCREEN_SIZE[1] // 2], WHITE)
    game_objects = [ball, pad1, pad2]
    return screen, game_objects


main()
