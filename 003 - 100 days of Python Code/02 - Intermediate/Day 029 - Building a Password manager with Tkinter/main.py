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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you haven't left any fields empty.",
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nUsername {username} "
            f"\nPassword: {password} \nIs it ok to save?",
        )
        if is_ok:
            with open(dir("data.txt"), "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


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
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "test@example.com")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)


# Buttons
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save, width=44)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
