"""File to produced a meme using a provided image and quote."""

from .imageLoader import ImageLoader
from .imageFormatter import ImageFormatter
from .imageCaptioner import ImageCaptioner


class ImageHandler:
    """Handler to produce user specified meme."""

    def process_image(path, text, author, width=500) -> str:
        """Call processing functions when needed.

        A handler to call image formatting functions when needed,
        storing and passing variables between them. Allows functions
        to be added and removed as needed.

        :params: an image file path, a quote split into body and author
                 and a width for the final image
        :returns: a path to the formatted and captioned meme
        """
        img = ImageLoader.loader(path)
        img_resized = ImageFormatter.resizer(img, width)
        meme = ImageCaptioner.captioner(img_resized, text, author)
        meme.save('./static/Memes/meme.jpg')
        return './static/Memes/meme.jpg'
