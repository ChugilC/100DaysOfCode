# Day 5 - Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

n_letters = int(input("How many letters would you like in your password?\n"))
n_symbol = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

# ------------------ Easy Level -------------------------
password = ''
# -- Letters
for num in range(1, n_letters + 1):
    let = random.choice(letters)
    password += let

# -- Numbers
for num in range(1, n_numbers + 1):
    let = random.choice(numbers)
    password += let

# -- Symbols
for num in range(1, n_symbol + 1):
    let = random.choice(symbols)
    password += let 

print(f"Easy Password: {password}")

# ------------------ Hard Level -------------------------
password_list = []
# -- Letters
for num in range(1, n_letters + 1):
    let = random.choice(letters)
    password_list.append(let)

# -- Numbers
for num in range(1, n_numbers + 1):
    let = random.choice(numbers)
    password_list.append(let)

# -- Symbols
for num in range(1, n_symbol + 1):
    let = random.choice(symbols)
    password_list.append(let)

# Shuffle the List
random.shuffle(password_list)

new_password = ""
for char in password_list:
    new_password += char

print(f"Hard Password: {new_password}")