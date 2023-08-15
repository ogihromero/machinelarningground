# This games lets the player guess which person has more followers until a wrong guess happens.

import art
import os
from game_data import data
import random


def compare(entry1, entry2, guess):
    if entry1['follower_count'] >= entry2['follower_count'] and guess == 'A':
        return True
    elif entry1['follower_count'] <= entry2['follower_count'] and guess == 'B':
        return True
    else:
        return False


def game():
    end_game = False
    score = 0
    entity1, entity2 = random.sample(data, 2)
    while not end_game:
        print(art.logo)
        if score > 0:
            print(f"You're right :). Current score: {score}\n")
        # pick 2 random elements from list
        entity1 = entity2
        while entity1 == entity2:
            entity2 = random.choice(data)
        print(
            f"Compare A: {entity1['name']}, a {entity1['description']} from {entity1['country']}.")
        print(art.vs)
        print(
            f"versus B: {entity2['name']}, a {entity2['description']} from {entity2['country']}.")
        # let the user guess
        user_pick = input("Who has more followers? Type 'A' or 'B': ")
        # verify the answer and if the game will continue
        right_guess = compare(entity1, entity2, user_pick)
        if right_guess:
            score += 1
        else:
            end_game = True
        os.system('clear')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")


game()
