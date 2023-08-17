import os
from secret_auction_program_art import logo

clear = lambda : os.system('tput reset')

print(f"{logo}\nWelcome to the secret auction program.")

more_bidders = True
bidders_dict = {}

while more_bidders:
    bidder = input("What is your name? ")
    bid = input("What is your bid? $")

    # Adds a key-value pair where bidder is the key and bid is the value to the dictionary.
    bidders_dict[bidder] = bid

    question = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if question != 'yes':
        more_bidders = False

    clear()

winning_bidder = ""
winning_bid = 0

# For loop over the keys in the dictionary.
for final_bidder in bidders_dict:
    # Values saved to dictionaries are converted into strings
    potential_bid = int(bidders_dict[final_bidder])

    if potential_bid > winning_bid:
        winning_bidder = final_bidder
        winning_bid = potential_bid

print(f"🧑‍⚖️  The winner is {winning_bidder} with a bid of ${winning_bid}")