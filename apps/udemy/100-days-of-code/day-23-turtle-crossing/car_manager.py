from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.generate_new_car()

    def generate_new_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(random.randint(300, 600), random.randint(-180, 200))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move(self, player_level):
        for car in self.cars:
            car.speed(MOVE_INCREMENT * player_level)
            car.forward(STARTING_MOVE_DISTANCE)

