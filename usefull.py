from tkinter import Tk, Canvas, PhotoImage
from collections import OrderedDict

import mid_point
# from mid_point import mid_point
from spherical_coordinates import spherical_coordinates
from traditional import traditional

# We use a OrderedDict to garante that the test is always done in the same order
FUNCTIONS = OrderedDict([
    ("Mid Point", mid_point.mid_point),
    ("Spherical Coordinates", spherical_coordinates),
    ("Traditional", traditional)])


WIDTH, HEIGHT = 640, 640
BACKGROUND_COLOUR = "#000000"

def get_img(name):
    window = Tk()

    # temp
    window.withdraw()

    window.title(name)
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOUR)
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    return img
