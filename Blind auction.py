
from art import logo
print(logo)
end = False
bid = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidder_record = {"Favour": 123, "Precious": 500}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]  # 123, 500
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(" ")
    print(f"The winner of the bid is {winner} with a bid of ${highest_bid}")

import os
while not end:

    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    bid[name] = price
    # Favour = 123
    another = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if another == 'no':
        end = True
        find_highest_bidder(bidding_record = bid)

    elif another == 'yes':
        os.system('cls')











