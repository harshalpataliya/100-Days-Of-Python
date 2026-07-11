from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
making_coffee = CoffeeMaker()
making_money = MoneyMachine()


is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False

    elif choice == "report":
        making_coffee.report()
        making_money.report()


    else:
        drink = menu.find_drink(choice)

        if drink and making_coffee.is_resource_sufficient(drink):
            if making_money.make_payment(drink.cost):
                making_coffee.make_coffee(drink)





