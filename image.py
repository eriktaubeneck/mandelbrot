from PIL import Image


def draw_image(color_values, w, h, mode):
    im = Image.new(mode, (w, h))
    im.putdata(color_values)
    return im
