from turtle import Turtle

SCORE_COLOR = "White"
# Determine the font, size and style of the scoreboard
FONTS = ("Arial", 20, "normal")
# Alignment of the scoreboard on the screen
ALIGNMENT = "center"


# Color of the scoreboard

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(-100, 260)
        self.write(f"Score: {self.l_score}", align=ALIGNMENT, font=FONTS)
        self.goto(100, 260)
        self.write(f"Score: {self.r_score}", align=ALIGNMENT, font=FONTS)

    def increase_score_right(self):
        """this function is responsible for incrementing the score
        updating then clearing the previous score"""
        self.r_score += 1
        self.clear()
        self.update()

    def increase_score_left(self):
        """this function is responsible for incrementing the score
        updating then clearing the previous score"""
        self.l_score += 1
        self.clear()
        self.update()

    def game_over(self):
        """Game over function which is called when the user crashes into the wall
        or becomes to long and crashes into itself."""
        # set the position to the top of the screen
        self.setposition(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONTS)