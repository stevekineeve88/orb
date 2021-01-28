import requests
from bs4 import BeautifulSoup


class DictionaryAdapter:
    def __init__(self):
        self.parser = "html.parser"

    def is_word(self, word: str):
        pass

    def parse_html(self, url: str) -> BeautifulSoup:
        return BeautifulSoup(requests.get(url).text, self.parser)
