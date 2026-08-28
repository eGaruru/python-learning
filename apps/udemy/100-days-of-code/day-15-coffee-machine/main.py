COIN_AMOUNT = {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickles" : 0.05,
    "pennies" : 0.01
}

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


def make(drink, m_resources):
    ingredients = MENU[drink]["ingredients"]

    new_resources = {}
    for name, amount in ingredients.items():
        new_resources[name] = m_resources[name] - amount

    return new_resources

def report(m_resources):
    for drink, amount in resources.items():
        print(f"{drink.title()}: {amount}")

def off():
    print("Off")

operate_machine = {
    "make": make,
    "report": report,
    "off": off,
}

# def operate_machine(operation):
#
#     if operation == "report":
#         water = resources["water"]
#         milk = resources["milk"]
#         coffee = resources["coffee"]
#         print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}")
#     elif operation == "make":
#
#     elif operation == "off":
#         print("Off")

def check_resources(machine_resources, drink):
    ingredients = MENU[drink]["ingredients"]
    for item in machine_resources:
        if resources[item] < ingredients[item]:
            return False
    return True


# TODO 5 calculate coins
def calculate_coins(drink_cost, c_quarters, c_dimes, c_nickles, c_pennies):
    amount = 0
    amount += COIN_AMOUNT["quarters"] * c_quarters
    amount += COIN_AMOUNT["dimes"] * c_dimes
    amount += COIN_AMOUNT["nickles"] * c_nickles
    amount += COIN_AMOUNT["pennies"] * c_pennies
    return order_cost < amount

# TODO 1 Prompt user by asking “What would you like?
order = input("What would you like? (espresso/latte/cappuccino): ")
print("Please insert coins.")

# TODO 2 Turn off the Coffee Machine by entering “off” to the prompt.
# operate_machine("off")

# TODO 3 Print report.
# operate_machine("report")

# TODO 4 Check resources sufficient?


quarters = int(input("how many quarters?: "))
dimes = int(input("how many dimes?: "))
nickles = int(input("how many nickles?: "))
pennies = int(input("how many pennies?: "))

is_sufficient = check_resources(resources, order)

order_cost = MENU[order]["cost"]
is_enough_money = calculate_coins(order_cost, quarters, dimes, nickles, pennies)
if is_sufficient and is_enough_money:
    operate_machine["make"]()
    print(f"Here is your {order}. Enjoy!☕")
else:
    print("Sorry that's not enough money. Money refunded.")




