import tkinter as tk
from tkinter import *


# Now moved to GUI #

def Add():
    add1 = int(Submit1.get())
    add2 = int(Submit2.get())
    total = add1 + add2
    label.config(text=total)
    button.config(state=DISABLED)


# GUI things.
m = tk.Tk()
m.title("Calculator")
label = Label(m, text="Welcome to calculator")
label.pack()
button = tk.Button(m, text="ADD", width=25, command=Add)
button.pack()
Submit1 = Entry(m, width=25)
Submit1.pack()
Submit2 = Entry(m, width=25)
Submit2.pack()

m.mainloop()
