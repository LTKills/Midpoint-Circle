from sys import argv
from time import process_time

# from usefull import WIDTH, HEIGHT, FUNCTIONS, get_img
import usefull
print(usefull.WIDTH)

def main():
    if len(argv) != 2:
        print("Wrong usage! Correct usage is:")
        print("python3 main.py <RAIO>")
        exit(1)

    radius = int(argv[1])
    if not 0 < radius < (min(WIDTH, HEIGHT)/2)-5:
        print("Radius too small, aborting program!")
        exit(1)

    # Draw circle for each different algorithm
    for name, function in FUNCTIONS.items():
        img = get_img(name)
        function(img, radius)

if __name__ == "__main__":
    main()
