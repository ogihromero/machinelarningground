from os import path
from tkinter import (
    messagebox,
    END,
    Tk,
    Label,
    Entry,
    PhotoImage,
    Canvas,
    Button,
)
from random import choice, randint, shuffle
import pyperclip
import json


# ----------------------------DIRECTORY FUNCTION --------------------------- #
def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


# ---------------------------- PASSWORD GENERATOR --------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {"username": username, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you haven't left any fields empty.",
        )
    else:
        try:
            with open(dir("data.json"), "r") as data_file:
                try:
                    data = json.load(data_file)
                except json.decoder.JSONDecodeError:
                    # When the file is empty, just create the emptydict
                    data = {}
                data.update(new_data)
        except FileNotFoundError:
            # Creates file and saves data if didn't exist
            with open(dir("data.json"), "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open(dir("data.json"), "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------------SEARCH PASSWORD------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open(dir("data.json"), "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website,
                message=f"Username: {username}\nPassword: {password}",
            )
            pyperclip.copy(password)
        else:
            messagebox.showinfo(
                title="Error", message=f"No entry for {website}"
            )
    finally:
        pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo_img = PhotoImage(file=dir("logo.png"))
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "test@example.com")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)


# Buttons
generate_button = Button(text="Generate Password", command=generate, width=15)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save, width=50)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search_password, width=15)
search_button.grid(row=1, column=2)


window.mainloop()
