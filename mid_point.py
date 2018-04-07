import usefull

def mid_point(window, img, radius):
    x = 0
    y = radius

    # 'd' is the decision variable
    d = 1 - radius
    usefull.write_pixel(img, x, y)
    while y > x:
        if d < 0:
            d = d + 2 * x + 3

            # draw to the right
            x += 1
        else:
            d = d + 2 * (x - y) + 5

            # draw to the bottom right
            x += 1
            y -= 1
        usefull.write_pixel(img, x, y)

    window.update()
