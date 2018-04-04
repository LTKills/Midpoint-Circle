from tkinter import Tk, Canvas, PhotoImage, Frame, Button, Label, Toplevel
from collections import OrderedDict

import mid_point
import traditional
import spherical_coordinates

# We use a OrderedDict to garante that the test is always done in the same order
FUNCTIONS = OrderedDict([
    ("Mid Point", mid_point.mid_point),
    ("Spherical Coordinates", spherical_coordinates.spherical_coordinates),
    ("Traditional", traditional.traditional)])

# Some default values
WIDTH, HEIGHT = 640, 640
BACKGROUND_COLOUR = "#000000"

# Close a window
def close_window(window):
    window.destroy()

# Creates the main GUI window and imediatelly hides it
def create_root_window():
    root = Tk()
    root.withdraw()
    return root

# Creates a window with a canvas and a image to be drawn on
def get_img(root, name):
    window = Toplevel(root)
    window.title(name)
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOUR)
    canvas.pack()
    img = PhotoImage(master=canvas, width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    return window, img

# Exits a window, killing the program. If print_times is True, it also
#   prints the results of drawing the circle
def exit_window(root, print_times=False, times=None):
    root.deiconify()
    frame = Frame(root)
    frame.pack()
    button = Button(frame, text="Exit", command=lambda: close_window(root))
    button.pack()

    if print_times:
        labels = []
        for name, time in times.items():
            label = Label(frame, text=name + ": " + str(time))
            label.pack()
            labels.append(label)
        return labels
    return None
