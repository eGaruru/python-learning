from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

for i in range(3):
    segment = Turtle()
    segment.color("white")
    segment.shape("square")
    segment.goto(x=(i * 20) * -1, y=0)

screen.exitonclick()
