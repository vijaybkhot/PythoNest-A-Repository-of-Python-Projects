from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("black")
        self.level = 0
        self.goto(-240, 270)
        self.update_scorecard()

    def update_scorecard(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)
