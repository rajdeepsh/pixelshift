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
    """Replace all occurances of the first RGB pixel with the second RGB pixel"""


def replace(img, src_rgb, dst_rgb):
    src_bgr = src_rgb[::-1]
    dst_bgr = dst_rgb[::-1]
    mask = np.all(img == src_bgr, axis=-1)
    img[mask] = dst_bgr


def main(args):
    img = cv2.imread(args.src, cv2.IMREAD_COLOR)

    if args.replace is not None:
        replace(img, *args.replace)

    cv2.imwrite(args.dst, img)


if __name__ == "__main__":
    args = tyro.cli(Args)
    main(args)
