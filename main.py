from sys import argv
from time import process_time

from usefull import WIDTH, HEIGHT
from mid_point import mid_point
from spherical_coordinates import spherical_coordinates
from traditional import traditional


def main():
    if len(argv) != 2:
        print("Wrong usage! Correct usage is:")
        print("python3 main.py <RAIO>")
        exit(1)
    radius = int(argv[1])
    if not 0 < radius < min(WIDTH, HEIGHT)/2:
        print("Radius too small, aborting program!")
        exit(1)

    # Draw circle for each different algorithm
    mid_point(radius)
    spherical_coordinates(radius)
    traditional(radius)


if __name__ == "__main__":
    main()
