from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_tup):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(paddle_tup)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)