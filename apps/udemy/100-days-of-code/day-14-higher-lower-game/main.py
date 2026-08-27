import random
from art import logo, vs
from game_data import data


# Generate random number **Alternative: random.choice**
def generate_random_number(data_list):
    """Returns a random index between 0 and length of data list"""
    return random.randrange(0, len(data_list))


# Check the choice is correct
def check_more_followers(followers_of_a, followers_of_b):
    """Returns 'A' or 'B' which has more followers than other"""
    if followers_of_a > followers_of_b:
        return "A"
    else:
        return "B"


def game():
    """Main game loop"""
    num1 = generate_random_number(data)
    num2 = generate_random_number(data)

    # Set player score and loop condition
    player_score = 0
    should_continue = True
    print(logo)

    # When player answered correct, keep playing
    while should_continue:
        # When random numbers are same, generate num2 again
        while num1 == num2:
            num2 = generate_random_number(data)

        # with random number, choose the data from data list
        compare_a = data[num1]
        against_b = data[num2]

        # show the 2 datum based on dictionary
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
        print(vs)
        print(f"Against B: {against_b['name']}, a {against_b['description']}, from {against_b['country']}.")

        # Ask player which person/media etc. has more follower
        player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Check if the choice is correct
        correct_answer = check_more_followers(compare_a["follower_count"], against_b["follower_count"])

        if correct_answer == player_choice:
            # When player answered correct, get + 1 score and show score
            player_score += 1
            print("\n" * 20)
            print(logo)
            print(f"You're right! Current score: {player_score}.")

            # Carry over to the next round, against B -> compare A
            num1 = num2
            num2 = generate_random_number(data)
        else:
            # When player answered wrong, stop the game and show score
            should_continue = False
            print("\n" * 20)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {player_score}")


game()

# SOLUTION
# Display art
# from art import logo, vs
# from game_data import data
# import random
#
#
# def format_data(account):
#     """Takes the account data and returns the printable format."""
#     account_name = account['name']
#     account_descr = account['description']
#     account_country = account['country']
#
#     return f"{account_name}, a {account_descr}, from {account_country}."
#
#
# def check_answer(user_guess, a_followers, b_followers):
#     """Take a user's guess and the followers counts and returns if they got it right."""
#     if a_followers > b_followers:
#         return user_guess == 'a'
#     else:
#         return user_guess == 'b'
#
#
# print(logo)
# score = 0
# game_should_continue = True
#
# # Generate a random account from the game data
# account_b = random.choice(data)
#
# # Make the game repeatable.
# while game_should_continue:
#
#     # Making account at position B become the next account at position A.
#     account_a = account_b
#     account_b = random.choice(data)
#
#     if account_a == account_b:
#         account_b = random.choice(data)
#
#     print(f"Compare A: {format_data(account_a)}")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}")
#
#     # Ask user for a guess.
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#
#     # Clear the screen
#     print("\n" * 20)
#     print(logo)
#
#     # Check if user is correct
#     ## Get follower count of each account
#     a_follower_count = account_a['follower_count']
#     b_follower_count = account_b['follower_count']
#
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#     # Give user feedback on their guess.
#     # score keeping.
#     if is_correct:
#         score += 1
#         print(f"You're right! Current score: {score}")
#     else:
#         print(f"Sorry, that's wrong. Final score: {score}")
#         game_should_continue = False