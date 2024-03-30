import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor


# Function defs.


# Is_drawing, prev_x and prev_y are all global variables the previous x and y to the event's x and y means it follows the mouse cursor's postion
def start_drawing(event):
    global is_drawing, prev_x, prev_y
    is_drawing = True
    prev_x, prev_y = event.x, event.y

# if drawing is true, it uses the current x and y pos of the cursor for creating a line in the canvas.
def draw(event):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill=drawing_color, width=line_width, capstyle=ROUND,
                           smooth=True)
        prev_x, prev_y = current_x, current_y


# stops drawing and sets is_drawing to false
def stop_drawing(event):
    global is_drawing
    is_drawing = False

# uses the built-in tk module to change color.
def change_pen_color():
    global drawing_color
    color = askcolor()[1]
    if color:
        drawing_color = color

# changes the width of the line
def change_line_width(value):
    global line_width
    line_width = int(value)


def destroy():
    root.destroy()


# GUI Stuff.


root = tk.Tk()
root.title("Whiteboard")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=BOTH, expand=True)

is_drawing = False
drawing_color = "black"
line_width = 2

root.geometry("800x800")

controls_frame = tk.Frame(root)
controls_frame.pack(side="top", fill="x")
controls_frame.config(bg="gray")

color_button = tk.Button(controls_frame, text="Change color", command=change_pen_color, bg="gray")
clear_button = tk.Button(controls_frame, text="Clear", command=lambda: [canvas.delete("all")], bg="gray")

color_button.pack(side="left", padx=5, pady=5)
clear_button.pack(side="left", padx=5, pady=5)

line_width_label = tk.Label(controls_frame, text="Line width: ")
line_width_label.pack(side="left", padx=5, pady=5)

line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient=tk.HORIZONTAL,
                             command=lambda val: change_line_width(val))
line_width_slider.set(line_width)
line_width_slider.pack(side="left", padx=5, pady=5)

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

root.mainloop()
