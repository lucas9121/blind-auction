import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
auctions = []

continue_bidding = True


def winner(auctions):
    print(logo)
    winner_name = ""
    winner_bid = 0
    for dict in auctions:
        if(dict["bid"] > winner_bid):
            winner_bid = dict["bid"]
            winner_name = dict["name"]
    print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
    
while continue_bidding:
    print(logo)
    new_dict = {}
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    others = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    new_dict["name"] = name
    new_dict["bid"] = bid
    auctions.append(new_dict)
    os.system('clear')
    if(others == 'no'):
        continue_bidding = False
        winner(auctions)