from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.draw_a_line()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Futura", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Futura", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()

    def draw_a_line(self):
        self.goto(0, 300)
        while self.ycor() > -300:
            self.pendown()
            self.goto(self.xcor(), self.ycor() - 10)
            self.penup()
            self.goto(self.xcor(), self.ycor() - 10)
