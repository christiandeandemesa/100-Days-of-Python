from turtle import Turtle
import random

# The Food class inherits from the Turtle class.
class Food(Turtle):
    def __init__(self):
        # Inherits all the attributes and methods from its super class (e.g. Animal).
        super().__init__()
        self.shape("circle")
        self.penup()
        # Stretches the "turtle" along its length and width
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
