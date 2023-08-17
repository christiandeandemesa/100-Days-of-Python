from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 9)

@app.route("/")
# Example of displaying styled HTML tags.
def home():
    return "<div style='text-align: center'><h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></div>"

# Example of creating a dynamic route that checks if it is an int.
@app.route("/<int:number>")
def guess_number(number):
    if number < random_num:
        return f"<h1 style='color: red; text-align: center'>{number} is too low!</h1>"
    elif number > random_num:
        return f"<h1 style='color: blue; text-align: center'>{number} is too high!<h1>"
    else:
        return f"<h1 style='color: green; text-align: center'>You guessed the correct number!</h1>"

if __name__ == "__main__":
    # debug=True refreshes the server whenever we make a change.
    app.run(debug=True)