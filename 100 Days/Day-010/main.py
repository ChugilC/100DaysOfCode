# Day 10 - Calculator
from art import logo
from os import system
#print(logo)

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply 
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Square root
def square_root(n1, n2):
    return n1 ** n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide, "**": square_root}



def calculation():
    print(logo)
    is_calculating = True
    num1 = float(input("What's the first number? "))

    while is_calculating:
        for key in operations:
            print(key)

        operation_symbol = input("Pick an operation to perform: ")

        num2 = float(input("What's the next number? "))

        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        is_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ")
        if is_going == 'n':
            is_calculating = False
            system('cls')
            calculation()
        else:
            num1 = answer

calculation()