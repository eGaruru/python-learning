from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left = 0
        self.right = 0
        self.color("white")
        self.hideturtle()
        self.penup()

    def display(self):
        self.clear()
        self.goto(0, 240)
        self.write(f"{self.left} : {self.right}", align="center", font=("Arial", 40, "normal"))

    def increment_score(self):
        self.clear()
        self.write(f"{self.left} : {self.right}", align="center", font=("Arial", 40, "normal"))