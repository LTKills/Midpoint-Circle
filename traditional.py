from tkinter import Tk, Canvas, PhotoImage, mainloop
import math


def traditional(repetitions, radius):
    WIDTH, HEIGHT = 640, 640

    window = Tk()
    window.title('Traditional')
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

    for x in range(-radius, radius):

        # Changing coordinates as origin is at bottom left of sceen
        z = int(x + WIDTH/2)
        w = math.sqrt(abs(x**2 - radius**2))

        # Draw under and above x-changed (or z) axis
        img.put("#ffffff", (z, int(HEIGHT/2 + w)))
        img.put("#ffffff", (z, int(HEIGHT/2 - w)))

    mainloop()
