from turtle import Turtle, Screen
import turtle as t
import random
bappe = Turtle()
t.colormode(255)

def random_color():
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
bappe.pensize(20)
bappe.speed("fastest")


for _ in range(200):
    bappe.color(random_color())
    bappe.forward(25)
    bappe.setheading(random.choice(directions))