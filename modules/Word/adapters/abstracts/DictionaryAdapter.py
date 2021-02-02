import requests
from bs4 import BeautifulSoup


class DictionaryAdapter:
    def __init__(self):
        self.parser = "html.parser"

    def is_word(self, word: str):
        pass

    def parse_html(self, url: str) -> BeautifulSoup:
        return BeautifulSoup(requests.get(url).text, self.parser)

    @classmethod
    def is_english(cls, word: str):
        try:
            word.encode(encoding='utf-8').decode('ascii')
            return True
        except UnicodeDecodeError:
            return False

    @classmethod
    def contains_number(cls, word: str) -> bool:
        return any(char.isdigit() for char in word)
