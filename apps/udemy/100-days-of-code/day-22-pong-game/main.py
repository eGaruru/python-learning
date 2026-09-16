from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player_left = Paddle(-350)
player_right = Paddle(350)

ball = Ball()

score_board = ScoreBoard()
score_board.display()

screen.listen()

screen.onkey(fun=player_left.move_to_up, key="w")
screen.onkey(fun=player_left.move_to_down, key="s")
screen.onkey(fun=player_right.move_to_up, key="Up")
screen.onkey(fun=player_right.move_to_down, key="Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

# Structure
# Paddle
# ball
# Scoreboard
# Paddle == Snake

screen.exitonclick()
