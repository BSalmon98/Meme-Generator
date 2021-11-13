"""File to load an image."""

from PIL import Image


class ImageLoader:
    """Class to load an image for processing using Pillow."""

    def loader(path):
        """Check if file path is ingestible and load using pillow.

        Check for ingestibility first by isolating path extension and
        comparing to allowed extensions. Extra extensions can be added,
        such as png. Return loaded image.

        :param: A file path.
        :return: A loaded image.
        """
        allowed_ext = ['jpg', 'png']

        ext = path.split('.')[-1]
        if ext not in allowed_ext:
            Exception('invalid file type')


        return Image.open(path)
