from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Opens the txt file, then closes it to clear up your computer's resources.
        with open("data.txt") as data:
            # Saves the contents of the file in a string that is then converted into an integer.
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Allows the "turtle" to write text in the first parameter, whether the text should move, what alignment it has, and what font style, size, and weight it should have.
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # mode="w" makes the file readable and writable.
            with open("data.txt", mode="w") as data:
                # Replaces all the text in the file with the given text.
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
