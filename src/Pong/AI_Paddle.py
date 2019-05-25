import pygame

from src.Pong.Paddle import Paddle
from src.Pong.Const import *


class AIPaddle(Paddle):
    def __init__(self, surface, pos, colour, ball):
        Paddle.__init__(self, surface, pos, colour, pygame.K_UP, pygame.K_DOWN)
        self.ball = ball

    def draw(self):
        x, y = self.pos[0], self.pos[1]
        w, h = self.size[0], self.size[1]
        pygame.draw.rect(self.surface, self.colour, (x, y, w, h))

    def tick(self):
        b = self.ball

        if (self.pos[0] <= MID_X) != (b.pos[0] <= MID_X):
            return

        if b.pos[1] < self.pos[1] + PADDLE_HEIGHT / 2:
            if self.pos[1] - self.vel < 0:
                self.pos[1] = 0
            else:
                self.pos[1] -= self.vel

        if b.pos[1] > self.pos[1] + PADDLE_HEIGHT / 2:
            if self.pos[1] + self.vel > SCREEN_SIZE[1] - PADDLE_HEIGHT:
                self.pos[1] = SCREEN_SIZE[1] - PADDLE_HEIGHT
            else:
                self.pos[1] += self.vel
