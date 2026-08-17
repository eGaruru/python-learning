from art import logo
print(logo)

is_bidding = True
winner = {
    "name": "",
    "bid": 0
}

bids = {}

while is_bidding:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    bids[name] = bid

    # TODO-3: Whether if new bids need to be added
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if continue_bidding == "yes":
        print("\033[H\033[J", end="")

    if continue_bidding == 'no':
        is_bidding = False

        for name in bids:
            if bids[name] > winner["bid"]:
                winner["name"] = name
                winner["bid"] = bids[name]

# TODO-4: Compare bids in dictionary
print(f"The winner is {winner["name"]} with a bid of ${winner["bid"]}")

# SOLUTION
# from art import logo
# print(logo)
#
# # TODO-1: Ask the user for input
# # TODO-2: Save data into dictionary {name: price}
# # TODO-3: Whether if new bids need to be added
# # TODO-4: Compare bids in dictionary
# def find_highest_bidder(bidding_dictionary):
#     winner = ""
#     highest_bid = 0
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#
#     # Alternative
#     # winner = max(bidding_dictionary, key=bidding_dictionary.get)
#     # highest_bid = bidding_dictionary[winner]
#
#     print(f"The winner is {winner} with a bid of ${highest_bid}.")
#
# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 20)