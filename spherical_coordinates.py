from tkinter import Tk, Canvas, PhotoImage, mainloop
import math


def spherical_coordinates(repetitions, radius):
    WIDTH, HEIGHT = 640, 640
    x0 = WIDTH/2
    y0 = HEIGHT/2

    window = Tk()
    window.title('Spherical')
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

    for theta in range(180):

        z = x0 + radius*math.cos(math.radians(theta))
        w1 = y0 + radius*math.sin(math.radians(theta))
        w2 = y0 + radius*math.sin(math.radians(-theta))

        # Draw under and above x-changed (or z) axis
        img.put("#ffffff", (int(z), int(w1)))
        img.put("#ffffff", (int(z), int(w2)))

    mainloop()
