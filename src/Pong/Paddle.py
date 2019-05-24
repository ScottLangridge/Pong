import pygame

from src.Pong.GameObject import GameObject


class Paddle(GameObject):
    def __init__(self, surface, size, pos, colour):
        GameObject.__init__(self, surface, pos, colour)
        self.size = size

    def draw(self):
        x, y = self.pos[0], self.pos[1]
        w, h = self.size[0], self.size[1]
        pygame.draw.rect(self.surface, self.colour, (x, y, w, h))

    def tick(self):
        pass
