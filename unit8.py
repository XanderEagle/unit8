from tkinter import *

root = Tk()

entry_button = Entry(root, text="")
entry_button.grid(row=1, column=1, columnspan=4)

clear_button = Button(root, text="C")
clear_button.grid(row=2, column=1, columnspan=2)

negative_button = Button(root, text="+/-")
negative_button.grid(row=2, column=3)

divide_button = Button(root, text="÷")
divide_button.grid(row=2, column=4)

seven_button = Button(root, text="7")
seven_button.grid(row=3, column=1)

eight_button = Button(root, text="8")
eight_button.grid(row=3, column=2)

nine_button = Button(root, text="9")
nine_button.grid(row=3, column=3)

multiply_button = Button(root, text="X")
multiply_button.grid(row=3, column=4)

four_button = Button(root, text="4")
four_button.grid(row=4, column=1)

five_button = Button(root, text="5")
five_button.grid(row=4, column=2)

six_button = Button(root, text="6")
six_button.grid(row=4, column=3)

subtract_button = Button(root, text="–")
subtract_button.grid(row=4, column=4)

one_button = Button(root, text="1")
one_button.grid(row=5, column=1)

two_button = Button(root, text="2")
two_button.grid(row=5, column=2)

three_button = Button(root, text="3")
three_button.grid(row=5, column=3)

addition_button = Button(root, text="+")
addition_button.grid(row=5, column=4)

zero_button = Button(root, text="0")
zero_button.grid(row=6, column=1)

decimal_button = Button(root, text=".")
decimal_button.grid(row=6, column=2)

equals_button = Button(root, text="=")
equals_button.grid(row=6, column=3, columnspan=4)

root.mainloop()
