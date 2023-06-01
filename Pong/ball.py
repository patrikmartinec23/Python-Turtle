from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.coordinate = [10, 10]
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.coordinate[0], self.ycor() + self.coordinate[1])

    def bounce(self):
        self.coordinate[1] *= -1

    def hit(self):
        self.coordinate[0] *= -1
        self.move_speed *= 0.9

    def goal(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.1
        self.hit()
