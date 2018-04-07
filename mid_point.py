import usefull


def write_pixel(img, x, y):
    z = int(usefull.WIDTH/2)
    w = int(usefull.HEIGHT/2)

    # write pixel on every octant of circunference
    img.put("#ffffff", (z + x, w + y))
    img.put("#ffffff", (z + x, w - y))
    img.put("#ffffff", (z - x, w + y))
    img.put("#ffffff", (z - x, w - y))
    img.put("#ffffff", (z + y, w + x))
    img.put("#ffffff", (z + y, w - x))
    img.put("#ffffff", (z - y, w + x))
    img.put("#ffffff", (z - y, w - x))


def mid_point(window, img, radius):
    x = 0
    y = radius

    # 'd' is the decision variable
    d = 1 - radius
    write_pixel(img, x, y)
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
        write_pixel(img, x, y)

    window.update()
