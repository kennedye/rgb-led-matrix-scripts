#!/usr/bin/env python3

from PIL import Image
from PIL import ImageDraw
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions


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

    wb = hb = 0
    we = he = 19
    orange = [255, 165, 0]
    dk_orange = [128, 83, 0]
    black = [0, 0, 0]
    light_blue = [173, 216, 230]
    dk_blue = [86, 108, 115]
    green = [0, 255, 0]
    dk_green = [0, 128, 0]

    image1 = Image.new("RGB", (20, 20))
    r, g, b = orange
    draw = ImageDraw.Draw(image1)
    draw.rectangle((wb, hb, we, he), fill=(r, g, b))
    r, g, b = dk_orange
    draw.point((wb + 1, hb), fill=(r, g, b))
    draw.point((we - 1, hb), fill=(r, g, b))
    draw.point((wb, hb + 1), fill=(r, g, b))
    draw.point((we, hb + 1), fill=(r, g, b))
    draw.point((wb, he - 1), fill=(r, g, b))
    draw.point((we, he - 1), fill=(r, g, b))
    draw.point((wb + 1, he), fill=(r, g, b))
    draw.point((we - 1, he), fill=(r, g, b))
    r, g, b = black
    draw.point((wb, hb), fill=(r, g, b))
    draw.point((wb, he), fill=(r, g, b))
    draw.point((we, hb), fill=(r, g, b))
    draw.point((we, he), fill=(r, g, b))

    image2 = Image.new("RGB", (20, 20))
    r, g, b = light_blue
    draw = ImageDraw.Draw(image2)
    draw.rectangle((wb, hb, we, he), fill=(r, g, b))
    r, g, b = dk_blue
    draw.point((wb + 1, hb), fill=(r, g, b))
    draw.point((we - 1, hb), fill=(r, g, b))
    draw.point((wb, hb + 1), fill=(r, g, b))
    draw.point((we, hb + 1), fill=(r, g, b))
    draw.point((wb, he - 1), fill=(r, g, b))
    draw.point((we, he - 1), fill=(r, g, b))
    draw.point((wb + 1, he), fill=(r, g, b))
    draw.point((we - 1, he), fill=(r, g, b))
    r, g, b = black
    draw.point((wb, hb), fill=(r, g, b))
    draw.point((wb, he), fill=(r, g, b))
    draw.point((we, hb), fill=(r, g, b))
    draw.point((we, he), fill=(r, g, b))

    image3 = Image.new("RGB", (20, 20))
    r, g, b = green
    draw = ImageDraw.Draw(image3)
    draw.rectangle((wb, hb, we, he), fill=(r, g, b))
    r, g, b = dk_green
    draw.point((wb + 1, hb), fill=(r, g, b))
    draw.point((we - 1, hb), fill=(r, g, b))
    draw.point((wb, hb + 1), fill=(r, g, b))
    draw.point((we, hb + 1), fill=(r, g, b))
    draw.point((wb, he - 1), fill=(r, g, b))
    draw.point((we, he - 1), fill=(r, g, b))
    draw.point((wb + 1, he), fill=(r, g, b))
    draw.point((we - 1, he), fill=(r, g, b))
    r, g, b = black
    draw.point((wb, hb), fill=(r, g, b))
    draw.point((wb, he), fill=(r, g, b))
    draw.point((we, hb), fill=(r, g, b))
    draw.point((we, he), fill=(r, g, b))

    matrix.Clear()
    matrix.SetImage(image1, 0, 0)
    matrix.SetImage(image2, 21, 0)
    matrix.SetImage(image3, 42, 0)
    time.sleep(1)
    for x in range(10):
        matrix.SetImage(image1, 0, x)
        for y in range(20):
            matrix.SetPixel(y, x-1, 0, 0, 0)
        time.sleep(0.025)
    for x in range(10):
        matrix.SetImage(image2, 21, x)
        for y in range(20):
            matrix.SetPixel(21+y, x-1, 0, 0, 0)
        time.sleep(0.025)
    for x in range(10):
        matrix.SetImage(image3, 42, x)
        for y in range(20):
            matrix.SetPixel(42+y, x-1, 0, 0, 0)
        time.sleep(0.025)
    time.sleep(5)
    matrix.Clear()

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
