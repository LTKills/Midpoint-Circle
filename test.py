from time import process_time
from collections import OrderedDict

from usefull import FUNCTIONS 

# This is NOT used in the program currently
WINDOW_TIME = 100 # microseconds

def test_all(repetitions, radius):
    for name, function in FUNCTIONS.items():
        start = process_time()
        for _ in range(repetitions):
            function(radius)
        print("Total time for ", name, process_time() - start)

if __name__ == "__main__":
    test_all(50, 300)
