from tkinter import *


def calculate():
    miles = float(miles_input.get())
    kilometers = round(miles * 1.609)
    kilometer_result.config(text=f"{kilometers}")

window = Tk()
window.title("Miles To Kilometer Converter")
window.config(padx=20, pady=10)

is_equal_label = Label(text="is equal to",font=("Arial",20))
is_equal_label.grid(row=1, column=1)

miles_label = Label(text="miles",font=("Arial",20))
miles_label.grid(row=0, column=3)

kilometer_label = Label(text="km",font=("Arial",20))
kilometer_label.grid(row=1, column=3)

kilometer_result = Label(text="0",font=("Arial",20))
kilometer_result.grid(row=1, column=2)

miles_input = Entry(width=6)
miles_input.grid(row=0, column=2)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=2)

window.mainloop()