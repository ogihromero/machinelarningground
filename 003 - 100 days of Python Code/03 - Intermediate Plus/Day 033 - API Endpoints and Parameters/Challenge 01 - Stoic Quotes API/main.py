from tkinter import Tk, Canvas, PhotoImage, Button
from os import path
import requests


def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


def get_quote():
    response = requests.get("https://api.themotivate365.com/stoic-quote")
    response.raise_for_status()
    api_quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=api_quote)


window = Tk()
window.title("Stoic Quote")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=dir("background.png"))
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="",
    width=250,
    font=("Arial", 14, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=dir("book_icon.png"))
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()
window.mainloop()
