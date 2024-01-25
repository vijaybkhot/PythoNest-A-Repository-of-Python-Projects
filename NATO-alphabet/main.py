import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")  # Create a dataframe object from the csv file
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}  # Create a dictionary in above format
# nato_df.iterrows() give index and row.
# We populate our new dictionary by accessing the letter and code columns

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Please enter a word: ")  # Ask for user input
phonetic_list = []
loop_over = False
while True:
    try:
        phonetic_list = [nato_dict[char.capitalize()] for char in
                         user_word]  # build a list of phonetic words from above list
        # for char in user_word:
        #     if char.capitalize() in nato_dict.keys():
        #         phonetic_list.append(nato_dict.get(char.capitalize()))
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        user_word = input("Please enter a word: ")
    else:
        break

print(phonetic_list)
