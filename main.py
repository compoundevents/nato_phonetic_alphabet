# Importing pandas moudel and time
import pandas
from time import sleep

program_is_on = True
while program_is_on:
    # Reading the nato_phonetic_alphabet.csv and saving it into a variable called data.
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    # Creating new dictionary using the dictionary comprehension.
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    # Taking input from user about the word and uppercase it.
    word = input("Enter a word: ").upper()
    # creating a list using list comprehension.
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)
    exit_program = input("Do you want to exit the program 'y', 'n': ")
    if exit_program == "y":
        print("Please wait...")
        sleep(1)
        program_is_on = False
    else:
        pass
