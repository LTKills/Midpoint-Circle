from time import process_time
from collections import OrderedDict

from mid_point import mid_point
from spherical_coordinates import spherical_coordinates
from traditional import traditional

# We use a OrderedDict to garante that the test is always done in the same order
FUNCTIOS = OrderedDict([
    ("Mid Point", mid_point),
    ("Spherical Coordinates", spherical_coordinates),
    ("Traditional", traditional)])

# This is NOT used in the program currently
WINDOW_TIME = 100 # microseconds

def test_all(repetitions, radius):
    for name, function in FUNCTIOS.items():
        start = process_time()
        for _ in range(repetitions):
            function(radius, auto_delete=True, auto_time=WINDOW_TIME)
        print("Total time for ", name, process_time() - start)

if __name__ == "__main__":
    test_all(50, 300)
