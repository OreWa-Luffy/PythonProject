import tkinter as tk
from tkinter import *


# Now moved to GUI #

# Validates that the input is in int.
def validate_input(new_value):
    if new_value == '':
        return True
    try:
        int(new_value)
        return True
    except ValueError:
        return False


# add method
def Add():
    add1 = int(Submit1.get())
    add2 = int(Submit2.get())
    total = add1 + add2
    label.config(text=total)


# Subtract method
def subTract():
    sub1 = int(Submit1.get())
    sub2 = int(Submit2.get())
    subtotal = sub1 - sub2
    label.config(text=subtotal)


# Validates whether the button can be pressed if both numbers are filled.
def validate_and_enable_button(*args):
    if Submit1.get() and Submit2.get():
        if Submit1.get().isdigit() and Submit2.get().isdigit():
            addButton.config(state=NORMAL)
            subButton.config(state=NORMAL)
        else:
            addButton.config(state=tk.DISABLED)
            subButton.config(state=tk.DISABLED)
    else:
        addButton.config(state=tk.DISABLED)
        subButton.config(state=tk.DISABLED)


# GUI things.
m = tk.Tk()
m.title("Calculator")
label = Label(m, text="Welcome to calculator")
label.pack()

# Button stuff
addButton = tk.Button(m, text="ADD", width=25, command=Add, state=DISABLED)
addButton.pack()
subButton = tk.Button(m, text="SUBTRACT", width=25,command=subTract, state=DISABLED)
subButton.pack()

validate_cmd = m.register(validate_input)

# Label stuff
Submit1 = Entry(m, width=25, validate="key", validatecommand=(validate_cmd, '%P'))
Submit1.pack()
Submit2 = Entry(m, width=25, validate="key", validatecommand=(validate_cmd, '%P'))
Submit2.pack()

# Binding the validate_and_enable_button function to any change in the Entry fields

Submit1.bind("<KeyRelease>", validate_and_enable_button)
Submit2.bind("<KeyRelease>", validate_and_enable_button)

m.mainloop()
