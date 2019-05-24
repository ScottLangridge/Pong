import pygame

from src.Pong.GameObject import GameObject
from src.Pong.Const import *


class Paddle(GameObject):
    def __init__(self, surface, pos, colour, down_key, up_key):
        GameObject.__init__(self, surface, pos, colour)
        self.vel = PADDLE_VEL
        self.size = [PADDLE_WIDTH, PADDLE_HEIGHT]
        self.up_key = up_key
        self.down_key = down_key

    def draw(self):
        x, y = self.pos[0], self.pos[1]
        w, h = self.size[0], self.size[1]
        pygame.draw.rect(self.surface, self.colour, (x, y, w, h))

    def tick(self):
        keys = pygame.key.get_pressed()

        if keys[self.up_key]:
            self.pos[1] -= self.vel
        if keys[self.down_key]:
            self.pos[1] += self.vel
