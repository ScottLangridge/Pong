import pygame

from src.Pong.GameObject import GameObject
from src.Pong.Const import *


class Ball(GameObject):
    def __init__(self, surface, pos, colour):
        GameObject.__init__(self, surface, pos, colour)
        self.vel = BALL_VEL
        self.radius = BALL_RADIUS

    def draw(self):
        pygame.draw.circle(self.surface, self.colour, self.pos, self.radius)

    def bounce(self, axis):
        if axis == 'x':
            self.vel[0] = -self.vel[0]
        elif axis == 'y':
            self.vel[1] = -self.vel[1]
        elif axis == 'xy':
            self.bounce('x')
            self.bounce('y')
