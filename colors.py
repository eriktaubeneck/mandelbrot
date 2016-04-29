import math

from gradient import color_gradient


rgb_black = 0, 0, 0
range_size = 300
purple_gradient = color_gradient((256, 256, 256), (85, 10, 110), 50)
green_gradient = color_gradient((85, 10, 110), (97, 227, 36), range_size)
gradient = purple_gradient + green_gradient


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
    # return gradient[min(count, range_size - 1)]
    d = math.log(math.log(abs(z))/math.log(2.0), 2)
    u = count + 1 - d
    n = min(int(u), range_size-2)
    color_range = color_gradient(gradient[n], gradient[n+1], 10)
    return color_range[int(10*(d-math.floor(d)))-1]


coloring_schemes = {
    'rgb': ('RGB', get_rgb),
    'gradient': ('RGB', get_gradient),
}
