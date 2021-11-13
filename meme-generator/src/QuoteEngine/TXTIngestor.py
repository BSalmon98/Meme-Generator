"""An ingestor file to handle txt files containing formatted quotes."""

from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel

from typing import List


class TXTIngestor(IngestorInterface):
    """A class inheriting from IngestorInterface that ingests txt files."""

    allowed_ext = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a list of quotes from the file.

        Using can_ingest, checks if the extension is 'txt'.
        Read the file and create QuoteModel class objects that are
        appended to a list of quotes, which is then returned.

        :params: A file path
        :returns: A list of quotes in the form of the QuoteModel class
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest filetype')

        quotes = []
        txt = open(path, 'r')

        for line in txt.readlines():
            line = line.strip('\n\r').strip('ï»¿')
            if len(line) > 0:
                parse = line.split('-')
                quote = QuoteModel((str(parse[0])), str(parse[1]))
                quotes.append(quote)

        txt.close()
        return quotes
