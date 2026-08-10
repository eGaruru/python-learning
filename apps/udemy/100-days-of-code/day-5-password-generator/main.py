# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level
letters_of_password = ""
for index in range(0, nr_letters):
    letters_of_password += random.choice(letters)

letter_of_symbols = ""
for index in range(0, nr_symbols):
    letter_of_symbols += random.choice(symbols)

letter_of_numbers = ""
for index in range(0, nr_numbers):
    letter_of_numbers += random.choice(numbers)

password = f"{letters_of_password}{letter_of_symbols}{letter_of_numbers}"
print("Your password is: ", password)

# Hard level
list_of_letters = []
for letter in password:
    list_of_letters.append(letter)

random.shuffle(list_of_letters)
password = "".join(list_of_letters)
print("Your password is: ", password)

# SOLUTION
# # Easy level
# password = ""
# 
# for char in range(0, nr_letters):
#     password += random.choice(letters)
# 
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
# 
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
# 
# print(password)
# 
# # Hard level
# password_list = []
# 
# for char in range(0, nr_letters):
#     password_list.append(random.choice(letters))
# 
# for char in range(0, nr_symbols):
#     password_list.append(random.choice(symbols))
# 
# for char in range(0, nr_numbers):
#     password_list.append(random.choice(numbers))
# 
# random.shuffle(password_list)
# 
# password = ""
# for char in password_list:
#     password += char
# 
# print("Your password is: ", password)