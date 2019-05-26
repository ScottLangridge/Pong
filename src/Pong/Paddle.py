import pygame

from src.Pong.GameObject import GameObject
from abc import ABC, abstractmethod
from src.Pong.Const import *


class Paddle(GameObject, ABC):
    def __init__(self, surface, pos, colour):
        GameObject.__init__(self, surface, pos, colour)
        self.vel = PADDLE_VEL
        self.size = [PADDLE_WIDTH, PADDLE_HEIGHT]

    def draw(self):
        x, y = self.pos[0], self.pos[1]
        w, h = self.size[0], self.size[1]
        pygame.draw.rect(self.surface, self.colour, (x, y, w, h))

    @abstractmethod
    def tick(self):
        pass

    def move_up(self):
        if self.pos[1] - self.vel < 0:
            self.pos[1] = 0
        else:
            self.pos[1] -= self.vel

    def move_down(self):
        if self.pos[1] + self.vel > SCREEN_SIZE[1] - PADDLE_HEIGHT:
            self.pos[1] = SCREEN_SIZE[1] - PADDLE_HEIGHT
        else:
            self.pos[1] += self.vel
