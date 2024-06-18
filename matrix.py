#!/usr/bin/env python3
"""
matrix.py
matrix code-like effect
"""

from PIL import Image  # pylint: disable=import-error
from PIL import ImageDraw  # pylint: disable=import-error

from rgbmatrix import RGBMatrix, RGBMatrixOptions  # pylint: disable=import-error

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

if __name__ == "__main__":
    main()
