############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from art import logo
import random
import os

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


def deal_card():
    """ Returns a random card, A value will be determined later"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Given a list of cards, returns the score and determines if A should be 11 or 1"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compare both scores and determine the winner"""
    if user_score > 21 and computer_score > 21:
        return "You went over, you lose."
    elif user_score == computer_score:
        return "It's a draw!!"
    elif user_score > 21:
        return "You went over, you lose."
    elif user_score == 0:
        return "Blackjack, you win :) !!"
    elif user_score > computer_score:
        return "You win :)"
    else:
        return "You lose"


def game():
    user_cards = []
    computer_cards = []
    end_game = False
    print(logo)
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not end_game:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Computer first card: {computer_cards[0]}")
        print(f"User cards: {user_cards}")
        print(f"Your score: {user_score}")

        if user_score == 0 or user_score > 21 or computer_score == 0:
            end_game = True
        else:
            user_pick = input("Do you want to pick another card? 'y' or 'n' ")
            if user_pick == 'y':
                user_cards.append(deal_card())
            else:
                end_game = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}")
    print(f"Your score: {calculate_score(user_cards)}")
    print(f"Computer cards: {computer_cards}")
    print(f"Computer score: {calculate_score(computer_cards)}")
    print(compare(user_score, computer_score))


while input("Do you want to play blackjack?  Type 'y' or 'n': ") == "y":
    os.system('clear')
    game()
