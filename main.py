from sys import argv
from time import process_time

import usefull

def main():
    if len(argv) != 2:
        print("Wrong usage! Correct usage is:")
        print("python3 main.py <RAIO>")
        exit(1)

    radius = int(argv[1])
    if not 0 < radius < (min(usefull.WIDTH, usefull.HEIGHT)/2)-5:
        print("Radius too small, aborting program!")
        exit(1)

    # Draw circle for each different algorithm
    for name, function in usefull.FUNCTIONS.items():
        img = usefull.get_img(name)
        function(img, radius)

if __name__ == "__main__":
    main()
