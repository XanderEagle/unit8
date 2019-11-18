from tkinter import *

root = Tk()
root.title("Name")

titleName = Entry(root)
titleName.grid(row=1, column=1)

response = Label(root, text="Hello,")
response.grid(row=2, column=1)

button = Button(root, text="Say Hello")
button.grid(row=3, column=1)

root.mainloop()
