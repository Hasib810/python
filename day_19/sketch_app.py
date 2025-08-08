from turtle import Turtle, Screen

bappe = Turtle()
screen = Screen()


def move_forward():
    bappe.forward(10)

def move_backward():
    bappe.backward(10)

def turn_left():
    new_heading = bappe.heading() + 10
    bappe.setheading(new_heading)

def turn_right():
    new_heading = bappe.heading() - 10
    bappe.setheading(new_heading)


def clear():
    bappe.clear()
    bappe.penup()
    bappe.home()
    bappe.pendown()  

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
clear()
screen.exitonclick()

