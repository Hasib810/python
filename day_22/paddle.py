from turtle import Turtle

class Paddle(Turtle):  # Correct class name

    def __init__(self, position):  # Fix: Use double underscores
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Fix: "stretch_wid" not "stretch_wid"
        self.penup()
        self.goto(position)

    def go_up(self):  # Add 'self' parameter
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def go_down(self):  # Add 'self' parameter
        y = self.ycor() - 20
        self.goto(self.xcor(), y)