# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age? ")

age = 90 - int(age)
days = age * 365
weeks = age * 52
months = age * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
