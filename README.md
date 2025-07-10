# pixelshift
Common image transformations

## Requirements
1. [uv](https://github.com/astral-sh/uv) python package manager

## Usage

### Replace Pixels
Replace all occurances of the first RGB value with the second RGB value in the source image. The resulting image will be saved to the destination path.
```bash
# Format
uv run main.py --src <source_image_path> --dst <destination_image_path> --replace  <first_red> <first_green> <first_blue> <second_red> <second_green> <second_blue>
# Example which changes all the white pixels to black pixels in ~/img.png and saves the resulting image to ~/img2.png
uv run main.py --src ~/img.png --dst ~/img2.png --replace 255 255 255 0 0 0
```

> [!TIP]
> You can find more information with `uv run main.py --help`.
