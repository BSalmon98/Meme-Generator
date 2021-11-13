"""A file to set abstract class parse and check ingestibility."""

from abc import ABC, abstractmethod
from typing import List

from .quoteModel import QuoteModel


class IngestorInterface(ABC):
    """Check file ingestibility, create abstract parse metthod.

    An abstract class to check if the path is ingestible
    and implement an abstract parse method to be inherited by
    child classes.
    """

    allowed_ext = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Determine if file path is ingestible.

        Isolate the extension of a file path
        and check against allowed extensions.

        :param: A file path
        :return: A boolean for file ingestibility
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_ext

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method ensuring ingestors have a parse method."""
        pass
