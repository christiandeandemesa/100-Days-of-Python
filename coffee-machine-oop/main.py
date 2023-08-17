from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

order_coffee = True

while order_coffee:
    drink_options = menu.get_items()
    drink_choice = input(f"What would you like ({drink_options}): ")

    if drink_choice == "off":
        print("You've turned off the coffee machine!")
        order_coffee = False
    elif drink_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink_choice != "espresso" and drink_choice != "latte" and drink_choice != "cappuccino":
        print("Sorry, but we don't carry that drink...")
    else:
        drink = menu.find_drink(drink_choice)

        if coffee_maker.is_resource_sufficient(drink) and (money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)