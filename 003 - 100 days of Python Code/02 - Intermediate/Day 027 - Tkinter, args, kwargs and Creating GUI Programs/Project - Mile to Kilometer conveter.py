from tkinter import Tk, Entry, Label, Button


def convert():
    miles = float(miles_input.get())
    km_result = miles * 1.609344
    result_label.config(text=f"{km_result:.2f}")


window = Tk()
window.title("Mile to Kilometer")
window.config(padx=20, pady=20)

# Miles_Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)


# Equal Label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)


# Result label
result_label = Label(text="0")
result_label.grid(column=1, row=1)


# Km Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)


# Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)


window.mainloop()
