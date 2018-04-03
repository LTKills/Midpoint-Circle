from tkinter import mainloop
import math

import usefull

def traditional(img, radius):
    for x in range(-radius, radius):

        # Changing coordinates as origin is at bottom left of sceen
        z = int(x + usefull.WIDTH/2)
        w = math.sqrt(abs(x**2 - radius**2))

        # Draw under and above x-changed (or z) axis
        img.put("#ffffff", (z, int(usefull.HEIGHT/2 + w)))
        img.put("#ffffff", (z, int(usefull.HEIGHT/2 - w)))

    mainloop()
