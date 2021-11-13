"""A file that encapsulates the body and author of quotes from files."""


class QuoteModel:
    """A quote from a docx, csv, pdf or txt file.

    The quote is formatted that the body and author
     of the quote are separated by a hyphen.
    """

    def __init__(self, body, author):
        """Create a new quote.

        :params: The body and author of a quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return 'repr(self)'."""
        return f'<body: {self.body}, author: {self.author}>'
