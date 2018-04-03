from time import process_time
from collections import OrderedDict
from tkinter import Tk, mainloop

import usefull

def test_all(repetitions, radius):
    root = Tk()
    root.withdraw()
   
    windows = []
    for name, function in usefull.FUNCTIONS.items():
        start = process_time()
        window, img = usefull.get_img(root, name)
        windows.append((window, img))
        for _ in range(repetitions):
            function(window, img, radius + _)
        print("Total time for ", name, process_time() - start)
        window.update()

    root.deiconify()
    mainloop()

if __name__ == "__main__":
    test_all(100, 100)
