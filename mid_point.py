from tkinter import Tk, Canvas, PhotoImage, mainloop

WIDTH, HEIGHT = 640, 640


def write_pixel(img, x, y):
    z = int(WIDTH/2)
    w = int(HEIGHT/2)

    img.put("#ffffff", (z + x, w + y))
    img.put("#ffffff", (z + x, w - y))
    img.put("#ffffff", (z - x, w + y))
    img.put("#ffffff", (z - x, w - y))
    img.put("#ffffff", (z + y, w + x))
    img.put("#ffffff", (z + y, w - x))
    img.put("#ffffff", (z - y, w + x))
    img.put("#ffffff", (z - y, w - x))


def mid_point(repetitions, radius):
    x = 0
    y = radius
    d = 1 - radius

    window = Tk()
    window.title('Mid Point')
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

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

    mainloop()
