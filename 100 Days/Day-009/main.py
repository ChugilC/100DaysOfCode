# Day 9 - Blind Auction
from art import logo
from os import system

print(logo)
print("Welcome to the secret auction program.")

is_going = True
bidders = {}

# find the highest bidder
def highest_bidder(all_bidders):
    maxi = 0
    user = ""
    for bidder in all_bidders:
        amount = all_bidders[bidder]
        if amount > maxi:
            maxi = amount
            user = bidder
    print(f"The winner is {user} for the bid amount ${maxi}.")

# Ask the name and bid amount
while is_going:
    name = input("What's your name?: ")
    amount = int(input("What's your bid?: $"))

    # Store the bidder's data
    bidders[name] = amount
    others = input("Are there any other bidders? Type 'yes' or 'no': ")
    
    if others == "no":
        is_going = False
        highest_bidder(bidders)
    elif others == "yes":
        system('cls')