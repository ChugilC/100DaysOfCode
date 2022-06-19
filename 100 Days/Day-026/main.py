import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("100 Days/Day-026/nato_phonetic_alphabet.csv")

data_dict = {row["letter"]: row["code"] for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_on = True

while is_on:
    word = input("Enter a word: ").upper()

    nato_alpabets = []
    for char in word:
        try:
            seperate_word = data_dict[char]
        except KeyError:
            print("Please provide only alphabets")
            break
        else:
            nato_alpabets.append(seperate_word)
            is_on = False

print(nato_alpabets)