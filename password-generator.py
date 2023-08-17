import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "*", "(", ")", "+"]

length = int(input("🔒 Welcome to the Password Generator!\nHow long would you like your password to be?\n"))

num_numbers = int(input("How many numbers would you like?\n"))

num_symbols = int(input("How many symbols would you like?\n"))

password = ""

# The for loop executes length - 0 times.
for step in range(0, length):
    random_num = random.randint(0, 2)

    if random_num == 0:
        random_letter = letters[random.randint(0, 25)]
        password += random_letter

    elif random_num == 1:
        if num_numbers > 0:
            random_number = numbers[random.randint(0, 10)]
            password += random_number
            num_numbers -= 1
        else:
            random_letter = letters[random.randint(0, 25)]
            password += random_letter

    else:
        if num_symbols > 0:
            random_number = symbols[random.randint(0, 8)]
            password += random_number
            num_symbols -= 1
        else:
            random_letter = letters[random.randint(0, 25)]
            password += random_letter

print(f"🔑 Here is your new password:\n{password}")
