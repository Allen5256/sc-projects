"""
File: blur.py
Name: Allen Lee
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    clear = img
    blurred = SimpleImage.blank(clear.width, clear.height)
    for y in range(clear.height):
        for x in range(clear.width):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            num_p = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixel_x = x+i
                    pixel_y = y+j
                    if 0 <= pixel_x < clear.width and 0 <= pixel_y < clear.height:
                        pixel = clear.get_pixel(pixel_x, pixel_y)
                        r_sum += pixel.red
                        g_sum += pixel.green
                        b_sum += pixel.blue
                        num_p += 1
            new_p = blurred.get_pixel(x, y)
            new_p.red = r_sum/num_p
            new_p.green = g_sum/num_p
            new_p.blue = b_sum/num_p
    return blurred


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
