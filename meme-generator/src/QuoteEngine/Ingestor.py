"""A selector file for choosing the correct ingestor."""

from typing import List

from .quoteModel import QuoteModel
from .ingestorInterface import IngestorInterface
from .TXTIngestor import TXTIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """A class to select the correct ingestor based upon the file type."""

    ingestors = [TXTIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select the correct ingestor for the file type.

        Iterate though the can_ingest functions for each
        ingestor and returns results when can_ingest is true.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
