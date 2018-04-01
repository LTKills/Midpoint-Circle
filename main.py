from sys import argv
from time import process_time
from tkinter import Tk, Canvas, PhotoImage
import math


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

    mid_point(repetitions, radius)
    spherical_coordinates(repetitions, radius)
    traditional(repetitions, radius)

if __name__ == "__main__":
    main()
