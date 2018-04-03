from tkinter import mainloop
import math

import usefull

def spherical_coordinates(img, radius):
    x0 = usefull.WIDTH/2
    y0 = usefull.HEIGHT/2

    for theta in range(180):
        z = x0 + radius*math.cos(math.radians(theta))
        w1 = y0 + radius*math.sin(math.radians(theta))
        w2 = y0 + radius*math.sin(math.radians(-theta))

        # Draw under and above x-changed (or z) axis
        img.put("#ffffff", (int(z), int(w1)))
        img.put("#ffffff", (int(z), int(w2)))

    mainloop()
