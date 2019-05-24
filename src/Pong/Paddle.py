import pygame

from src.Pong.GameObject import GameObject


class Paddle(GameObject):
    def __init__(self, surface, size, pos, colour, up_key, down_key, vel):
        GameObject.__init__(self, surface, pos, colour)
        self.vel = vel
        self.size = size
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
