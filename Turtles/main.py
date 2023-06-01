from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=1280, height=720)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []


def finnish_line():
    line = Turtle("circle")
    line.hideturtle()
    line.speed("fastest")
    line.penup()
    line.width(15)
    line.setheading(270)
    line.goto(x=625, y=360)
    line.pendown()
    while line.ycor() > -360:
        line.forward(100)


finnish_line()
turtle_number = 1
y = -180

for i in colors:
    turtle_name = "turtle" + "turtle_number"
    turtle_name_m = Turtle(shape="turtle")
    turtle_name_m.color(colors[turtle_number - 1])
    turtle_name_m.penup()
    turtle_name_m.goto(x=-590, y=y)
    turtle_number += 1
    y += 70
    turtle_list.append(turtle_name_m)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 575:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!\nThe {winning_color} turtle is the winner!")
            else:
                print(f"You've lost!\nThe {winning_color} turtle is the winner!")

        rand_distance = randint(8, 28)
        turtle.forward(rand_distance)

screen.exitonclick()