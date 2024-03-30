# Going to be added to main. Just establishes main menu

import tkinter as tk
from tkinter import *
import time
import os
import subprocess
import sys

# setting up file paths.

GUI_Calculator = '/PythonProjects/src/Calculator.py'

args = '"%s" "%s"' % (sys.executable, GUI_Calculator)


def openfile():
    proc = subprocess.run(args)


def closeMenu():
    mainMenu.destroy()


mainMenu = tk.Tk()
mainMenu.title("Main menu")
mainMenu.geometry("400x200")
welcomeLabel = Label(mainMenu, text="Welcome to the main menu. Please select from the following options")
welcomeLabel.grid(row=0, column=0)
openCalculatorButton = Button(mainMenu, text="Open Calculator", command=lambda: [closeMenu(), openfile()])
openCalculatorButton.grid(row=1, column=1)
mainMenu.mainloop()
