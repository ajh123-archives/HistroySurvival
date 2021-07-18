WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700


def hex_to_rgba_colour(color):
    if '#' in color:
        c = color.lstrip("#")
        c = max(6 - len(c), 0) * "0" + c
        r = int(c[:2], 16)
        g = int(c[2:4], 16)
        b = int(c[4:], 16)
        color = (r, g, b, 255)
    return color
