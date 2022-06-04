import random
from os import system
from game_data import data
from art import logo, vs

# Compare the 2 data
def compare(option_a, option_b):
    a_followers = option_a['follower_count']
    b_followers = option_b['follower_count']

    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")
    
    ans = input("Who has more followers, Type 'A' or 'B': ").lower()

    if ans == 'a' and a_followers > b_followers:
        return True
    elif ans == 'b' and b_followers > a_followers:
        return True
    else:
        return False

# Get  data
def get_account():
    return random.choice(data)

# Clear Screen and Print Logo
def cls_screen():
    system('cls')
    print(logo)

print(logo)

# Main game logic
def game():
    account_a = get_account()
    account_b = get_account()
    score = 0
    is_playing = True
    
    while is_playing:
        account_a = account_b
        account_b = get_account()

        while account_a == account_b:
            account_b = get_account()

        result = compare(account_a,account_b)

        if result:
            score += 1
            cls_screen()
            print(f"Correct your score is {score}")
        else:
            is_playing = False
            cls_screen()
            print(f"Sorry that's wrong your final score is {score}")

game()