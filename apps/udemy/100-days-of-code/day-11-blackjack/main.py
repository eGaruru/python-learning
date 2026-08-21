import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    """Draw a random card."""
    return random.choice(cards)


def calculate_score(hand):
    """Calculate the score of a hand and return the score.
    When user's score went over 21 and has 11, replace 11 to 1."""
    while sum(hand) > 21 and 11 in hand:
          hand[hand.index(11)] = 1

    return sum(hand)

def check_winner(user_score, dealer_score):
    """Compare user score and dealer score to check winner."""
    if user_score > 21:
        return "You went over. You lose😭\n"
    elif dealer_score > 21:
        return "Dealer went over. You win!🥳\n"
    elif user_score == dealer_score:
        return "Draw😲\n"
    elif user_score > dealer_score:
        return "You win!🥳\n"
    else:
        return "You lose😭\n"

def play_game():
    print(logo)

    user_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    is_game_over = False
    while not is_game_over:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")
        draw_another = input("Type 'y' to get another card, type 'n' to pass: ")

        if draw_another == 'y':
            user_cards.append(draw_card())
            user_score = calculate_score(user_cards)
            if user_score > 21:
                is_game_over = True
        else:
            is_game_over = True

    if user_score <= 21:
        while dealer_score < 17:
            dealer_cards.append(draw_card())
            dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score {dealer_score}")
    print(check_winner(user_score, dealer_score))

def run():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        print("\n" * 20)
        play_game()

    print("See you next time!")

run()