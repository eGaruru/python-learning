import random
from art import logo

# Constants
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
MIN_NUMBER = 1
MAX_NUMBER = 100


def create_random_number():
    """Create a random number between MIN_NUMBER and MAX_NUMBER"""
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def set_difficulty():
    """Return the attempts based on the difficulty"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def check_guess(answer, guess):
    """Check if guess is correct and return boolean"""
    if guess == answer:
        print(f"You got it! The answer was {answer}!")
        return True
    elif guess > answer:
        print("Too high")
    else:
        print("Too low")

    return False


def play_game():
    print(logo)
    print("Welcome to the Number guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer_number = create_random_number()
    attempts = set_difficulty()

    is_correct = False
    while attempts > 0 and not is_correct:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))
        is_correct = check_guess(answer_number, guessed_number)

        if not is_correct:
            attempts -= 1
            if attempts > 0:
                print("Guess again.")
            else:
                print("You've run out of guesses. Run the program to play again.")


play_game()

# SOLUTION
# from random import randint
# from art import logo
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
#
# # Function to check users' guess against actual answer
# def check_answer(user_guess, actual_answer, turns):
#     """Checks answer against guess, returns the number of turns remaining."""
#     if user_guess > actual_answer:
#         print("Too high")
#         return turns - 1
#     elif user_guess < actual_answer:
#         print("Too low")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {actual_answer}")
#
#
# # Function to set difficulty
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS
#
#
# def game():
#     # Choosing a random number between 1 and 100.
#     print(logo)
#     print("Welcome to the Number guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = randint(1, 100)
#
#     turns = set_difficulty()
#
#     guess = 0
#     # Repeat the guessing functionality
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         # Let the user guess the number
#         guess = int(input("Make a guess: "))
#
#         # Track the number of turns and reduce by 1 if they get it wrong
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")
#
#
# game()
