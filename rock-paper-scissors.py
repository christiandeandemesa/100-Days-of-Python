import random

choices = ["🪨", "📰", "✂️"]

# Randomly creates an integer from 0 to 2.
computer_choice = random.randint(0, 2)

user_choice = int(input('What do you choose? Type 0 for 🪨, 1 for 📰, or 2 for ✂️\n'))

if user_choice == 0:
    if computer_choice == 0:
        print(f"{choices[computer_choice]}  ties with {choices[user_choice]}\nIT'S A DRAW")
    elif computer_choice == 1:
        print(f"{choices[computer_choice]}  beats {choices[user_choice]}\nYOU LOSE")
    else:
        print(f"{choices[computer_choice]}  loses to {choices[user_choice]}\nYOU WIN")

elif user_choice == 1: 
    if computer_choice == 0:
        print(f"{choices[computer_choice]}  loses to {choices[user_choice]}\nYOU WIN")
    elif computer_choice == 1:
        print(f"{choices[computer_choice]}  ties with {choices[user_choice]}\nIT'S A DRAW")
    else:
        print(f"{choices[computer_choice]}  beats {choices[user_choice]}\nYOU LOSE")

elif user_choice == 2:
    if computer_choice == 0:
        print(f"{choices[computer_choice]}  beats {choices[user_choice]}\nYOU LOSE")
    elif computer_choice == 1:
        print(f"{choices[computer_choice]}  loses to {choices[user_choice]}\nYOU WIN")
    else:
        print(f"{choices[computer_choice]}  ties with {choices[user_choice]}\nIT'S A DRAW")
        
else:
    print('Please choose 0, 1, or 2 to play the game!')