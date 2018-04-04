from sys import argv
from tkinter import mainloop

import usefull

def main():
    # Check if program usage is correct
    if len(argv) != 2:
        print("Wrong usage! Correct usage is:")
        print("python3 main.py <RAIO>")
        exit(1)

    # Check if valid radius value
    radius = int(argv[1])
    if not 0 < radius < (min(usefull.WIDTH, usefull.HEIGHT)/2)-5:
        print("Radius too small, aborting program!")
        exit(1)

    root = usefull.create_root_window()

    # Due to the python garbage collector, it is necessary to keep the window
    #   and img in memory after the foop loop
    windows = []

    # Draw circle for each different algorithm
    for name, function in usefull.FUNCTIONS.items():
        window, img = usefull.get_img(root, name)
        windows.append((window, img))
        function(window, img, radius)

    usefull.exit_window(root)
    mainloop()

if __name__ == "__main__":
    main()
