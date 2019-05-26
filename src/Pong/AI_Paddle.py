from src.Pong.Paddle import Paddle
from src.Pong.Const import *


class AIPaddle(Paddle):
    def __init__(self, surface, pos, colour, ball):
        Paddle.__init__(self, surface, pos, colour,)
        self.ball = ball

    def tick(self):
        b = self.ball

        # Don't move if not on your half of screen
        if (self.pos[0] <= MID_X) != (b.pos[0] <= MID_X):
            return

        if b.pos[1] < self.pos[1] + PADDLE_HEIGHT / 2:
            self.move_up()
        if b.pos[1] > self.pos[1] + PADDLE_HEIGHT / 2:
            self.move_down()
