from abc import ABC


class Scraper(ABC):
    def __init__(self, target: str):
        self.target: str = target
        self.__data = []
        self.__successful = False
        self.scrape()

    @property
    def data(self):
        return self.__data

    def __add__(self, other):
        self.__data.append(other)

    def __bool__(self):
        return self.__successful

    def set_successful(self, status: bool) -> None:
        self.__successful = status

    def scrape(self):
        raise NotImplementedError
