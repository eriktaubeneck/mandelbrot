from PIL import Image
import pyprind


def compute_count(x, y, max_iter):
    count = 0
    z = 0.0
    c = complex(x, y)
    while count < max_iter:
        z = z ** 2 + c
        if abs(z) > 2.0:
            break
        count += 1
    return count


def get_color(count, max_iter):
    _r, _g, _b = 256, 128, 64
    r = int((count % _r) * 256/_r)
    g = int((count % _g) * 256/_g)
    b = int((count % _b) * 256/_b)
    return r, b, g


def compute_point(pixels, i, _min, _max):
    delta = (_max - _min)/float(pixels)
    return _min + (i * delta)


def compute_colors(w, h, min_x, max_x, min_y, max_y, max_iter):
    rgb_values = []
    progress = pyprind.ProgBar(w*h, monitor=True, bar_char='#')
    for _y in reversed(xrange(h)):
        for _x in xrange(w):
            x = compute_point(w, _x, min_x, max_x)
            y = compute_point(h, _y, min_y, max_y)
            rgb_values.append(get_color(compute_count(x, y, max_iter), max_iter))
            progress.update()
    return rgb_values


def draw_image(rgb_values, w, h):
    im = Image.new('RGB', (w, h))
    im.putdata(rgb_values)
    return im


def main(w, h, max_iter, min_x, max_x, min_y, max_y):
    rgb_values = compute_colors(w, h, min_x, max_x, min_y, max_y, max_iter)
    im = draw_image(rgb_values, w, h)
    with open('mandelbrot.png', 'w') as fp:
        im.save(fp)


if __name__ == "__main__":
    w = 800
    h = 600
    max_iter = 2**10
    center = -1.0, 0.0
    x_scale = 4.0
    y_scale = x_scale*h/w
    min_x, max_x = center[0]-x_scale/2, center[0]+x_scale/2
    min_y, max_y = center[1]-y_scale/2, center[1]+y_scale/2
    main(w, h, max_iter, min_x, max_x, min_y, max_y)


def unzip():
    w = 800
    h = 600
    max_iter = 2**10
    center = 0.274, 0.482
    x_scale = 0.02
    y_scale = x_scale*h/w
    min_x, max_x = center[0]-x_scale/2, center[0]+x_scale/2
    min_y, max_y = center[1]-y_scale/2, center[1]+y_scale/2
    main(w, h, max_iter, min_x, max_x, min_y, max_y)
