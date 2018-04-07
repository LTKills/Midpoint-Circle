import math

import usefull

def spherical_coordinates(window, img, radius):
    for theta in range(45, 90):
        x = radius*math.cos(math.radians(theta))
        y = radius*math.sin(math.radians(-theta))

        # Draw under and above x-changed (or z) axis
        usefull.write_pixel(img, int(x), int(y))

    window.update()
