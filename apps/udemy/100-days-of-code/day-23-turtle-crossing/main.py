import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard(player)

screen.listen()
screen.onkey(player.go_up, "Up")

loop_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move(player.level)
    scoreboard.display_level()

    for car in cars.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.display_game_over()

    loop_counter += 1
    if loop_counter % 6 == 0:
        cars.generate_new_car()

screen.exitonclick()
