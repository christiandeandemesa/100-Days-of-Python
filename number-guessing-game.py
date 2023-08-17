import random

computer_numbers = list(range(1, 100))
computer_choice = random.choice(computer_numbers)

print("🙉 Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def check_difficulty(difficulty):
    if difficulty != "easy" and difficulty != "hard":
        return "easy"
    else:
        return difficulty

checked_difficulty = check_difficulty(difficulty)

if checked_difficulty == "easy":
    attempts = 10
else:
    attempts = 5

def play_game(attempts):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess my number!")
        guess = int(input("Make a guess: "))

        if guess > computer_choice:
            print("Your guess is too high!")
            attempts -= 1
        elif guess < computer_choice:
            print("Your guess is too low!")
            attempts -= 1
        else:
            print("🙈 You guessed my number!")
            return

    print("🙊 You ran out of guesses!")
    return

play_game(attempts)