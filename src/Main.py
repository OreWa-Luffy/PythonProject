import tkinter as tk
from tkinter import *


# Now moved to GUI #


def validate_input(new_value):
    if new_value == '':
        return True
    try:
        int(new_value)
        return True
    except ValueError:
        return False


def Add():
    add1 = int(Submit1.get())
    add2 = int(Submit2.get())
    total = add1 + add2
    label.config(text=total)


def subTract():
    sub1 = int(Submit1.get())
    sub2 = int(Submit2.get())
    subtotal = sub1 - sub2
    label.config(text=subtotal)


def validate_and_enable_button(*args):
    if Submit1.get() and Submit2.get():
        if Submit1.get().isdigit() and Submit2.get().isdigit():
            button.config(state=NORMAL)
        else:
            button.config(state=tk.DISABLED)
    else:
        button.config(state=tk.DISABLED)


# GUI things.
m = tk.Tk()
m.title("Calculator")
label = Label(m, text="Welcome to calculator")
label.pack()
button = tk.Button(m, text="ADD", width=25, command=Add, state=DISABLED)
button.pack()
validate_cmd = m.register(validate_input)
Submit1 = Entry(m, width=25, validate="key", validatecommand=(validate_cmd, '%P'))
Submit1.pack()
Submit2 = Entry(m, width=25, validate="key", validatecommand=(validate_cmd, '%P'))
Submit2.pack()


# Binding the validate_and_enable_button function to any change in the Entry fields

Submit1.bind("<KeyRelease>", validate_and_enable_button)
Submit2.bind("<KeyRelease>", validate_and_enable_button)

m.mainloop()
