# Day 8 - Caesar Cipher
from timeit import repeat
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True

# caesar - Helper fn to encrypt and decrypt
def caesar(text, shift, direction):
    caesar_text = ""
    for char in text:
        if char not in alphabet:
            caesar_text += char
        else:
            idx = alphabet.index(char)
            if direction == 'encode':
                caesar_text += alphabet[(idx + shift) % len(alphabet)]
            elif direction == 'decode':
                caesar_text += alphabet[(idx - shift) % len(alphabet)]
    print(f"Here's the {direction}d result: {caesar_text}")

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    
    repeat_task = input("To restart the program, Type 'yes' or to close the program, Type 'no'\n")
    if repeat_task == 'no':
        should_continue = False