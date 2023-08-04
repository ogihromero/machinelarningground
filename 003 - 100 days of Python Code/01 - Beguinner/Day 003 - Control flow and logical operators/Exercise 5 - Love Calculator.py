# write a program that tests the compatibility between two people.
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1.lower() + name2.lower()
t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
first_digit = t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
