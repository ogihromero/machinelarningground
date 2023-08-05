# Make a rock, paper, scissors game.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

player_pick = int(
    input("What do you choose?  Type 0 for rock, 1 for paper and 2 for scissors"))
print(options[player_pick])

computer_pick = random.randint(0, 2)
print("Computer pick:")
print(options[computer_pick])

if player_pick >= 3 or player_pick < 0:
    print("You typed an invalid number, you lose!")
if player_pick == computer_pick:
    print("It's a draw")
elif player_pick == 0 and computer_pick == 2:
    print("You win!")
elif computer_pick == 0 and player_pick == 2:
    print("You lose")
elif computer_pick > player_pick:
    print("You lose")
elif player_pick > computer_pick:
    print("You win!")
