print("💸 Welcome to the tip calculator. ")

# float() converts the data type into a floating point number.
total_bill = float(input("What was the total bill? $"))
# int() converts the data type into an integer.
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
# round() rounds the number down to an integer, but if a second parameter is included (e.g. 2) then it rounds it to that many decimal places.
split_tip = round(total_bill * (1 + (percent_tip / 100)) / people, 2)
# "{:.2f}".format() formats the number to always have two decimal places (e.g. 2 -> 2.00).
format_split_tip = "{:.2f}".format(split_tip)

# Uses an f string for string concatenation.
print(f"Each person should pay: ${format_split_tip}")