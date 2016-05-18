from mandelbrot import calculate_mandelbrot_values
from colors import coloring_schemes
from image import draw_image


base_location = (-1.0, 0.0), 2.0
zipper_location = (0.274, 0.482), 0.01


def main(w, h, center, x_scale, max_iter, coloring_scheme, verbose):
    mandelbrot_values = calculate_mandelbrot_values(
        w, h, center, x_scale, max_iter, verbose)
    mode, get_color = coloring_scheme
    color_values = map(lambda v: get_color(v[0], v[1], v[2]), mandelbrot_values)
    im = draw_image(color_values, w, h, mode)
    if mode != 'RGB':
        im = im.convert('RGB')
    with open('mandelbrot.png', 'w') as fp:
        im.save(fp)


if __name__ == "__main__":
    w = 1600
    h = 1200
    max_iter = 2**12
    center, x_scale = base_location
    coloring_scheme = coloring_schemes['gradient']
    verbose = True
    main(w, h, center, x_scale, max_iter, coloring_scheme, verbose)
