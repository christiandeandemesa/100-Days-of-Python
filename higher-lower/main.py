from higher_lower_art import logo, vs
from game_data import data
import random
import os

clear = lambda : os.system('tput reset')

continue_game = True
score = 0

first_choice = random.choice(data)
second_choice = random.choice(data)

while continue_game:
    first_choice = random.choice(data)
    second_choice = random.choice(data)

    while first_choice == second_choice:
        second_choice = random.choice(data)

    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}\n")
    print(f"Compare A: {first_choice['name']}, {first_choice['description']}, from {first_choice['country']}")
    print(vs)
    print(f"Compare B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")

    guess = input("\nWho has more followers? Type 'A' or 'B': ")

    clear()

    if guess != 'A' and guess != 'B':
        guess = 'A'

    if guess == 'A' and int(first_choice['follower_count']) > int(second_choice['follower_count']):
        score += 1
    elif guess == 'B' and int(first_choice['follower_count']) < int(second_choice['follower_count']):
        score += 1
    else:
        continue_game = False

print(logo)
print(f"Sorry, that's wrong. Final score: {score}")