from tkinter import *#mainloop, update

import usefull

def write_pixel(img, x, y):
    z = int(usefull.WIDTH/2)
    w = int(usefull.HEIGHT/2)

    img.put("#ffffff", (z + x, w + y))
    img.put("#ffffff", (z + x, w - y))
    img.put("#ffffff", (z - x, w + y))
    img.put("#ffffff", (z - x, w - y))
    img.put("#ffffff", (z + y, w + x))
    img.put("#ffffff", (z + y, w - x))
    img.put("#ffffff", (z - y, w + x))
    img.put("#ffffff", (z - y, w - x))


def mid_point(window, img, radius):
    x = 0
    y = radius
    d = 1 - radius
    write_pixel(img, x, y)
    while y > x:
        if d < 0:
            d = d + 2 * x + 3
            x += 1
        else:
            d = d + 2 * (x - y) + 5
            x += 1
            y -= 1
        write_pixel(img, x, y)

    window.update()
