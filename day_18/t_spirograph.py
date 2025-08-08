from turtle import Turtle, Screen
import turtle as t
import random
bappe = Turtle()
t.colormode(255)

def random_color():
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]
bappe.pensize(2)
bappe.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        bappe.color(random_color())
        bappe.circle(100)
        bappe.setheading(bappe.heading() + size_of_gap)



draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()