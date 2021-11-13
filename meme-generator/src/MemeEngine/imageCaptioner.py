"""File to caption images."""

from PIL import Image, ImageDraw, ImageFont
from .textFitter import TextFitter
import random

class ImageCaptioner:
    """Class to add a given quote to an image."""

    fonts = ('./MemeEngine/Fonts/LilitaOne/LilitaOne-Regular.ttf',
             './MemeEngine/Fonts/MochyPopOne/MochiyPopPOne-Regular.ttf',
             './MemeEngine/Fonts/Mohave/Mohave-Italic-VariableFont_wght.ttf',
             './MemeEngine/Fonts/Mohave/Mohave-VariableFont_wght.ttf',
             './MemeEngine/Fonts/OpenSans/'
             'OpenSans-Italic-VariableFont_wdth,wght.ttf',
             './MemeEngine/Fonts/OpenSans/'
             'OpenSans-VariableFont_wdth,wght.ttf')

    @classmethod
    def captioner(cls, img, text, author):
        """Place quote on image in random location and random font.

        Select a font from list of fonts, place the quote in
        random location on image. If text doesn't fit, send to
        TextFitter to format. Return captioned image.

        :param: A resized image and a quote split into body and
                author.
        :return: A captioned image.
        """
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(
                str(random.choice(cls.fonts)), size=30)
        x = random.randint(10, img.size[0]-100)
        y = random.randint(30, img.size[1]-50)
        text, x, y = TextFitter.fitter(text, x, y, font,
                                       img.size[0], img.size[1])
        for index, line in enumerate(text):
            draw.text((x, y+(index*25)), line, font=font, fill='white', stroke_width=1, stroke_fill='black')
        draw.text((x, y+((len(text))*25)), f'-{author}', font=font, fill='white', stroke_width=1, stroke_fill='black')
        return img