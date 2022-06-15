import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("100 Days/Day-026/nato_phonetic_alphabet.csv")

data_dict = {row["letter"]: row["code"] for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
nato_alpabets = [data_dict[char] for char in word]
print(nato_alpabets)