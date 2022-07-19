import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
from crawler.utils import dtype_convert
from crawler.utils.logger import logger


class Crawler(ABC):
    @abstractmethod
    def crawl(self):
        pass

    @abstractmethod
    def _check_connection(self):
        pass


class Hentai2ReadCrawler(Crawler):
    def __init__(self, url):
        self.url = url
        self.response = None
        self.soup = None
        self.result = None

    def _check_connection(self):
        try:
            self.response = requests.get(self.url)
            status_code = self.response.status_code
            if status_code == 200:
                logger.info(f"Connect successfully to {self.url}")
                return True
            logger.error(f"Cannot connect to {self.url}. Status Code {status_code}")
        except ConnectionError:
            logger.error(f"Connection to {self.url} Error")

    def _get_soup(self):
        self.soup = BeautifulSoup(self.response.content, 'html5lib')

    def crawl(self):
        if self._check_connection():
            self._get_soup()

