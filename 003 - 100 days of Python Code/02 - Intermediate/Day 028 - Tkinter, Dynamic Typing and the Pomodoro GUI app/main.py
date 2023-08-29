from tkinter import Tk, PhotoImage, Canvas, Label, Button
from os import path
import math


# ----------------------------DIRECTORY FUNCTION --------------------------- #
def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


# ---------------------------- CONSTANTS and Global-------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset(item):
    window.after_cancel(timer)
    canvas.itemconfig(item, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    streak_label.config(text="")
    global reps
    reps = 0
    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM
def start_timer():
    start_button.config(state="disabled")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ---------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_id, text=f"{count_min}:{count_sec:02}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        streak = ""
        for _ in range(reps // 2):
            streak += "✔"
        streak_label.config(text=streak)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file=dir("tomato.png"))
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_id = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)
# count_down(5000, timer)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)


# button = Button(text="Calculate", command=convert)
# button.grid(column=1, row=2)
# buttons
start_button = Button(
    text="Start", bg="white", highlightthickness=0, command=start_timer
)
start_button.grid(column=0, row=2)

reset_button = Button(
    text="Reset",
    bg="white",
    highlightthickness=0,
    command=lambda: reset(timer_id),
)
reset_button.grid(column=2, row=2)

# streak_label
streak_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
streak_label.grid(column=1, row=3)

window.mainloop()
