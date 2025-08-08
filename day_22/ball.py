from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Move the ball in the current direction."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the ball's direction along the y-axis."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the ball's direction along the x-axis and increase speed."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset the ball to the center and reverse its x direction."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()