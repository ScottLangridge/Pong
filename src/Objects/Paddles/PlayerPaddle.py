import pygame

from src.Objects.Paddles.Paddle import Paddle


class PlayerPaddle(Paddle):
    def __init__(self, surface, pos, colour, down_key, up_key):
        Paddle.__init__(self, surface, pos, colour)
        self.down_key = down_key
        self.up_key = up_key

    def tick(self):
        keys = pygame.key.get_pressed()

        if keys[self.up_key]:
            self.move_up()

        if keys[self.down_key]:
            self.move_down()
