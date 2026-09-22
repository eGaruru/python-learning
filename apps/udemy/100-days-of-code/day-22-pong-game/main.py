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
score_board.display_score()

screen.listen()

screen.onkey(fun=player_left.move_to_up, key="w")
screen.onkey(fun=player_left.move_to_down, key="s")
screen.onkey(fun=player_right.move_to_up, key="Up")
screen.onkey(fun=player_right.move_to_down, key="Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    ball.move()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(player_right) < 50 and ball.xcor() > 330:
        ball.bounce_x(player_right)

    elif ball.distance(player_left) < 50 and ball.xcor() > -330:
        ball.bounce_x(player_left)

    elif ball.distance(player_right) > 50 and ball.xcor() < -380:
        score_board.increase_score_right()
        ball.reset_position()
    elif ball.distance(player_left) > 50 and ball.xcor() > 380:
        score_board.increase_score_left()
        ball.reset_position()

    if score_board.left >= 11 or score_board.right >= 11:
        is_game_on = False
        score_board.display_winner()


# Structure
# Paddle
# ball
# Scoreboard
# Paddle == Snake

screen.exitonclick()
