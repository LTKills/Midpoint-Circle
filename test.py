from time import process_time
from tkinter import mainloop

import usefull

def test_all(repetitions, max_radius):
    if max_radius < 100:
        print("Radius too small for usefull testing conditions, please use " +
              "a bigger radius")
        exit(1)
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
            for radius in range(int(max_radius/10), max_radius+1, int(max_radius/10)):  
                function(window, img, radius)
            print(_)

        # Store total total time and update window
        times[name] = process_time()-start
        window.update()

    # For the garbage collector again
    labels = usefull.exit_window(root, print_times=True, times=times)
    mainloop()

if __name__ == "__main__":
    test_all(repetitions=10, max_radius=300)
