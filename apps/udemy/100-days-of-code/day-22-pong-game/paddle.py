from turtle import Turtle

PADDLE_SPEED = 40

class Paddle(Turtle):
    def __init__(self, pos_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.goto(pos_x, 0)

    def move_to_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + PADDLE_SPEED)

    def move_to_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - PADDLE_SPEED)