#!/usr/bin/env python3
"""
square.py
draw some rectangles
make 'em bounce
"""

import time
import sys
from PIL import Image
from PIL import ImageDraw

from rgbmatrix import RGBMatrix, RGBMatrixOptions  # pylint: disable=import-error


def make_rect(width: int, height: int, color: tuple) -> Image:
    """generate a "rounded" rect

    Args:
        width (int): rectangle width
        height (int): rectangle height
        color (tuple): RGB color

    Returns:
        Image: the completed rectangle
    """
    h_start = w_start = 0
    h_end = height - 1
    w_end = width - 1

    color_r = color[0]
    color_g = color[1]
    color_b = color[2]

    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    draw.rectangle((w_start, h_start, w_end, h_end), fill=(color_r, color_g, color_b))

    draw.point(
        (w_start + 1, h_start),
        fill=(int(color_r * 0.1), int(color_g * 0.1), int(color_b * 0.1)),
    )
    draw.point(
        (w_end - 1, h_start),
        fill=(int(color_r * 0.1), int(color_g * 0.1), int(color_b * 0.1)),
    )
    draw.point(
        (w_start, h_start + 1),
        fill=(int(color_r * 0.1), int(color_g * 0.1), int(color_b * 0.1)),
    )
    draw.point(
        (w_end, h_start + 1),
        fill=(int(color_r * 0.1), int(color_g * 0.1), int(color_b * 0.1)),
    )
    draw.point(
        (w_start, h_end - 1),
        fill=(int(color_r * 0.1), int(color_g * 0.1), int(color_b * 0.1)),
    )
    draw.point(
        (w_end, h_end - 1),
        fill=(int(color_r * 0.1), int(color_g * 0.1), int(color_b * 0.1)),
    )
    draw.point(
        (w_start + 1, h_end),
        fill=(int(color_r * 0.1), int(color_g * 0.1), int(color_b * 0.1)),
    )
    draw.point(
        (w_end - 1, h_end),
        fill=(int(color_r * 0.1), int(color_g * 0.1), int(color_b * 0.1)),
    )

    draw.point((w_start, h_start), fill=(0, 0, 0))
    draw.point((w_start, h_end), fill=(0, 0, 0))
    draw.point((w_end, h_start), fill=(0, 0, 0))
    draw.point((w_end, h_end), fill=(0, 0, 0))

    return img


def move_down(matrix: RGBMatrix, rect: Image, pos: int) -> None:
    """
    move a rectangle's Group down (todo: add gravity?)
    """
    for i in range(matrix.height - rect.height):
        time.sleep(0.025)
        matrix.SetImage(rect, pos, i)
        for j in range(rect.width):
            matrix.SetPixel(pos + j, i - 1, 0, 0, 0)


def move_up(matrix: RGBMatrix, rect: Image, pos: int) -> None:
    """
    move a rectangle's Group up (todo: add gravity?)
    """
    for i in range(matrix.height - rect.height - 1, -1, -1):
        time.sleep(0.025)
        matrix.SetImage(rect, pos, i)
        for j in range(rect.width):
            matrix.SetPixel(pos + j, matrix.height - i + 1, 0, 0, 0)


def main():
    """
    they call it main.
    """
    # Configuration for the matrix
    options = RGBMatrixOptions()
    options.cols = 64
    options.rows = 32
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = "adafruit-hat"

    matrix = RGBMatrix(options=options)
    # offscreen_matrix = matrix.CreateFrameCanvas()

    width = height = 20
    orange = [255, 165, 0]
    light_blue = [173, 216, 230]
    green = [0, 255, 0]

    image1 = make_rect(width, height, orange)
    image2 = make_rect(width, height, light_blue)
    image3 = make_rect(width, height, green)

    # matrix.Clear()
    matrix.SetImage(image1, 0, 0)
    matrix.SetImage(image2, 21, 0)
    matrix.SetImage(image3, 42, 0)
    time.sleep(1)

    try:
        while True:
            move_down(matrix, image1, 0)
            move_down(matrix, image2, 21)
            move_down(matrix, image3, 42)
            move_up(matrix, image1, 0)
            move_up(matrix, image2, 21)
            move_up(matrix, image3, 42)
    except KeyboardInterrupt:
        matrix.Clear()
        sys.exit("cancelled.")


if __name__ == "__main__":
    main()


# class roundrect:
#
# init(upper_left, upper_right, lower_left, lower_right, color[tuple?]):
# 1. draw a rectangle in specified color
# 2. set color to 50% V
# 3. draw eight points
# 4. set color to black
# 5. draw four corner points
#
# show(point_x, point_y):
#  matrix.SetImage(self.image, point_x, point_y)
#
# move_down():
# for x in range(10):
#     matrix.SetImage(self.image, self.upper_left, x)
#     for y in range(20):
#         matrix.SetPixel(y, x-1, 0, 0, 0)
#     time.sleep(0.025)
