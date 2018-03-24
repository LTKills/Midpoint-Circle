from tkinter import *
from math import sin

WIDTH, HEIGHT = 640, 640

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
window.title('Test Pixels')

canvas.grid()


img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state='normal')


for x in range(WIDTH):
    img.put("#ffffff", (x, int(HEIGHT/2)))
    img.put("#ffffff", (x, 100))

for y in range(HEIGHT):
    img.put("#ffffff", (int(WIDTH/2), y))
    img.put("#ffffff", (100, y))

window.mainloop()
