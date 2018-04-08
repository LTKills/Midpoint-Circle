import math

import usefull

def traditional(window, img, radius, color):
    # Since we are only worried with the second octant, we only need to draw
    #   until the 45 degree angle hits the circle, which happens for
    #   x = 0.5*sqrt(2)*radius
    end_x = int(0.5*math.sqrt(2)*radius) + 1

    for x in range(0, end_x):
        y = int(math.sqrt(abs(x**2 - radius**2)))
        usefull.write_pixel(img, x, y, color)

    window.update()
