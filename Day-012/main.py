# Day 12 - Number guesing game

# Concepts learned
# 1. Global vs Local Scope
# 2. There is no BLOCK scope in python
import random

print("Welcome to my Number Guessing Game")
print("I'm thinking a number between 1 and 50")

number = random.randrange(1,50)
difficulity = input("Choose your difficulity 'easy' or 'hard': ")
is_playing = True

if difficulity == 'easy':
    level = 10
elif difficulity == 'hard':
    level = 5
else:
    print("Please enter the correct difficulity!")
    is_playing = False

while is_playing:

    # Check level
    if level == 0:
        is_playing = False
    else:
        guess = int(input("Guess my number: "))
        level -= 1

        if guess > number:
            print("Guess is too high")
            print(f"You have {level} guesses remaining.")
        elif guess < number:
            print("Guess is too low")
            print(f"You have {level} guesses remaining.")
        elif guess == number:
            print("You guessed the correct number, You Won!")
            is_playing = False