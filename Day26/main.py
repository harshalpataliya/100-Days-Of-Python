import pandas
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


ask_word = input("Enter your word: ").upper()
result = [phonetic_dict[letter] for letter in ask_word]
print(result)