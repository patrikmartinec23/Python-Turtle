from turtle import Turtle
from random import randint, choice

COLORS = ["#ff3300", "#990000", "#e6e600", "#212427", "#009933", "#1a1aff", "#333333"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def spawn(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

