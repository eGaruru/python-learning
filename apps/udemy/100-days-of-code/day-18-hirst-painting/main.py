# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# color_palette = []
# def get_rgb(rgb):
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#
#     return r, g, b
#
# for color in colors:
#     color_palette.append(get_rgb(color.rgb))
#
# print(color_palette)

import random
import turtle as t

color_palette = [(229, 228, 226), (224, 222, 224), (199, 175, 117), (125, 36, 24), (169, 105, 56), (187, 158, 51),
                 (5, 57, 83), (203, 217, 207), (222, 223, 226), (109, 67, 84), (40, 35, 34), (87, 141, 56),
                 (110, 160, 175), (20, 122, 175), (75, 39, 47), (64, 153, 138), (8, 67, 47), (134, 41, 43),
                 (183, 97, 79), (179, 201, 186), (206, 200, 136), (150, 176, 162), (174, 160, 164), (214, 183, 173),
                 (35, 76, 60), (97, 140, 153), (23, 77, 92), (200, 186, 189), (40, 65, 90), (140, 120, 125)]

t.colormode(255)
brush = t.Turtle()
brush.hideturtle()
brush.penup()

num_of_column = 10
num_of_row = 10

for i in range(num_of_row):
    x = -300
    y = i * 50 - 150
    brush.setpos(x, y)

    for _ in range(num_of_column):
        brush.forward(50)
        brush.dot(20, random.choice(color_palette))

screen = t.Screen()
screen.exitonclick()
