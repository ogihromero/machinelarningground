from os import path
from tkinter import Button, Tk, PhotoImage, Canvas
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


# Current directory file path function
def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


# Reading data
current_card: list[dict] = []
try:
    data = pandas.read_csv(dir("./data/learned_words.csv"))
    learned_words = data.to_dict(orient="records")
except FileNotFoundError:
    learned_words = []
data = pandas.read_csv(dir("./data/french_words.csv"))
data_list = data.to_dict(orient="records")
# recorded_words = []
switch_timer = None


# Functions
def change_word(remove):
    global switch_timer, current_card
    if remove:
        learned_words.append(current_card)
        data_list.remove(current_card)
        saved_data = pandas.DataFrame(learned_words)
        saved_data.to_csv(dir("./data/learned_words.csv"), index=False)
    window.after_cancel(switch_timer)
    current_card = random.choice(
        [card for card in data_list if card not in learned_words]
    )
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    switch_timer = window.after(3000, change_card)


def change_fr():
    change_word("French")
    canvas.itemconfig(language_label, text="French")


def change_en():
    change_word("English")
    canvas.itemconfig(language_label, text="English")


def change_card():
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


# UI Setup
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
switch_timer = window.after(3000, change_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=dir("./images/card_front.png"))
card_back_img = PhotoImage(file=dir("./images/card_back.png"))
card_bg = canvas.create_image(400, 236, image=card_front_img)
# canvas.create_image(400, 236, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Canvas Text
language_label = canvas.create_text(400, 150, font=LANG_FONT)
word_label = canvas.create_text(400, 263, font=WORD_FONT)

# Buttons
right_img = PhotoImage(file=dir("./images/right.png"))
wrong_img = PhotoImage(file=dir("./images/wrong.png"))

right_button = Button(
    image=right_img,
    bg=BACKGROUND_COLOR,
    border=0,
    command=lambda: change_word(True),
)
right_button.grid(row=1, column=1)

wrong_button = Button(
    image=wrong_img,
    bg=BACKGROUND_COLOR,
    border=0,
    command=lambda: change_word(False),
)
wrong_button.grid(row=1, column=0)

change_word(False)
window.mainloop()
