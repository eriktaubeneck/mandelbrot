from colors import compute_colors
from image import draw_image
from colors import get_rgb, get_hsv


def main(w, h, max_iter, min_x, max_x, min_y, max_y, get_color, mode):
    color_values = compute_colors(w, h, min_x, max_x, min_y, max_y, max_iter, get_color, True)
    im = draw_image(color_values, w, h, mode)
    if mode != 'RGB':
        im = im.convert('RGB')
    with open('mandelbrot.png', 'w') as fp:
        im.save(fp)


if __name__ == "__main__":
    w = 1000
    h = 750
    max_iter = 2**10
    center = 0.275, 0.0
    x_scale = 0.1
    y_scale = x_scale*h/w
    min_x, max_x = center[0]-x_scale/2, center[0]+x_scale/2
    min_y, max_y = center[1]-y_scale/2, center[1]+y_scale/2
    main(w, h, max_iter, min_x, max_x, min_y, max_y, get_hsv, 'HSV')


def unzip():
    w = 800
    h = 600
    max_iter = 2**12
    center = 0.274, 0.482
    x_scale = 0.02
    y_scale = x_scale*h/w
    min_x, max_x = center[0]-x_scale/2, center[0]+x_scale/2
    min_y, max_y = center[1]-y_scale/2, center[1]+y_scale/2
    main(w, h, max_iter, min_x, max_x, min_y, max_y, get_rgb, 'RGB')
