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

# ball.ball_x_cor = 0
# ball.ball_y_cor = 0
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.movement()
    # if screen.update():
        # ball.settiltangle(45)
        # ball_x_cor = ball.xcor() + 10
        # ball_y_cor = ball.ycor() + 10


screen.exitonclick()
