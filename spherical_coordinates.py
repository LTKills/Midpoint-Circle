import math

import usefull

def spherical_coordinates(window, img, radius, color):
    for theta in range(45, 90):
        x = radius*math.cos(math.radians(theta))
        y = radius*math.sin(math.radians(-theta))

        usefull.write_pixel(img, int(x), int(y), color)

    window.update()
