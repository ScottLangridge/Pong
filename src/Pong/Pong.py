import pygame

from src.Pong.Ball import Ball
from src.Pong.Paddle import Paddle
from src.Pong.Const import *


def main():
    screen, game_objects = initialisation()

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        draw_screen(screen, game_objects)
        run_tick(game_objects)


def draw_screen(screen, game_objects):
    screen.fill(BLACK)
    for obj in game_objects.values():
        obj.draw()
    pygame.display.update()


def run_tick(game_objects):
    for obj in game_objects.values():
        obj.tick()


def initialisation():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    ball = Ball(screen, [MID_X, BALL_RADIUS], WHITE)
    pad1 = Paddle(screen, [PADDLE_WIDTH, MID_Y], WHITE, pygame.K_s, pygame.K_w)
    pad2 = Paddle(screen, [SCREEN_SIZE[0] - 2 * PADDLE_WIDTH, MID_Y], WHITE, pygame.K_DOWN, pygame.K_UP)
    game_objects = {"ball": ball, "pad1": pad1, "pad2": pad2}
    return screen, game_objects


main()
