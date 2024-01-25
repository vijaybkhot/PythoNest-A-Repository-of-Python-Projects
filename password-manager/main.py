from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    data = ''
    if len(website.replace(' ', '')) <= 0 or len(password.replace(' ', '')) <= 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            data_file = open("data.json", mode='r')
            # Updating old data with new data
            data = json.load(data_file)
            data.update(new_data)
            data_file.close()
        except FileNotFoundError:
            data_file = open("data.json", mode='w')
            data = new_data
            data_file.close()
        finally:
            # Saving updated data
            data_file = open("data.json", mode='w')
            json.dump(data, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
            data_file.close()


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    website = (website_entry.get()).capitalize()
    try:
        with open("data.json", mode='r') as search_file:
            search_data = json.load(search_file)
            if website in search_data.keys():
                messagebox.showinfo(title=website,
                                    message=f"Email: {search_data[website]['email']}\nPassword: {search_data[website]['password']} ")
                print(search_data[website]['email'])
            else:
                messagebox.showinfo(title="Error",
                                    message=f"Password not saved for {website}.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error",
                            message=f"No Data File found.")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
background_image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=background_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "abc@gmail.com")

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

search_button = Button(text="Search", width=12, command=search_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
