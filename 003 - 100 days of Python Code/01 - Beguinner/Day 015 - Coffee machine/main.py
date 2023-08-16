MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def resource_status():
    for item in resources:
        print(f"{item.title()}: {resources[item]} ml")
    print(f"Money: ${profit:.2f}")


def check_resource(drink):
    """Return True if there's enough resources to make the drink, otherwise returns false"""
    for item in MENU[drink]['ingredients']:
        if resources[item] < MENU[drink]['ingredients'][item]:
            print(f"Sorry, there is not enough {item} for the {drink}")
            return False
    return True


def process_coins(drink):
    """Return True if enough money was inserted to purchase the drink, otherwise returns false"""
    print("Please insert coins.")
    global profit
    money = 0.25 * (float(input("How many quarters?: ")))
    money += 0.10 * (float(input("How many dimes?: ")))
    money += 0.05 * (float(input("How many nickles?: ")))
    money += 0.01 * (float(input("How many pennies?: ")))
    print(f"You put {money:.2f}. ")
    if money >= MENU[drink]['cost']:
        profit += MENU[drink]['cost']
        money -= MENU[drink]['cost']
        print(f"Here's  {money:.2f} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(drink):
    """ Removes the necessary resources to make the specified drink"""
    for item in MENU[drink]['ingredients']:
        global resources
        resources[item] -= MENU[drink]['ingredients'][item]


machine_on = True
while machine_on:
    choice = input(
        "Hi, What would you like? (espresso - $1.50/latte - $2.50/cappuccino - $3.00):” ").lower()
    if choice == "off":
        print("Machine will turn off")
        machine_on = False
    elif choice == "report":
        resource_status()
    else:
        if check_resource(choice):
            if process_coins(choice):
                make_drink(choice)
                print(f"Here is your {choice}. Enjoy! ")
