# Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
from art import logo

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
EASY_MODE = 10
HARD_MODE = 5


def game():
    print(logo)
    print("Welcome to the guessing game!!")
    turns = EASY_MODE if (input(
        "Type 'y' if you want the easy mode, or anything else for hard mode: ") == 'y') else HARD_MODE
    right_number = random.randint(1, 100)
    print(f"the number is: {right_number}")
    while turns != 0:
        user_guess = int(
            input(f"You have {turns} tries remaining. Guess a number between 1 and 100: "))
        if user_guess == right_number:
            print(f"Right number, you won with {turns-1} guesses remaining")
            turns = 0
        elif user_guess > right_number:
            turns -= 1
            print(f"Wrong. Too high. ")

        elif user_guess < right_number:
            turns -= 1
            print(f"Wrong. Too low.")
    print(f"The answer was {right_number}")


game()
