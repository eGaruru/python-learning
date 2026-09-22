from turtle import Turtle
from paddle import Paddle

DIRECTION = 1
BALL_SPEED = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.move_speed_x = BALL_SPEED
        self.move_speed_y = BALL_SPEED
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
            self.move_speed_y = offset * (BALL_SPEED * 0.01)

    def bounce_y(self):
        self.move_speed_y *= -1

    def reset_position(self):
        self.bounce_x(None)
        self.bounce_y()
        self.goto(0,0)

