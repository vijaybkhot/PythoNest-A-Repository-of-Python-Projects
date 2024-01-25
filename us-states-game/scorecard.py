from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.score = 0

    def update_scorecard(self):
        self.score += 1
