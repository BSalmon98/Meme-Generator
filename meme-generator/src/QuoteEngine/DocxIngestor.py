"""An ingestor file to handle docx files containing formatted quotes."""

from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel

import docx
from typing import List


class DocxIngestor(IngestorInterface):
    """A class inheriting from IngestorInterface that ingests Docx files."""

    allowed_ext = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a list of quotes from the file.

        Using can_ingest, check if the extension is 'docx'.
        Read the file using docx module and create QuoteModel class
        objects that areappended to a list of quotes, which is then returned.

        :params: A file path
        :returns: A list of quotes in the form of the QuoteModel class
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest filetype')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                quote = QuoteModel(str(parse[0]), str(parse[1]))
                quotes.append(quote)

        return quotes
