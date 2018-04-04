from time import process_time
from tkinter import mainloop

import usefull

def test_all(repetitions, radius):
    root = usefull.create_root_window()

    # Due to the python garbage collector, it is necessary to keep the window
    #   and img in memory after the foop loop
    windows = []

    times = {}
    for name, function in usefull.FUNCTIONS.items():
        start = process_time()
        #Create window and draw circle
        window, img = usefull.get_img(root, name)
        windows.append((window, img))
        for _ in range(repetitions):
            function(window, img, radius + _)

        # Store total total time and update window
        times[name] = process_time()-start
        window.update()

    # For the garbage collector again
    labels = usefull.exit_window(root, print_times=True, times=times)
    mainloop()

if __name__ == "__main__":
    test_all(10, 100)
