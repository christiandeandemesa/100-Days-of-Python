from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()

def move_forward():
    arrow.forward(10)

def move_backward():
    # Moves the arrow backwards 100 pixels.
    arrow.backward(10)

def turn_counter_clockwise():
    arrow.left(10)

def turn_clockwise():
    arrow.right(10)

def clear():
    # Clears all the lines the arrow drew.
    arrow.clear()
    arrow.penup()
    # Returns the arrow to its initial position.
    arrow.home()
    arrow.pendown()

# Gives the screen an event listener.
screen.listen()

# When the w key is pressed, execute the given function within our higher order function (i.e. a function that takes a function as an input).
# If move_forward was in parentheses, it would execute the function immediately without the key needing to be pressed.
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()