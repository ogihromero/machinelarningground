
# Calculator

from art import logo
import os

# Add funciton


def add(num1, num2):
    return num1 + num2

# Subtract function


def subtract(num1, num2):
    return num1 - num2

# Multiply function


def multiply(num1, num2):
    return num1 * num2

# Divide


def divide(num1, num2):
    return num1 / num2


# Dict with operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    end_program = False

    while not end_program:
        for operation in operations:
            print(operation, end=" ")
        user_choice = input(
            "\nWhat operation do you want from the list above? ")
        num2 = float(input("What's the next number?: "))
        answer = operations[user_choice](num1, num2)
        print(f"{num1:.2f} {user_choice} {num2:.2f} = {answer:.2f}")
        end_choice = input(
            f"Type 'y' if you want to continue calculating with {answer}, 'n' to start a new calculation or anything else to exit")
        if end_choice == 'y':
            num1 = answer
        elif (end_choice == 'n'):
            end_program = True
            os.system('clear')
            calculator()
        else:
            print("Thanks for using the calculator, exiting...")
            end_program = True


calculator()
