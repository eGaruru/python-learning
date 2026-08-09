# Rock Paper Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]
choices = ['rock', 'paper', 'scissors']

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if not 0 <= user_choice <= 2:
    print("Invalid choice, please try again")
else:
    computer_choice = random.randint(0, 2)

    user_hand = choices[user_choice]
    computer_hand = choices[computer_choice]

    print(hands[user_choice])
    print("Computer chose:")
    print(hands[computer_choice])

    if user_hand == computer_hand:
        print("It's a draw")
    elif user_hand == "rock":
        if computer_hand == "paper":
            print("You lose")
        else:
            print("You win")
    elif user_hand == "paper":
        if computer_hand == "scissors":
            print("You lose")
        else:
            print("You win")
    else:
        if computer_hand == "rock":
            print("You lose")
        else:
            print("You win")


# SOLUTION
# game_images = [rock, paper, scissors]
# 
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
# 
# if user_choice >= 0 and user_choice <= 2:
#     print(game_images[user_choice])
# 
# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])
# 
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number. You lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw!")
