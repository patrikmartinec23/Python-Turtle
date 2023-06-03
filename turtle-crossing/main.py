import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.spawn()
    car_manager.move()

    # Detect if turtle is at the top
    if player.ycor() > 280:
        player.starting_p()
        scoreboard.update()
        car_manager.increase_speed()

    # Detect if turtle crash with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over(player.xcor(), player.ycor())
            game_is_on = False

screen.exitonclick()
