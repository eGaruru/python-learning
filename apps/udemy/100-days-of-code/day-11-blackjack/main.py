import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    return random.choice(cards)


def calculate_score(hand):
    if sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1

    return sum(hand)


def play_game():
    print(logo)

    user_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]

    is_game_over = False
    while is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")
        draw_another = input("Type 'y' to get another card, type 'n' to pass: ")

        if draw_another == 'y':
            user_cards.append(draw_card())
            user_score = calculate_score(user_cards)

            if user_score > 21:
                is_game_over = True
                print("You went over. You lose😭")
        else:
            is_game_over = True

    while dealer_score < 17:
            dealer_cards.append(draw_card())
            dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score {dealer_score}")
    if user_score == dealer_score:
        print("Draw")
    elif user_score > dealer_score:
        print("You win!🥳")
    else:
        print("You lose😭")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
