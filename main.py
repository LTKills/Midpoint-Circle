from sys import argv
from time import process_time


from mid_point import mid_point
from spherical_coordinates import spherical_coordinates
from traditional import traditional


def main():
    if len(argv) != 2:
        print("Wrong usage! Correct usage is:")
        print("python3 main.py <RAIO>")
        exit(1)
    radius = int(argv[1])
    repetitions = 100

    mid_point(radius)
    spherical_coordinates(radius)
    traditional(radius)


if __name__ == "__main__":
    main()
