from turtle import Turtle


class GameText(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(-20, 260)
        self.color('White')

    def write_score(self):
        self.write(f'Score: {self.score}', align='center', font=('Courier', 16, 'normal'))

    def game_over(self):
        self.goto(0 ,0)
        self.write('GAME OVER' , align='center', font=('Courier', 16, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()
