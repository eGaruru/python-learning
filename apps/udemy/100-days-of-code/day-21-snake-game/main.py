from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Left", fun=lambda: snake.turn("left"))
screen.onkey(key="Right", fun=lambda: snake.turn("right"))
screen.onkey(key="Up", fun=lambda: snake.turn("up"))
screen.onkey(key="Down", fun=lambda: snake.turn("down"))

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()


screen.exitonclick()
