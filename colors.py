import math
from mandelbrot import compute_z_and_count

import pyprind


def compute_point(pixels, i, _min, _max):
    delta = (_max - _min)/float(pixels)
    return _min + (i * delta)


def get_rgb(z, count, max_iter):
    _r, _g, _b = 64, 32, 16
    r = int((count % _r) * 256/_r)
    g = int((count % _g) * 256/_g)
    b = int((count % _b) * 256/_b)
    return r, g, b


def get_hsv(z, count, max_iter):
    if abs(z) < 1:
        return 0, 0, 0
    v = count + 1 - math.log(math.log(abs(z))/math.log(2.0), 2)
    h = int((v*360) % 360)
    return h, 60, 100


def compute_colors(w, h, min_x, max_x, min_y, max_y, max_iter, get_color, verbose):
    color_values = []
    if verbose:
        progress = pyprind.ProgBar(w*h, monitor=True, bar_char='#')
    for _y in reversed(xrange(h)):
        for _x in xrange(w):
            x = compute_point(w, _x, min_x, max_x)
            y = compute_point(h, _y, min_y, max_y)
            z, count = compute_z_and_count(x, y, max_iter)
            color_values.append(get_color(z, count, max_iter))
            if verbose:
                progress.update()
    return color_values
