from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.hideturtle()
        self.goto(-280,250)
        self.player = player
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.player.level}", align="left", font=FONT)

    def display_game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER", align="center", font=FONT)