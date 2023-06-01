from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 17, "bold")
FONT_O = ("Courier", 24, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.write_sb()

    def write_sb(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write_sb()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT_O)
