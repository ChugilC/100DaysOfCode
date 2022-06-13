PLACEHOLDER = "[name]"

with open("100 Days/Day-024/Input/Names/invited_names.txt") as everyone:
    all_names = everyone.readlines()

with open("100 Days/Day-024/Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

    for name in all_names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        
        with open(f"100 Days/Day-024/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as write_letter:
            write_letter.write(new_letter)