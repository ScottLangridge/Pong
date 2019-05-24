import pygame


class Paddle:
    def __init__(self, size, pos, colour, surface):
        self.size = size
        self.pos = pos
        self.colour = colour
        self.surface = surface

    def draw(self):
        rect = self.size[0] * self.size[1]
        pygame.draw.rect(self.surface, self.colour, rect, self.size[0])
