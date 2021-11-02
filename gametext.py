from turtle import Turtle


class GameText(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(-20, 280)
        self.color('White')

    def write_score(self):
        self.write(f'Score: {self.score}')

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()
