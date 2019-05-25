import pygame

from src.Pong.GameObject import GameObject
from src.Pong.Const import *


class Ball(GameObject):
    def __init__(self, surface, pos, colour):
        GameObject.__init__(self, surface, pos, colour)
        self.vel = BALL_START_VEL
        self.radius = BALL_RADIUS
        self.bounce_lock = 10

    def set_pos(self, pos):
        self.pos = pos

    def set_vel(self, vel):
        self.vel = vel

    def draw(self):
        pygame.draw.circle(self.surface, self.colour, self.pos, self.radius)

    def tick(self):
        for i in range(2):
            self.pos[i] += self.vel[i]
        self.bounce_lock -= 1

    def bounce(self, axis):
        if self.bounce_lock > 0:
            return False
        if axis == 'x':
            self.vel[0] = -self.vel[0]
            self.bounce_lock = 5
        elif axis == 'y':
            self.vel[1] = -self.vel[1]
        elif axis == 'xy':
            self.bounce('x')
            self.bounce('y')
            self.bounce_lock = 5
