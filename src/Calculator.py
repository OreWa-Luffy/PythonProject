import tkinter as tk
from tkinter import *
import time
import sys
import os
import subprocess


# Now moved to GUI #


# CALCULATOR FUNCTIONS
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


# GUI SPECIFIC COMMANDS

GUI_MAINMENU = '/PythonProjects/src/MainMenu.py'
args = '"%s" "%s"' % (sys.executable, GUI_MAINMENU)


def destroy():
    calculator.destroy()


def returnToMain():
    proc = subprocess.run(args)


# light and dark mode

def light_dark():
    global switch_value
    if switch_value:
        calculator.configure(bg="darkslategrey")
        addButton.config(fg="white", bg="slategray")
        subButton.config(fg="white", bg="slategray")
        multiButton.config(fg="white", bg="slategray")
        divideButton.config(fg="white", bg="slategray")
        label.config(fg="white", bg="slategray")
        light_darkButton.config(fg="white", bg="slategray")
        clearButton.config(fg="white", bg="slategray")
        Submit1.config(fg="white", bg="slategray")
        Submit2.config(fg="white", bg="slategray")
        light_darkButton.config(text="LIGHT MODE")

        switch_value = False
    else:
        calculator.configure(bg="white")
        addButton.config(fg="black", bg="white")
        subButton.config(fg="black", bg="white")
        multiButton.config(fg="black", bg="white")
        divideButton.config(fg="black", bg="white")
        label.config(fg="black", bg="white")
        light_darkButton.config(fg="black", bg="white")
        clearButton.config(fg="black", bg="white")
        Submit1.config(fg="black", bg="white")
        Submit2.config(fg="black", bg="white")
        light_darkButton.config(text="DARK MODE")
        switch_value = True


# GUI things.
calculator = tk.Tk()
calculator.title("Calculator")
calculator.geometry("450x200")
calculator.resizable(width=False, height=False)
icon_path = "/PythonProjects/Resources/redstone.png"
icon_image = tk.PhotoImage(file=icon_path)
calculator.iconphoto(False, icon_image)
switch_value = True

controlFrame = tk.Frame(calculator)
controlFrame.grid(row=0, column=0)
controlFrame.config(background="gray")

# Timer stuff

calculator.start_time = time.time()
timerLabel = tk.Label(calculator, text="Timer: 0 seconds", font=14, fg="green", background="black", )
timerLabel.grid(row=7, column=0, columnspan=2)


def clock():
    hour = time.strftime("%H", time.localtime())
    minute = time.strftime("%M", time.localtime())
    second = time.strftime("%S", time.localtime())
    digital = time.strftime("%p", time.localtime())
    timerLabel.config(text=hour + ":" + minute + ":" + second + " - " + digital)
    timerLabel.after(1000, clock)


# Label stuff
label = Label(calculator, text="Welcome to calculator")

label.grid(row=0, column=0, columnspan=2)

# AddButton stuff
addButton = tk.Button(calculator, text="ADD", width=25, command=Add, state=DISABLED, activebackground="Green")
addButton.grid(row=1, column=0)
# SubButton stuff
subButton = tk.Button(calculator, text="SUBTRACT", width=25, command=subTract, state=DISABLED, activebackground="Green")
subButton.grid(row=1, column=1)
# MultiButton stuff
multiButton = tk.Button(calculator, text="MULTIPLY", width=25, command=multiply, state=DISABLED, activebackground="Green")
multiButton.grid(row=2, column=0)
# DivideButton stuff
divideButton = tk.Button(calculator, text="DIVIDE", width=25, command=divide, state=DISABLED, activebackground="Green")
divideButton.grid(row=2, column=1)
# light/dark mode button
light_darkButton = tk.Button(calculator, text="DARK MODE", command=light_dark)
light_darkButton.grid(row=6, column=1)
# Return to main menu button
mainMenu_button = tk.Button(calculator, text="Return to main menu", width=25, command=lambda: [destroy(), returnToMain()])
mainMenu_button.grid(row=8, column=0, columnspan=2)

validate_cmd = calculator.register(validate_input)

# Label stuff
Submit1 = Entry(calculator, width=25, validate="key", validatecommand=(validate_cmd, '%P'))
Submit1.grid(row=3, column=0, columnspan=2)
Submit2 = Entry(calculator, width=25, validate="key", validatecommand=(validate_cmd, '%P'))
Submit2.grid(row=4, column=0, columnspan=2)

# ClearButton stuff
clearButton = tk.Button(calculator, text="CLEAR", width=15, command=clear, activebackground="Red")
clearButton.grid(row=6, column=0)

# Binding the validate_and_enable_button function to any change in the Entry fields

Submit1.bind("<KeyRelease>", validate_and_enable_button)
Submit2.bind("<KeyRelease>", validate_and_enable_button)

clock()
calculator.mainloop()
