import pygame

from src.Objects.GameObject import GameObject
from src.Const import *


class Ball(GameObject):
    def __init__(self, surface, pos, colour):
        GameObject.__init__(self, surface, pos, colour)
        self.vel = BALL_START_VEL[:]
        self.radius = BALL_RADIUS

    def set_pos(self, pos):
        self.pos = pos

    def set_vel(self, vel):
        self.vel = vel

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
