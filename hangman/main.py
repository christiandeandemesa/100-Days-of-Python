import random
from hangman_words import word_list
# Imports multiple variables from the hangman_art.py file.
from hangman_art import logo, stages
import os

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
end_of_game = False
lives = 6

# Clears the terminal.
clear = lambda : os.system('tput reset')

for _ in range(word_length):
    display += "_"

print(logo)

# While loop runs until end_of_game is True.
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    # If the guess letter matches any element in the display list, do something.
    if guess in display:
        print(f"You've already guessed the letter {guess}?")

    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            print(f"The letter {guess} is in the word!")
            display[position] = letter

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word...")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("💀 You lose...")

    if "_" not in display:
        end_of_game = True
        print("😁 You win!")

    print(display)
    print(stages[lives])