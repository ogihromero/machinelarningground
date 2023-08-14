############ DEBUGGING#####################


from random import randint

# Describe Problem
# problem: the loop ends before 20


def my_function():
    #   for i in range(1, 20): line with the problem
    for i in range(1, 21):  # fixed code
        if i == 20:
            print("You got it")


my_function()

# Reproduce the Bug
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)  # the error occurs when 6 gets selected
# dice_num = randint(6)  # reproducing the bug
dice_num = randint(0, 5)  # fixed code
print(dice_imgs[dice_num])

# Play Computer
# Problem: the code never picks  94
year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994: # any of the ifs have this problem
if year > 1980 and year <= 1994:  # fixed code
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# Fix the Errors
# age = input("How old are you?") # generates a string
age = int(input("How old are you? "))
if age > 18:
    # print("You can drive at age {age}.") # code is not indentend and is missing a f-string
    print(f"You can drive at age {age}.")

# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) extra equal
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# Use a Debugger


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    # b_list.append(new_item) # problem: wrong indent
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
