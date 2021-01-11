from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.goto(pos)
        self.is_collided = False
        self.safe_count = 1

    def move_up(self):
        if self.ycor() < 250:
            y_cor = self.ycor()+30
            self.goto((self.pos[0], y_cor))

    def move_down(self):
        if self.ycor() > -250:
            y_cor = self.ycor() - 30
            self.goto((self.pos[0], y_cor))
