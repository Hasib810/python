from turtle import Turtle, Screen
import turtle as t
import random
bappe = Turtle()


colors = ["red", "blue", "cyan", "yellow", "orange", "skyblue"]


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        bappe.forward(100)
        bappe.right(angle)



for shape_side_n in range(3, 11):
    bappe.color(random.choice(colors))
    draw_shapes(shape_side_n)
