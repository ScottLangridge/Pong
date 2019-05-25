import pygame

from time import sleep
from src.Pong.Ball import Ball
from src.Pong.Paddle import Paddle
from src.Pong.Const import *


def main():
    screen = initialisation()
    while True:
        print(rally(screen))


def rally(screen):
    ball = Ball(screen, BALL_START_POS[:], WHITE)
    pad1 = Paddle(screen, [PADDLE_WIDTH, MID_Y - int(PADDLE_HEIGHT / 2)], WHITE, pygame.K_s, pygame.K_w)
    pad2 = Paddle(screen, [SCREEN_SIZE[0] - 2 * PADDLE_WIDTH, MID_Y - int(PADDLE_HEIGHT / 2)],
                  WHITE, pygame.K_DOWN, pygame.K_UP)
    game_objects = {"ball": ball, "pad1": pad1, "pad2": pad2}
    scored = 0

    while scored == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        draw_screen(screen, game_objects)
        scored = run_tick(game_objects)
        sleep(SLEEP)

    return scored


def draw_screen(screen, game_objects):
    screen.fill(BLACK)
    for obj in game_objects.values():
        obj.draw()
    pygame.display.update()


def run_tick(game_objects):
    scored = collisions(game_objects)
    for obj in game_objects.values():
        obj.tick()
    return scored


def collisions(game_objects):
    ball_x = game_objects["ball"].pos[0]
    ball_y = game_objects["ball"].pos[1]
    ball_vel_x = game_objects["ball"].vel[0]
    pad1_top = game_objects['pad1'].pos[1]
    pad1_bot = game_objects['pad1'].pos[1] + PADDLE_HEIGHT
    pad1_x = game_objects['pad1'].pos[0] + PADDLE_WIDTH
    pad2_top = game_objects['pad2'].pos[1]
    pad2_bot = game_objects['pad2'].pos[1] + PADDLE_HEIGHT
    pad2_x = game_objects['pad2'].pos[0]

    # Score
    if ball_x == SCREEN_SIZE[0]:
        # Indicate p1 scores
        return 1
    elif ball_x == 0:
        # Indicate p2 scores
        return 2

    # Bounce off top/bottom
    if ball_y <= BALL_RADIUS or ball_y >= SCREEN_SIZE[1] - BALL_RADIUS:
        game_objects['ball'].bounce('y')

    # Bounce off paddle
    i = PADDLE_HEIGHT / 5
    if ball_x - BALL_RADIUS <= pad1_x - ball_vel_x - 1 and pad1_top <= ball_y <= pad1_bot:
        game_objects['ball'].bounce('x')
        if pad1_top <= ball_y <= pad1_top + i:
            game_objects['ball'].vel[1] = -5
        elif pad1_top + i <= ball_y <= pad1_top + 2 * i:
            game_objects['ball'].vel[1] = -2
        elif pad1_top + 2 * i <= ball_y <= pad1_top + 3 * i:
            game_objects['ball'].vel[1] = 0
        elif pad1_top + 3 * i <= ball_y <= pad1_top + 4 * i:
            game_objects['ball'].vel[1] = 2
        elif pad1_top + 4 * i <= ball_y <= pad1_bot:
            game_objects['ball'].vel[1] = 5

    elif ball_x + BALL_RADIUS >= pad2_x - ball_vel_x + 1 and pad2_top <= ball_y <= pad2_bot:
        game_objects['ball'].bounce('x')
        if pad2_top <= ball_y <= pad2_top + i:
            game_objects['ball'].vel[1] = -5
        elif pad2_top + i <= ball_y <= pad2_top + 2 * i:
            game_objects['ball'].vel[1] = -2
        elif pad2_top + 2 * i <= ball_y <= pad2_top + 3 * i:
            game_objects['ball'].vel[1] = 0
        elif pad2_top + 3 * i <= ball_y <= pad2_top + 4 * i:
            game_objects['ball'].vel[1] = 2
        elif pad2_top + 4 * i <= ball_y <= pad2_bot:
            game_objects['ball'].vel[1] = 5

    # Indicate no score
    return 0


def initialisation():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    return screen


main()
