# by Xander Eagle
# November 21, 2019
# this program creates a usable calculator

from tkinter import *

root = Tk()


def add_seven():
    result = entry_value.get()
    result += "7"
    entry_value.set(result)


def add_eight():
    result = entry_value.get()
    result += "8"
    entry_value.set(result)


def add_nine():
    result = entry_value.get()
    result += "9"
    entry_value.set(result)


def add_four():
    result = entry_value.get()
    result += "4"
    entry_value.set(result)


def add_five():
    result = entry_value.get()
    result += "5"
    entry_value.set(result)


def add_six():
    result = entry_value.get()
    result += "6"
    entry_value.set(result)


def add_one():
    result = entry_value.get()
    result += "1"
    entry_value.set(result)


def add_two():
    result = entry_value.get()
    result += "2"
    entry_value.set(result)


def add_three():
    result = entry_value.get()
    result += "3"
    entry_value.set(result)


def add_zero():
    result = entry_value.get()
    result += "0"
    entry_value.set(result)


def add_decimal():
    result = entry_value.get()
    result += "."
    entry_value.set(result)


def add_equals():
    result = entry_value.get()
    result = eval(result)
    entry_value.set(result)


def add_plus_minus():
    result = entry_value.get()
    result += "-"
    entry_value.set(result)


def add_divide():
    result = entry_value.get()
    result += "/"
    entry_value.set(result)


def add_multiply():
    result = entry_value.get()
    result += "*"
    entry_value.set(result)


def add_subtract():
    result = entry_value.get()
    result += "-"
    entry_value.set(result)


def add_add():
    result = entry_value.get()
    result += "+"
    entry_value.set(result)


def add_clear():
    entry_value.set("")


entry_value = StringVar()
entry_button = Entry(root, text="", textvariable=entry_value, justify="right", font="Optima 24", width=24)
entry_button.grid(row=1, column=1, columnspan=4)

clear_button = Button(root, text="C", command=add_clear, font="Optima 24", width=12)
clear_button.grid(row=2, column=1, columnspan=2)

negative_button = Button(root, text="+/-", command=add_plus_minus, font="Optima 24", width=6)
negative_button.grid(row=2, column=3)

divide_button = Button(root, text="÷", command=add_divide, font="Optima 24", width=6)
divide_button.grid(row=2, column=4)

seven_button = Button(root, text="7", command=add_seven, font="Optima 24", width=6)
seven_button.grid(row=3, column=1)

eight_button = Button(root, text="8", command=add_eight, font="Optima 24", width=6)
eight_button.grid(row=3, column=2)

nine_button = Button(root, text="9", command=add_nine, font="Optima 24", width=6)
nine_button.grid(row=3, column=3)

multiply_button = Button(root, text="X", command=add_multiply, font="Optima 24", width=6)
multiply_button.grid(row=3, column=4)

four_button = Button(root, text="4", command=add_four, font="Optima 24", width=6)
four_button.grid(row=4, column=1)

five_button = Button(root, text="5", command=add_five, font="Optima 24", width=6)
five_button.grid(row=4, column=2)

six_button = Button(root, text="6", command=add_six, font="Optima 24", width=6)
six_button.grid(row=4, column=3)

subtract_button = Button(root, text="–", command=add_subtract, font="Optima 24", width=6)
subtract_button.grid(row=4, column=4)

one_button = Button(root, text="1", command=add_one, font="Optima 24", width=6)
one_button.grid(row=5, column=1)

two_button = Button(root, text="2", command=add_two, font="Optima 24", width=6)
two_button.grid(row=5, column=2)

three_button = Button(root, text="3", command=add_three, font="Optima 24", width=6)
three_button.grid(row=5, column=3)

addition_button = Button(root, text="+", command=add_add, font="Optima 24", width=6)
addition_button.grid(row=5, column=4)

zero_button = Button(root, text="0", command=add_zero, font="Optima 24", width=6)
zero_button.grid(row=6, column=1)

decimal_button = Button(root, text=".", command=add_decimal, font="Optima 24", width=6)
decimal_button.grid(row=6, column=2)

equals_button = Button(root, text="=", command=add_equals, width=12, font="Optima 24")
equals_button.grid(row=6, column=3, columnspan=4)

root.mainloop()
