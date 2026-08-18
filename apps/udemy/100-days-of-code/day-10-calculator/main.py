from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate():
    print(logo)
    first_number = float(input("What's the first number?: "))

    while True:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("What's the next number?: "))

        result = operators[operator](first_number, second_number)

        print(f"{first_number} {operator} {second_number} = {result}")

        continue_calculating = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ")

        if continue_calculating == "y":
            first_number = result
        else:
            print("\033[H\033[J", end="")
            return

while True:
    calculate()


# my_favourite_operator = add
# print(my_favourite_operator(2, 5))

# SOLUTION
# from art import logo
# print(logo)

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# operators = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# def calculator():
#     should_accumulate = True
#     num_1 = float(input("What's the first number?: "))

#     while should_accumulate:
#         for symbol in operators:
#             print(symbol)
#         operator_symbol = input("Pick an operation: ")
#         num_2 = float(input("What's the next number?: "))
#         answer = operators[operator_symbol](num_1, num_2)
#         print(f"{num_1} {operator_symbol} {num_2} = {answer}")

#         choice = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ")

#         if choice == "y":
#             num_1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 20)
#             calculator()

# calculator()