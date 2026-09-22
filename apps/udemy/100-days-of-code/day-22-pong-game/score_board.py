from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left = 0
        self.right = 0
        self.color("white")
        self.hideturtle()
        self.penup()

    def display_score(self):
        self.clear()
        self.goto(0, 240)
        self.write(f"{self.left} : {self.right}", align="center", font=("Arial", 40, "normal"))

    def display_winner(self):
        self.display_score()
        self.goto(0, 0)
        if self.left == 11:
            winner = "Player 1"
        else:
            winner = "Player 2"
        self.write(f"{winner} WIN!", align="center", font=("Arial", 40, "normal"))

    def increase_score_left(self):
        self.left += 1
        self.display_score()

    def increase_score_right(self):
        self.right += 1
        self.display_score()