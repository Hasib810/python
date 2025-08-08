from turtle import Turtle, Screen

bappe = Turtle()
screen = Screen()


def move_forward():
    bappe.forward(22)

screen.listen()
screen.onkey(key = "space", fun = move_forward)
screen.exitonclick()

