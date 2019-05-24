import pygame

from src.Pong.Ball import Ball

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
SCREEN_SIZE = [1200, 800]


def main():
    screen = initialisation()
    ball = Ball(10, [SCREEN_SIZE[0] // 2, 10], WHITE, screen)

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        draw_screen(screen, ball)
        ball.tick()


def draw_screen(screen, ball):
    screen.fill(BLACK)

    # Draw ball
    ball.draw()

    pygame.display.update()


def initialisation():
    pygame.init()
    return pygame.display.set_mode(SCREEN_SIZE)


main()
