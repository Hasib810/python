from turtle import Turtle, Screen
import turtle as t
import random
bappe = Turtle()


colors = ["red", "blue", "cyan", "yellow", "orange", "skyblue", "seagreen"]


directions = [0, 90, 180, 270]
bappe.pensize(20)
bappe.speed("fastest")


for _ in range(200):
    bappe.color(random.choice(colors))
    bappe.forward(25)
    bappe.setheading(random.choice(directions))