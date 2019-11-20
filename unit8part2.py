from tkinter import *
import random

root = Tk()

roll_value = IntVar()

def equals():
    max = side_choice.get()
    roll = random.randint(1, max)
    roll_value.set(roll)
    side_choice.set(20)

seven_button = Button(root, text="7", value=7)
seven_button.grid(row=1, column=1, sticky="w")

six_sided = Radiobutton(root, text="6-sided", value=6)
six_sided.grid(row=3, column=1, sticky="w")

eight_sided = Radiobutton(root, text="8-sided", value=8)
eight_sided.grid(row=4, column=1, sticky="w")

ten_sided = Radiobutton(root, text="10-sided", value=10)
ten_sided.grid(row=5, column=1, sticky="w")

twenty_sided = Radiobutton(root, text="20-sided", value=20)
twenty_sided.grid(row=6, column=1, sticky="w")

equals_button = Button(root, text="Roll die", command=equals)
equals_button.grid(row=7, column=1)

equals_result = Label(root, text="0", textvariable=roll_value, font="Helvetica 32")
equals_result.grid(row=8, column=8, sticky="w")

root.mainloop()
