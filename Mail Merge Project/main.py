"""
The objective of the program is to write invitation letter. Each letter using
a sample letter. The only difference being that each letter contains the name
of each individual to be invited.
"""
# Open the starting letter in the Input folder as starting_letter
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()  # Assign the str contents to variable letter
    with open("./Input/Names/invited_names.txt") as names:  # Open invited_names.txt to get names of guests
        for name in names.readlines():  # Use readlines() method to create a list of all the elements on each line
            cleared_name = name.strip()  # Use name.strip() to strip off the leading and ending spaces around name
            personalized_letter = letter.replace("[name]", cleared_name)  # Replace the [name] string with the name
            with open(f"./Output/ReadyToSend/letter_for_{cleared_name}.txt", "w") as output_file:
                output_file.write(personalized_letter)  # Write a separate letter for each name
