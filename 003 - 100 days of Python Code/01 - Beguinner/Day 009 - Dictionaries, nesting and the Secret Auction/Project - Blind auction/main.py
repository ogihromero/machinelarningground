from art import logo
import os


def highest_bid(bids_dict):
    winner_name = ""
    winner_bid = 0
    for bidder in bids_dict:
        if bids_dict[bidder] > winner_bid:
            winner_name = bidder
            winner_bid = bids_dict[bidder]
    print(logo)
    print(f"The winner is {winner_name} with a bid of ${winner_bid:.2f}")


bidders = {}
end_program = False
while not end_program:
    print(logo)
    print("Welcome to the secret auction program. ")
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: "))
    bidders[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    os.system('clear')
    if (more_bidders) == "no":
        # (more_bidders) == "no":
        end_program = True

highest_bid(bidders)
