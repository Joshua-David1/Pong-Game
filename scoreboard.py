from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.score1 = 0
        self.score2 = 0
        self.p1_win = False
        self.p2_win = False

    def display_score(self):
        self.goto((-200, 270))
        self.write(f"Score: {self.score1}", False, align='center',font=("Arial", 15, "normal"))
        self.goto((200, 270))
        self.write(f"Score: {self.score2}", False, align='center',font=("Arial", 15, "normal"))

    def final_result(self):
        if self.p1_win:
            self.goto((0, 0))
            self.write(f"P1 Wins!!", False, align='center',font=("Arial", 25, "normal"))
        elif self.p2_win:
            self.goto((0, 0))
            self.write(f"P2 Wins!!", False, align='center', font=("Arial", 25, "normal"))

    def check_win(self):
        if self.score1 == 7:
            self.p1_win = True
            return True
        elif self.score2 == 7:
            self.p2_win = True
            return True
        return None


class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.setheading(90)
        self.forward(300)
        self.setheading(270)
        self.forward(600)
        self.hideturtle()
