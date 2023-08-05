# write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

pick = random.choice(names)

print(f"{pick} is going to buy the meal today!")
