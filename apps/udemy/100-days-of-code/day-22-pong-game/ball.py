from turtle import Turtle
from paddle import Paddle

DIRECTION = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.move_speed_x = 15
        self.move_speed_y = 15
        self.penup()
        self.goto(0,0)

    def move(self):
        new_x = self.xcor() + self.move_speed_x
        new_y = self.ycor() + self.move_speed_y
        self.goto(new_x, new_y)

    def bounce_x(self, paddle):
        self.move_speed_x *= -1

        if paddle:
            offset = self.ycor() - paddle.ycor()
            self.move_speed_y = offset * 0.15

    def bounce_y(self):
        self.move_speed_y *= -1

    def reset_position(self):
        self.bounce_x(None)
        self.bounce_y()
        self.goto(0,0)

