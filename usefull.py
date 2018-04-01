from tkinter import Tk, Canvas, PhotoImage

WIDTH, HEIGHT = 640, 640
backgroud_color = "#000000"

def get_img(name):
    window = Tk()
    window.title(name)
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg=backgroud_color)
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    return img
