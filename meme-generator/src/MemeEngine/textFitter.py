"""File for text formatting on image."""

class TextFitter:
    """Class to fit text within bounds of image."""

    def fitter(text, x_pos, y_pos, font, width, height):
        """Fitter to reposition and split text to fit on image.

        Check if text goes out of the boundary of image. If text width
        is shorter than image width, move text until it fits. If text width
        is longer than image width, split text onto separate lines and return
        as a list. If text goes bellow image, raise it up accordingly.
        """
        size = font.getsize(text)

        if size[0] + x_pos < width:
            return [text], x_pos, y_pos

        elif size[0] + x_pos >= width and size[0] < width:
            overhang = (x_pos+size[0])-width
            x_pos = x_pos-(overhang+10)
            return [text], x_pos, y_pos

        elif size[0] > width:
            x_pos = 10
            lines = []
            line = []
            words = text.split(' ')
            joined_line = ''

            for word in words:
                line.append(word)
                joined_line = ' '.join(line)
                if font.getsize(joined_line)[0] > (width-20):
                    del line[-1]
                    joined_line = ' '.join(line)
                    lines.append(joined_line)
                    line = [word]
                    if word == words[-1]:
                        joined_line = word
            lines.append(joined_line)


            if y_pos + size[1]*(len(lines)+1) > height:
                overhang = (y_pos+size[1]*(len(lines))+1)-height+20
                y_pos = y_pos-overhang

            return lines, x_pos, y_pos

