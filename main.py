# Importing pandas moudel.
import pandas
# Reading the nato_phonetic_alphabet.csv and saving it into a variable called data.
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Creating new dictionary using the dictionary comprehension.
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# Taking input from user about the word and uppercase it.
word = input("Enter a word: ").upper()
# creating a list using list comprehension.
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
