import math

from gradient import color_interpolate, circular_gradient


rgb_black = 0, 0, 0
range_size = 240
gradient = circular_gradient([(97, 227, 36,), (85, 10, 110)], range_size)


def get_rgb(escape, z, count):
    if not escape:
        return rgb_black
    _r, _g, _b = 64, 32, 16
    r = int((count % _r) * 256/_r)
    g = int((count % _g) * 256/_g)
    b = int((count % _b) * 256/_b)
    return r, g, b


def get_gradient(escape, z, count):
    if not escape:
        return rgb_black
    d = math.log(math.log(abs(z))/math.log(2.0), 2)
    u = count + 1 - d
    n = (int(u) % range_size) - 1
    #return gradient[n]
    color1, color2 = gradient[n], gradient[n+1]
    return color_interpolate(color1, color2, u % 1)


coloring_schemes = {
    'rgb': ('RGB', get_rgb),
    'gradient': ('RGB', get_gradient),
}
