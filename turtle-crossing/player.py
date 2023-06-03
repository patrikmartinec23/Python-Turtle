from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("#006400")
        self.setheading(90)
        self.starting_p()

    def starting_p(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
