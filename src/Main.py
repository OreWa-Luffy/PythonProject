import tkinter as tk
from tkinter import *
import time


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


# Multiply method.
def multiply():
    multi1 = int(Submit1.get())
    multi2 = int(Submit2.get())
    multiTotal = multi1 * multi2
    label.config(text=multiTotal)


# Divide method.
def divide():
    divide1 = int(Submit1.get())
    divide2 = int(Submit2.get())
    divideTotal = divide1 / divide2
    label.config(text=divideTotal)


def clear():
    Submit1.delete(0, END)
    Submit2.delete(0, END)
    validate_and_enable_button()


# Validates whether the button can be pressed if both numbers are filled.
def validate_and_enable_button(*args):
    if Submit1.get() and Submit2.get():
        if Submit1.get().isdigit() and Submit2.get().isdigit():
            addButton.config(state=NORMAL)
            subButton.config(state=NORMAL)
            multiButton.config(state=NORMAL)
            divideButton.config(state=NORMAL)
        else:
            addButton.config(state=tk.DISABLED)
            subButton.config(state=tk.DISABLED)
            multiButton.config(state=tk.DISABLED)
            divideButton.config(state=tk.DISABLED)
    else:
        addButton.config(state=tk.DISABLED)
        subButton.config(state=tk.DISABLED)
        multiButton.config(state=tk.DISABLED)
        divideButton.config(state=tk.DISABLED)


# GUI things.
m = tk.Tk()
m.title("Calculator")
m.geometry("360x150")
icon_path = "C:/Users/baydr/Pictures/Uni/redstone.png"

# Attempts to apply image to icon photo.
try:
    icon_image = tk.PhotoImage(file=icon_path)

    m.iconphoto(False, icon_image)

except Exception as e:
    print("Error with file path.", e)

# Timer stuff

m.start_time = time.time()

m.timer_label = tk.Label(m, text="Timer: 0 seconds", font=14)
m.timer_label.grid(row=6, column=0, columnspan=2)


def clock():
    hour = time.strftime("%H", time.localtime())
    minute = time.strftime("%M", time.localtime())
    second = time.strftime("%S", time.localtime())


# Label stuff
label = Label(m, text="Welcome to calculator")
label.grid(row=0, column=0, columnspan=2)

# AddButton stuff
addButton = tk.Button(m, text="ADD", width=25, command=Add, state=DISABLED, activebackground="Green")
addButton.grid(row=1, column=0)
# SubButton stuff
subButton = tk.Button(m, text="SUBTRACT", width=25, command=subTract, state=DISABLED, activebackground="Green")
subButton.grid(row=1, column=1)
# MultiButton stuff
multiButton = tk.Button(m, text="MULTIPLY", width=25, command=multiply, state=DISABLED, activebackground="Green")
multiButton.grid(row=2, column=0)
# DivideButton stuff
divideButton = tk.Button(m, text="DIVIDE", width=25, command=divide, state=DISABLED, activebackground="Green")
divideButton.grid(row=2, column=1)

validate_cmd = m.register(validate_input)

# Label stuff
Submit1 = Entry(m, width=25, validate="key", validatecommand=(validate_cmd, '%P'))
Submit1.grid(row=3, column=0, columnspan=2)
Submit2 = Entry(m, width=25, validate="key", validatecommand=(validate_cmd, '%P'))
Submit2.grid(row=4, column=0, columnspan=2)

# ClearButton stuff
clearButton = tk.Button(m, text="CLEAR", width=15, command=clear, activebackground="Red")
clearButton.grid(row=5, column=0, columnspan=2)

# Binding the validate_and_enable_button function to any change in the Entry fields

Submit1.bind("<KeyRelease>", validate_and_enable_button)
Submit2.bind("<KeyRelease>", validate_and_enable_button)

m.mainloop()
