"""An ingestor file to handle csv files containing formatted quotes."""

from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel

import pandas
from typing import List


class CSVIngestor(IngestorInterface):
    """A class inheriting from IngestorInterface that ingests CSV files."""

    allowed_ext = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a list of quotes from the file.

        Using can_ingest, check if the extension is 'csv'.
        Read the file and create QuoteModel class objects that
        are appended to a list of quotes, which is then returned.

        :params: A file path
        :returns: A list of quotes in the form of the QuoteModel class
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest filetype')

        quotes = []
        data_frame = pandas.read_csv(path, header=0)

        for i, row in data_frame.iterrows():
            quote = QuoteModel(f'"{row["body"]}"', row['author'])
            quotes.append(quote)

        return quotes
