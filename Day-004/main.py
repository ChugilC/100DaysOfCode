# Day 4 - RPS
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for 'Rock', 1 for 'Paper', 2 for 'Scissors\n'"))
values = [rock, paper, scissors]

your_choice = values[choice]
print(your_choice)

computer_choice = random.randint(0,2)
comp_val = values[computer_choice]
print("Computer Choose:")
print(comp_val)

if choice == 0 and computer_choice == 2:
    print("You Won")
elif choice == 1 and computer_choice == 2:
    print("You Lose")
elif choice == 2 and computer_choice == 2:
    print("It's a Draw")
elif choice == 0 and computer_choice == 0:
    print("It's a Draw")
elif choice == 1 and computer_choice == 0:
    print("You Won")
elif choice == 2 and computer_choice == 0:
    print("You Lose")
elif choice == 0 and computer_choice == 1:
    print("You Lose")
elif choice == 1 and computer_choice == 1:
    print("It's a Draw")
elif choice == 2 and computer_choice == 1:
    print("You Won")