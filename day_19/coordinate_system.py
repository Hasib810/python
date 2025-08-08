from turtle import Turtle, Screen

screen = Screen()
screen.setup(width= 500, height= 500)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "yellow", "green", "orange", "pink", "cyan"]
y_positions = [-100, -60, -20, 20, 60, 100, 140]


for turtle_index in range(0, 7):
    bappe = Turtle(shape = "turtle")
    bappe.color(colors[turtle_index])
    bappe.penup()
    bappe.goto(x = -230, y = y_positions[turtle_index])
    




screen.exitonclick()