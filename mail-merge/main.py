PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    # Returns a list where each line is an item.
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    
    for name in names:
        # Removes extra whitespace at the beginning and end of a string.
        stripped_name = name.strip()
        # Replaces the first text with the second text.
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

