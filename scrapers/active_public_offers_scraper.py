import requests
from bs4 import BeautifulSoup
from models import ActivePublicOfferingModel
from scrapers.scraper import Scraper


class ActivePublicOfferingScraper(Scraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def scrape(self):
        response = requests.get(self.target)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for ipo in soup.find_all('div', {'class': 'ipo'}):
                self + ActivePublicOfferingModel(
                    title=ipo.find('a').text,
                    url=ipo.find('a').get('href'),
                    detail={
                        detail.find_all('span')[0].text.strip().replace(':', ''): detail.find_all('span')[1].text.strip()
                        for detail in ipo.find_all('div', {'class': 'detail'})
                        if len(detail.find_all('span')) >= 2
                    }
                )
            self.set_successful(True)

    @property
    def data(self) -> list[ActivePublicOfferingModel]:
        return super().data


if __name__ == '__main__':
    if scraper := ActivePublicOfferingScraper(target=''):
        print(scraper.data)
