from turtle import Turtle

DISPLAY_POSITION = [0, 256]
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(DISPLAY_POSITION[0], DISPLAY_POSITION[1])
        self.score = 0
        self.display()

    def display(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display()