# Day 7 - Hangman
import random
import hangman_words
from hangman_art import stages, logo

print(logo)

words_list = hangman_words.word_list
chosen_word = random.choice(words_list)
lives = 6

# print(f"Pssss, The solution is {chosen_word}")

display = []

for i in range(len(chosen_word)):
        display.append('_')

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You already guessed the letter {guess}")

    # Fill the display if guessed word is ocrrect
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    
    

    # Draw hangman if guess is not correct
    if guess not in chosen_word:
        print(f"You guessed a letter {guess}, That's not in the word. You lose a life")
        print(stages[lives])
        lives -= 1

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")
    elif lives < 0:
        end_of_game = True
        print("You Lose")
        print(f"The correct word is: {chosen_word}")