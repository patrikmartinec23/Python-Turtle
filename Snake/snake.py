from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.coordinates = [(0, 0), (-20, 0), (-40, 0)]
        self.squares = []
        self.create_snake()
        self.move_distance = 20
        self.head = self.squares[0]

    def create_snake(self):
        for coordinate in self.coordinates:
            self.add_segment(coordinate)

    def add_segment(self, coordinate):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(coordinate)
        self.squares.append(new_square)

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.head.fd(self.move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

