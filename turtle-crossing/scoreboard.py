from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("#212427")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.goto(x=-280, y=250)
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self, x, y):
        self.goto(x, y)

        # Add background color
        self.color("#a9a9aa")
        self.begin_fill()
        self.goto(x + 75, y + 30)
        self.goto(x + 75, y)
        self.goto(x - 80, y)
        self.goto(x - 80, y + 30)
        self.goto(x + 75, y + 30)
        self.end_fill()

        self.color("#212427")  # Reset the color back to the original

        self.goto(x, y)  # Reset position for writing text
        self.write(f"Game Over!", align="center", font=FONT)


