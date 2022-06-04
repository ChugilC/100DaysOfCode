# Day 15 - Coffee Machine
from importlib.resources import is_resource
from art import logo
from os import system

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

# CHeck for resource availability
def is_resource_sufficient(ing):
    for item in ing:
        if ing[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Process coins
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# Transaction
def transaction_successfull(money_received, drink_cost):
    if money_received >= drink_cost:
        
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")

        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Make Coffee
def make_coffee(drink_selected, ing):
    for item in ing:
        resources[item] -= ing[item]
    print(f"Enjoy your {drink_selected} ☕")

# Main Logic
while is_on:
    print(logo)
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if transaction_successfull(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])