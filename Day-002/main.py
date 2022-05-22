# Day 2 - Tip Calculator
print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage would you like to give? 10 or 12 or 15? "))
people = int(input("How many people to split the bill? "))

total = bill + (bill * (percentage / 100))
people_amount = round(total / people, 2)

print(f"Each one of you should pay: ${people_amount}")