import requests
from bs4 import BeautifulSoup
from models import ActivePublicOfferingModel
from scrapers.scraper import Scraper
import logging


logger = logging.getLogger(__name__)


class ActivePublicOfferingScraper(Scraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def scrape(self):
        try:
            response = requests.get(self.target)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                for ipo in soup.find_all('div', {'class': 'ipo'}):
                    self + ActivePublicOfferingModel(
                        title=ipo.find('a').text,
                        url=ipo.find('a').get('href'),
                        detail={
                            detail.find_all('span')[0].text.strip().replace(':', ''): detail.find_all('span')[
                                1].text.strip()
                            for detail in ipo.find_all('div', {'class': 'detail'})
                            if len(detail.find_all('span')) >= 2
                        }
                    )
                self.set_successful(self > 0)
                logger.debug(f'ActivePublicOfferingScraper scraped {len(self)} Assets')
            else:
                logger.warning(
                    f'ActivePublicOfferingScraper is get a response and response status code is not 200 != {response.status_code} ')
        except Exception as exception:
            logger.exception(exception)

    @property
    def data(self) -> list[ActivePublicOfferingModel]:
        return super().data


if __name__ == '__main__':
    if scraper := ActivePublicOfferingScraper(target=''):
        print(scraper.data)
