import pathlib
from dataclasses import dataclass

import cv2
import numpy as np
import tyro


@dataclass
class Args:
    """Pixelshift, common image transformations"""

    src: pathlib.Path
    """Source image path"""

    dst: pathlib.Path
    """Destination image path"""

    replace: tuple[tuple[int, int, int], tuple[int, int, int]] | None = None
    """Replace all occurances of the first RGB value with the second RGB value. Provide RGB values in the form of <first_red> <first_green> <first_blue> <second_red> <second_green> <second_blue>."""

    crop: tuple[tuple[int, int], tuple[int, int]] | None = None
    """Crop image according to top-left and bottom-right XY coordinates. Provide coordinates in the form of <top_left_x> <top_left_y> <bottom_right_x> <bottom_right_y>."""


def replace(img, src_rgb, dst_rgb):
    src_bgr = src_rgb[::-1]
    dst_bgr = dst_rgb[::-1]
    mask = np.all(img == src_bgr, axis=-1)
    img[mask] = dst_bgr


def crop(img, top_left_xy, btm_right_xy):
    x1, y1 = top_left_xy
    x2, y2 = btm_right_xy
    return img[y1:y2, x1:x2]


def main(args):
    img = cv2.imread(args.src, cv2.IMREAD_COLOR)

    if args.replace is not None:
        replace(img, *args.replace)

    if args.crop is not None:
        crop(img, *args.crop)

    cv2.imwrite(args.dst, img)


if __name__ == "__main__":
    args = tyro.cli(Args)
    main(args)
