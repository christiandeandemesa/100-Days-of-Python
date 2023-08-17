# Installed the python package using: pip install colorgram.py from https://pypi.org/project/colorgram.py/.
import colorgram
import turtle
import random

turtle.colormode(255)

# Extracts 30 colors from the given image.
colors = colorgram.extract('image.jpg', 30)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

arrow = turtle.Turtle()

arrow.speed(0)
# Removes the drawn line following the "turtle".
arrow.penup()
# Makes the "turtle" invisible.
arrow.hideturtle()

# Sets the "turtle's" heading in degrees.
arrow.setheading(225)
# The "turtle" moves 250 pixels.
arrow.forward(250)
arrow.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    arrow.dot(20, random.choice(rgb_colors))
    arrow.forward(50)

    if dot_count % 10 == 0:
        arrow.setheading(90)
        arrow.forward(50)
        arrow.setheading(180)
        arrow.forward(500)
        arrow.setheading(0)

screen = turtle.Screen()
screen.exitonclick()