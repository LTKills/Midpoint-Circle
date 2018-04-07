from tkinter import mainloop
import math

import usefull
import mid_point

def spherical_coordinates(window, img, radius):
    x0 = usefull.WIDTH/2
    y0 = usefull.HEIGHT/2

    for theta in range(45, 90):
        z = x0 + radius*math.cos(math.radians(theta))
        w1 = y0 + radius*math.sin(math.radians(theta))
        w2 = y0 + radius*math.sin(math.radians(-theta))

        # Draw under and above x-changed (or z) axis
        #img.put("#ffffff", (int(z), int(w1)))
        #img.put("#ffffff", (int(z), int(w2)))
        #img.put("#ffffff", (int(z), int(w1)))
        mid_point.write_pixel(img, int(z), int(w1))
        

    window.update()
