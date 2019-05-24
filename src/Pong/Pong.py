import pygame

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]


def main():
    screen = initialisation()

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        draw_screen(screen)


def draw_screen(screen):
    screen.fill(BLACK)
    pygame.display.update()


def initialisation():
    pygame.init()
    size = 1000, 800
    return pygame.display.set_mode(size)


main()
