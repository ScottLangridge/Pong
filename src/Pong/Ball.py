import pygame


class Ball:
    def __init__(self, radius, pos, colour, surface):
        self.radius = radius
        self.vel = [1, 1]
        self.pos = pos
        self.colour = colour
        self.surface = surface

    def draw(self):
        pygame.draw.circle(self.surface, self.colour, self.pos, self.radius)

    def tick(self):
        for i in range(2):
            self.pos[i] += self.vel[i]
