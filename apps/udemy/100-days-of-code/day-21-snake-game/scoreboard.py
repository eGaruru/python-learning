from turtle import Turtle

INITIAL_POSITION = [0, 0]
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

    def game_over(self):
        self.goto(INITIAL_POSITION[0], INITIAL_POSITION[1])
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display()