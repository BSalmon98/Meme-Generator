"""File for formatting images."""

from PIL import Image


class ImageFormatter:
    """Class for image resizing."""

    def resizer(img, width):
        """Resize image based on specified width.

        Use the ratio of width and height to scale the size of the
        image proportionally. Resize width to specified value and adjust
        height to nearest pixel.

        :param: A loaded image and width for resized image.
        :return: A resized image.
        """
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img_resized = img.resize((width, height), Image.NEAREST)
        return img_resized