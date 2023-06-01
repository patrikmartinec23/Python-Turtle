import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#212427")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.draw_a_line()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit()

    # Detect if the left scores
    if ball.xcor() > 390:
        ball.goal()
        scoreboard.l_point()

    # Detect if the right scores
    if ball.xcor() < -390:
        ball.goal()
        scoreboard.r_point()

screen.exitonclick()
