print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

choice1 = input(
    'You want to go right and stay in the beach or left in the middle of the forest? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input(
        'You\'ve come to a river. There is a small boat to cross the river. Type "board" to get on the boat. Type "swim" to swim across. \n').lower()
    if choice2 == "board":
        choice3 = input("You safely reach the other side of the river. Ahead, there's a mysterious cave with two entrances. Which entrance will you choose? The one on the 'left' or the one on the 'right'? \n").lower()
        if choice3 == "left":
            print(
                "You find yourself in a beautiful underground garden. The treasure is right here! You Win!")
        elif choice3 == "right":
            print("You encounter a swarm of bats. You must retreat. Game Over.")
        else:
            print("You hesitate and miss your chance. Game Over.")
    elif choice2 == "swim":
        print("The river's current is too strong, and you get swept away. Game Over.")
    else:
        print("You couldn't decide and missed the opportunity. Game Over.")
else:
    print("You take the right path, but it leads you to a dead end. Game Over.")
