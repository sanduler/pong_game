from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.movement()

    def movement(self):
        new_x = self.xcor() + 2
        new_y = self.ycor() + 2
        self.goto(new_x, new_y)