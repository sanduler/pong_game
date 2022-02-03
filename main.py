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

right_paddle = Turtle(shape="square")
right_paddle.color("White")
right_paddle.resizemode("auto")
right_paddle.turtlesize(stretch_wid=5, stretch_len=1)

right_paddle.penup()
right_paddle.goto((350, 0))


def paddle_up():
    new_y = right_paddle.ycor() + 20
    right_paddle.goto(right_paddle.xcor(), new_y)

def paddle_down():
    new_y = right_paddle.ycor() - 20
    right_paddle.goto(right_paddle.xcor(), new_y)

screen.listen()
screen.onkey(paddle_up, "Up")
screen.onkey(paddle_down, "Down")













screen.exitonclick()