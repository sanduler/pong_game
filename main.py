# Name: Ruben Sanduleac
# Date: February 3rd, 2022
# Description: Pong game built with OOP in mind.

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

GAME_TITLE = "Pong"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOUNCE_EDGE = 13
BACKGROUND_COLOR = "Black"

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.movement()
    if ball.ycor() > ((SCREEN_HEIGHT/2) - BOUNCE_EDGE) or ball.ycor() < ((-1 * (SCREEN_HEIGHT / 2)) + BOUNCE_EDGE):
        ball.bounce()

screen.exitonclick()
