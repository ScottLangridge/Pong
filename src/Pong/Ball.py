import pygame

from src.Pong.GameObject import GameObject


class Ball(GameObject):
    def __init__(self, surface, radius, pos, colour, vel=[0, 0]):
        GameObject.__init__(self, surface, pos, colour, vel)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.surface, self.colour, self.pos, self.radius)
