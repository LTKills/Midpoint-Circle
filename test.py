from time import process_time
from tkinter import mainloop

import usefull

def test_all(repetitions, max_radius):
    # Makes sure radius size is big enough
    if max_radius < 100:
        print("Radius too small for usefull testing conditions, please use " +
              "a bigger radius.")
        exit(1)
 
    # Makes sure we are running enough repetitions
    if repetitions < 100:
        print("Less than 100 repetitions is not statisticly significant." +
              "Please run with more repetitions.")
        exit(1)

    step = int(max_radius/10)

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

        # For 10 different significant values in radius size, run each algorithm
        #   "repetitions" (100 by default) times
        for rep in range(repetitions):
            for multi in range(1, 11):
                function(window, img, multi*step, usefull.COLORS[
                    int(rep*multi % 11)])

        # Store total total time and update window
        times[name] = process_time()-start
        window.update()

    # For the garbage collector again
    labels = usefull.exit_window(root, print_times=True, times=times)
    mainloop()

if __name__ == "__main__":
    test_all(repetitions=100, max_radius=300)
