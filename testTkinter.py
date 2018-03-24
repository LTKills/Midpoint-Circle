from tkinter import *


root = Tk()

w = Canvas(root, width=200, height=200)
root.title('Test TkInter')

coord = 0, 0, 200, 200
circle = w.create_oval(coord, fill='red')


w.pack()

root.mainloop()
