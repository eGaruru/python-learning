COIN_AMOUNT = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
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


def make_drink(d_ingredients: dict[str, int], m_resources: dict[str, int]):
    new_resources = {}
    for name, d_amount in d_ingredients.items():
        new_resources[name] = m_resources[name] - d_amount

    return new_resources


def report_machine_resources(m_resources: dict[str, int], m_money):
    for drink, r_amount in m_resources.items():
        print(f"{drink.title()}: {r_amount}")
    print(f"Money: ${m_money:.2f}")


def check_resources(d_ingredients: dict[str, int], m_resources: dict[str, int]):
    for item in d_ingredients:
        if m_resources[item] < d_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True


def calculate_coins(c_quarters, c_dimes, c_nickels, c_pennies):
    c_amount = 0
    c_amount += COIN_AMOUNT["quarters"] * c_quarters
    c_amount += COIN_AMOUNT["dimes"] * c_dimes
    c_amount += COIN_AMOUNT["nickels"] * c_nickels
    c_amount += COIN_AMOUNT["pennies"] * c_pennies
    return c_amount


def run():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    money_in_machine = 0
    is_machine_running = True

    # TODO 6 Loop until shutdown
    while is_machine_running:

        # TODO 1 Prompt user by asking “What would you like?
        order = input("What would you like? (espresso/latte/cappuccino): ")

        if order == "off":
            # TODO 2 Turn off the Coffee Machine by entering “off” to the prompt.
            is_machine_running = False
        elif order == "report":
            # TODO 3 Print report.
            report_machine_resources(resources, money_in_machine)
        elif order not in MENU:
            print("Sorry that's not a valid option.")
        else:
            # TODO 4 Check resources sufficient?
            is_sufficient = check_resources(MENU[order]["ingredients"], resources)

            if is_sufficient:
                try:
                    print("Please insert coins.")
                    quarters = int(input("how many quarters?: "))
                    dimes = int(input("how many dimes?: "))
                    nickels = int(input("how many nickels?: "))
                    pennies = int(input("how many pennies?: "))
                except ValueError:
                    print("please insert coins.")
                    continue

                # TODO 5 Calculate coins
                order_cost = MENU[order]["cost"]
                money_of_user = calculate_coins(quarters, dimes, nickels, pennies)
                is_enough_money = money_of_user >= order_cost

                if is_enough_money:

                    resources = make_drink(MENU[order]["ingredients"], resources)
                    money_in_machine += order_cost
                    print(f"Here is ${round(money_of_user - order_cost, 2)} in change.")
                    print(f"Here is your {order}. Enjoy!☕")
                else:
                    print("Sorry that's not enough money. Money refunded.")


run()
