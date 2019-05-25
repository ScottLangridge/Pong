import pygame

from time import sleep
from src.Pong.Ball import Ball
from src.Pong.Paddle import Paddle
from src.Pong.AI_Paddle import AIPaddle
from src.Pong.Const import *


def main():
    screen = initialisation()
    while True:
        print(rally(screen))


def rally(screen):
    ball = Ball(screen, BALL_START_POS[:], WHITE)
    pad1 = AIPaddle(screen, [PADDLE_WIDTH, MID_Y - int(PADDLE_HEIGHT / 2)], WHITE, ball)
    pad2 = AIPaddle(screen, [SCREEN_SIZE[0] - 2 * PADDLE_WIDTH, MID_Y - int(PADDLE_HEIGHT / 2)],
                  WHITE, ball)
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
    draw_centre_line(screen)
    for obj in game_objects.values():
        obj.draw()
    pygame.display.update()


def draw_centre_line(screen):
    i = 0
    while i <= SCREEN_SIZE[1]:
        pygame.draw.rect(screen, WHITE, (MID_X, i, 8, 32))
        i += 64


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
    if ball_x - BALL_RADIUS <= pad1_x - ball_vel_x - PADDLE_WIDTH and pad1_top <= ball_y <= pad1_bot:
        game_objects['ball'].bounce('x')
        game_objects['ball'].vel[1] = get_bounce_angle(game_objects['ball'], game_objects['pad1'])

    elif ball_x + BALL_RADIUS >= pad2_x - ball_vel_x + PADDLE_WIDTH and pad2_top <= ball_y <= pad2_bot:
        game_objects['ball'].bounce('x')
        game_objects['ball'].vel[1] = get_bounce_angle(game_objects['ball'], game_objects['pad2'])

    # Indicate no score
    return 0


def get_bounce_angle(ball, paddle):
    z_width = PADDLE_HEIGHT / 11
    zone_start = paddle.pos[1]
    zone_end = paddle.pos[1] + z_width
    ball_pos = ball.pos[1]

    for i in range(-5, 6):
        if zone_start <= ball_pos <= zone_end:
            return i
        zone_start += z_width
        zone_end += z_width

def initialisation():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    return screen


main()
