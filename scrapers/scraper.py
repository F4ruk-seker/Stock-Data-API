from abc import ABC
from datetime import datetime
import logging


logger = logging.getLogger(__name__)


class Scraper(ABC):
    def __init__(self, target: str):
        self.target: str = target
        self.__data = []
        self.__successful = False
        self.scrape()
        logger.info(f'Scraper is start |{datetime.now()}|')

    @property
    def data(self):
        return self.__data

    def __iter__(self):
        return iter(self.__data)

    def __len__(self):
        return len(self.__data)

    def __add__(self, other):
        self.__data.append(other)

    def __bool__(self):
        return self.__successful

    def __gt__(self, other):
        if isinstance(other, int):
            return len(self.__data) > other
        return False

    def __lt__(self, other):
        if isinstance(other, int):
            return len(self.__data) < other
        return False

    def set_successful(self, status: bool) -> None:
        self.__successful = status

    def scrape(self):
        raise NotImplementedError
