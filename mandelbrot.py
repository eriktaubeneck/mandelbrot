import pyprind
from hermes import Hermes
from hermes.backend.redis import Backend


cache = Hermes(Backend, host='localhost', db=1)


def compute_point(pixels, i, _min, _max):
    delta = (_max - _min)/float(pixels)
    return _min + (i * delta)


def check_cardioid(c):
    q = (c.real - 0.25)**2 + c.imag**2
    return q * (q + (c.real - 0.25)) < (0.25 * c.imag**2)


def mandelbrot_process(c, max_iter):
    count = 0
    z = 0.0
    escape = False
    if check_cardioid(c):
        return False, c, max_iter
    while count < max_iter:
        z = z ** 2 + c
        if abs(z) > 2.0:
            escape = True
            break
        count += 1
    return escape, z, count


@cache
def calculate_mandelbrot_values(w, h, center, x_scale, max_iter, verbose):
    y_scale = x_scale*h/w
    min_x, max_x = center[0]-x_scale/2, center[0]+x_scale/2
    min_y, max_y = center[1]-y_scale/2, center[1]+y_scale/2
    if verbose:
        progress = pyprind.ProgBar(w*h, monitor=True, bar_char='#')

    mandelbrot_values = []
    for _y in reversed(xrange(h)):
        for _x in xrange(w):
            x = compute_point(w, _x, min_x, max_x)
            y = compute_point(h, _y, min_y, max_y)
            c = complex(x, y)
            escape, z, count = mandelbrot_process(c, max_iter)
            mandelbrot_values.append((escape, z, count))
            if verbose:
                progress.update()
    return mandelbrot_values
