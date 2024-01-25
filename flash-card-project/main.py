from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# Initialize the Tkinter window
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

try:
    # Try to read the edited CSV file, if it doesn't exist, create one from the original CSV file
    with open(file="./data/edited_french_words.csv") as starting_csv:
        word_csv = pandas.read_csv(starting_csv)

except FileNotFoundError:
    try:
        with open(file="./data/french_words.csv") as original_csv:
            temp_csv = pandas.read_csv(original_csv)
    except FileNotFoundError:
        # Show an error message if neither file is found
        messagebox.showerror("No flash card database found")
    else:
        # Save the original CSV as an edited CSV file
        temp_csv.to_csv("./data/edited_french_words.csv", index=False)
        with open(file="./data/edited_french_words.csv") as starting_csv:
            word_csv = pandas.read_csv(starting_csv)

finally:
    # Create a list of French words for flashcards
    french_word_list = word_csv['French'].to_list()

# Initialize a random French word
random_word = random.choice(french_word_list)


# Function to generate a new word on the canvas
def generate_word(canvas_sample):
    global window_timer, random_word, french_word_list
    window.after_cancel(window_timer)
    random_word = random.choice(french_word_list)
    canvas.itemconfig(card_image, image=card_front)
    canvas_sample.itemconfigure(title, text="French", fill='black')
    canvas_sample.itemconfigure(word, text=random_word, font=("Ariel", 60, "bold"), fill='black')
    window_timer = window.after(3000, flip_card)


# Function to flip the card and display the English translation
def flip_card():
    displayed_word = (canvas.itemcget(word, 'text'))
    english_word = word_csv.loc[word_csv['French'] == displayed_word, 'English'].values[0]
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfigure(title, text="English", fill='white')
    canvas.itemconfigure(word, text=f"{english_word}", fill='white')


# Function to update the CSV file after a correct guess
def update_csv():
    global random_word, french_word_list, word_csv
    french_word_list.remove(random_word)
    word_csv = word_csv.drop(word_csv[word_csv['French'] == random_word].index)
    word_csv.to_csv("./data/edited_french_words.csv", index=False)
    print(len(word_csv.index))
    generate_word(canvas)


# Set up the timer to automatically flip the card after 3 seconds
window_timer = window.after(3000, flip_card)

# Create Image files using PhotoImage
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

# Create a canvas for the flashcards
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# Buttons for right and wrong answers
right_button = Button(image=right, highlightthickness=0, command=update_csv)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong, highlightthickness=0, command=lambda: generate_word(canvas))
wrong_button.grid(column=0, row=1)

# Generate the initial word on the canvas
generate_word(canvas)

# Start the Tkinter event loop
window.mainloop()
