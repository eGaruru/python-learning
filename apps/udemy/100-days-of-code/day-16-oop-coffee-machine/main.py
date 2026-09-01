from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
drinks = Menu()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"What would you like? ({drinks.get_items()}): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = drinks.find_drink(choice)
        if order and coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)

# SOLUTION
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()

# is_on = True

# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? {options}: ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)


