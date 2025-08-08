from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.goto(-100, 260)
        self.write(self.l_score, align="center", font=("courier", 24, "normal"))
        self.goto(100, 260)
        self.write(self.r_score, align="center", font=("courier", 24, "normal"))
