from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.segments  = []

    def create_paddle(self):
        for i in range(4):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(-380, 300 - (i * 10))
            self.segments.append(segment)

        self.segments = []

    def move(self):
        self.forward()