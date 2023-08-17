import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# pandas can only use images that are .gif file.
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reads the contents of a .csv file.
data = pandas.read_csv("50_states.csv")
# Converts the data into a list.
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    # Executes this if block if you type "Exit" in the text input.
    if answer_state == "Exit":
        # Uses list comprehension get all the states that are in all_states, but not in guessed_states.
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        # Converts the data into a .csv file.
        new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
