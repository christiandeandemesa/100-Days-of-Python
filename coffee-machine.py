MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

order_coffee = True

# Checks to see if we have enough water, milk, and coffe to make your order, and, if so, subtracts the resources used.
def are_resources_sufficient(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient} to make your {drink_name}...\n")
            return False
        else:
            resources[ingredient] -= drink_ingredients[ingredient]
            return True
        
# Tallies the total amount from the given coins.
def process_payment():
    quarter_amount = float(input("Please insert coins.\nHow many quarters? "))
    dime_amount = float(input("How many dimes? "))
    nickel_amount = float(input("How many nickels? "))
    penny_amount = float(input("How many pennies? "))
    total = (quarter_amount * 0.25) + (dime_amount * 0.1) + (nickel_amount * 0.05) + (penny_amount * 0.01)
    return total

# Checks to see if the money provided is enough to purchase your drink, and, if so, gives change.
def is_payment_successful(money, drink_cost):
    if money >= drink_cost:
        change = round(money - drink_cost, 2)

        if change > 0:
            print(f"Here is your change: ${'{:.2f}'.format(change)}")

        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Refunding your money...\n")
        return False

# Goes through the ordering process for your coffee.
while order_coffee:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if drink_choice == "off":
        print("You've turned off the coffee machine!")
        order_coffee = False
    elif drink_choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${'{:.2f}'.format(profit)}\n")
    elif drink_choice != "espresso" and drink_choice != "latte" and drink_choice != "cappuccino":
        print("Sorry, but we don't carry that drink...\n")
    else: 
        drink = MENU[drink_choice]

        if are_resources_sufficient(drink, drink["ingredients"]):
            payment = process_payment()

            if is_payment_successful(payment, drink["cost"]):
                print(f"Here is your {drink}: ☕ Please enjoy!\n")