# Giving an import an alias name (useful for really long names).
import turtle as t
from turtle import Turtle, Screen
import random

# Sets the colormode to use rgb(0, 0, 0).
t.colormode(255)

turtle = Turtle()
# Sets the shape of the "turtle".
turtle.shape("turtle")
# Sets the speed of the "turtle".
turtle.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # Tuples (r, g, b), unlike lists, are immutable.
    return (r, g, b)

for _ in range(360):
    turtle.color(random_color())
    # Creates a circle with a radius of 100.
    turtle.circle(100)
    # Turns the "turtle" to the right by 1 degree.
    turtle.right(1)

# Generates a new window for our turtle that closes when clicked on.
screen = Screen()
screen.exitonclick()