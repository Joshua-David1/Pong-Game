from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hit_count = 0
        self.bounce_speed = choice([-10, 10])
        self.bounce_x, self.bounce_y = self.bounce_speed, choice([-10, -9, -8, -7, 6, 7, 8, 9, 10])
        self.penup()
        self.shape('circle')
        self.shapesize()
        self.color('white')
        self.hit = False
        self.point_wait = 1
        self.ispoint_wait = False

    def move(self):
        x_cor = self.xcor()+self.bounce_x
        y_cor = self.ycor()+self.bounce_y
        self.goto((x_cor, y_cor))

    def wall_collision(self):
        self.bounce_y *= -1

    def paddle_collision(self):
        self.bounce_x *= -1

    def ball_reset(self):
        self.hit_count = 0
        self.bounce_speed = choice([-10, 10])
        self.bounce_x = self.bounce_speed
        self.bounce_y = choice([-10, -9, -8, 6, 7, 8, 9, 10])
        self.goto((0, 0))

