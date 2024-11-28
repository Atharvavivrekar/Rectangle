import pgzrun
import random

title = "Bouncing ball"

WIDTH = 600
HEIGHT = 800

class Ball:
    def _init_(self, initial_x,initial_y):
        self.x = inital_x
        self.y = initial_y
        self.radius = 40
        self.vx = 200
        self.vy = 0
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)

ball = Ball(50,100)
