import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Uses dictionary comprehension to create a dictionary by iterating over each row in the DataFrame, and making the key that row's letter and its value that row's code.
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()

    # Tries the code within the try block.
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    # Executes the code within the except block if the code within the try block fails.
    # The except block can take a specific error to look for.
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    # Executes the code within the else block if the code within the try block succeeds.
    else:
        print(output_list)

generate_phonetic()