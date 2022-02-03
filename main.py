# Name: Ruben Sanduleac
# Date: February 3rd, 2022
# Description: Pong game built with OOP in mind.

import random
from turtle import Turtle, Screen

GAME_TITLE = "Pong"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = "Black"


screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)

paddle = Turtle(shape="square")
paddle.color("White")
paddle.resizemode("auto")
paddle.turtlesize(stretch_wid=5, stretch_len=1)

paddle.penup()
paddle.goto((350, 0))


def paddle_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def paddle_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(paddle_up, "Up")
screen.onkey(paddle_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()








screen.exitonclick()