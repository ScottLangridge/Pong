import pygame

from time import sleep
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
        sleep(0.001)


def draw_screen(screen, game_objects):
    screen.fill(BLACK)
    for obj in game_objects.values():
        obj.draw()
    pygame.display.update()


def run_tick(game_objects):
    collisions(game_objects)
    for obj in game_objects.values():
        obj.tick()


def collisions(game_objects):
    ball_x = game_objects["ball"].pos[0]
    ball_y = game_objects["ball"].pos[1]
    pad1_top = game_objects['pad1'].pos[1]
    pad1_bot = game_objects['pad1'].pos[1] + PADDLE_HEIGHT
    pad1_x = game_objects['pad1'].pos[0] + PADDLE_WIDTH
    pad2_top = game_objects['pad2'].pos[1]
    pad2_bot = game_objects['pad2'].pos[1] + PADDLE_HEIGHT
    pad2_x = game_objects['pad2'].pos[0]

    # Score
    if ball_x == SCREEN_SIZE[0]:
        print('P1 Scores')
        game_objects['ball'].set_pos(BALL_START_POS)
        game_objects['ball'].set_vel(BALL_START_VEL)
    elif ball_x == 0:
        print('P2 Scores')
        game_objects['ball'].set_pos(BALL_START_POS)
        game_objects['ball'].set_vel(BALL_START_VEL)

    # Bounce off top/bottom
    if ball_y <= BALL_RADIUS or ball_y >= SCREEN_SIZE[1] - BALL_RADIUS:
        game_objects['ball'].bounce('y')

    # Bounce off paddle
    if ball_x - BALL_RADIUS <= pad1_x and pad1_top <= ball_y <= pad1_bot:
        game_objects['ball'].bounce('x')
    if ball_x + BALL_RADIUS >= pad2_x and pad2_top <= ball_y <= pad2_bot:
        game_objects['ball'].bounce('x')

def initialisation():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    ball = Ball(screen, BALL_START_POS[:], WHITE)
    pad1 = Paddle(screen, [PADDLE_WIDTH, MID_Y], WHITE, pygame.K_s, pygame.K_w)
    pad2 = Paddle(screen, [SCREEN_SIZE[0] - 2 * PADDLE_WIDTH, MID_Y], WHITE, pygame.K_DOWN, pygame.K_UP)
    game_objects = {"ball": ball, "pad1": pad1, "pad2": pad2}
    return screen, game_objects


main()
