from tkinter import Tk, Canvas, PhotoImage

WIDTH, HEIGHT = 640, 640
backgroud_color = "#000000"

def get_img(name, auto_delete, auto_time):
    window = Tk()
    # If choosen, auto delete the window after auto_time microseconds
    if auto_delete:
        window.withdraw() # window.after(auto_time, lambda: window.destroy())
    window.title(name)
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg=backgroud_color)
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    return img
