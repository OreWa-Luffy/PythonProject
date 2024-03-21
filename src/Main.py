import tkinter as tk
from tkinter import *


def backToMenu():
    print("Back to menu")
    menu()


def menu():
    print("Welcome to the menu")

    print("Please choose from the following")

    print("1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Exit")

    choice = input("")
    if choice == "1":
        add = input("Enter the first")
        add = int(add)
        add2 = input("Enter the second")
        add2 = int(add2)
        total = add + add2
        print(total)
        backToMenu()


    elif choice == "2":
        sub = input("Enter the first number")
        sub = int(sub)
        sub2 = input("Enter the second number")
        sub2 = int(sub2)
        total = sub - sub2
        print(total)
        backToMenu()

    elif choice == 3:
        multi = input("Enter the first number")
        multi = int()
        multi2 = input("Enter the second number")
        multi2 = int(multi2)
        total = multi * multi2
        print(total)
        backToMenu()

    elif choice == 4:
        divide = input("Enter the first number")
        divide = int()
        divide2 = input("Enter the second number")
        divide2 = int(divide2)
        total = divide / divide2
        print(total)
        backToMenu()

    elif choice == 5:
        print("Goodbye")


# menu()


m = tk.Tk()
m.title("Calculator")
label = Label(m, text="Welcome to calculator")
label.pack()
button = tk.Button(m, text="ADD", width=25, command=m.destroy)
button.pack()
m.mainloop()
