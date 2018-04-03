from tkinter import Tk, Canvas, PhotoImage, Toplevel
from collections import OrderedDict

import mid_point
import traditional
import spherical_coordinates

# We use a OrderedDict to garante that the test is always done in the same order
FUNCTIONS = OrderedDict([
    ("Mid Point", mid_point.mid_point),
    ("Spherical Coordinates", spherical_coordinates.spherical_coordinates),
    ("Traditional", traditional.traditional)])

WIDTH, HEIGHT = 640, 640
BACKGROUND_COLOUR = "#000000"

def create_root_window():
    root = Tk()
    root.withdraw()

def get_img(root, name):
    window = Toplevel(root)
    window.title(name)
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOUR)
    canvas.pack()
    img = PhotoImage(master=canvas, width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    return window, img
