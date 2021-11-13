"""An ingestor file to handle pdf files containing formatted quotes."""

from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel

import subprocess
import os
from typing import List


class PDFIngestor(IngestorInterface):
    """A class inheriting from IngestorInterface that ingests pdf files."""

    allowed_ext = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a list of quotes from the file.

        Using can_ingest, check if the extension is 'pdf'.
        Read the file by using subprocess to call 'pdftotext',
        making a readable text file, and create QuoteModel class
        objects that are appended to a list of quotes, which is then returned.

        :params: A file path
        :returns: A list of quotes in the form of the QuoteModel class
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest filetype')

        tmp = "./tmp.txt"
        subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, 'r')
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                quote = QuoteModel(str(parse[0]), str(parse[1]))
                quotes.append(quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
