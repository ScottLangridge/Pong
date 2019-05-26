from abc import ABC, abstractmethod


class GameObject(ABC):
    def __init__(self, surface, pos, colour):
        self.surface = surface
        self.pos = pos
        self.colour = colour

    @abstractmethod
    def draw(self):
        pass

    def tick(self):
        for i in range(2):
            self.pos[i] += self.vel[i]
