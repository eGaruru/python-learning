# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(229, 228, 226), (224, 222, 224), (199, 175, 117), (125, 36, 24), (169, 105, 56), (187, 158, 51),
              (5, 57, 83), (203, 217, 207), (222, 223, 226), (109, 67, 84), (40, 35, 34), (87, 141, 56),
              (110, 160, 175), (20, 122, 175), (75, 39, 47), (64, 153, 138), (8, 67, 47), (134, 41, 43), (183, 97, 79),
              (179, 201, 186), (206, 200, 136), (150, 176, 162), (174, 160, 164), (214, 183, 173), (35, 76, 60),
              (97, 140, 153), (23, 77, 92), (200, 186, 189), (40, 65, 90), (140, 120, 125)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
