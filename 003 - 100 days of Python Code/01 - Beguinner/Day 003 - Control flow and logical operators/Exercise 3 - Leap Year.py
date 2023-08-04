# Write a program that works out whether if a given year is a leap year. A

year = int(input("Which year do you want to check? "))

if year % 4 != 0:
    print("Not leap year.")
elif (year % 400 == 0):
    print("Leap year.")
elif (year % 100 == 0):
    print("Not leap year.")
else:
    print("Leap year.")
