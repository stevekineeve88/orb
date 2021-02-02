from modules.Word.adapters.abstracts.DictionaryAdapter import DictionaryAdapter


class WebsterAdapter(DictionaryAdapter):
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.merriam-webster.com"

    def is_word(self, word: str) -> bool:
        html = self.parse_html(f'{self.base_url}/dictionary/{word}')
        return html.find("h1", {"class": "mispelled-word"}) is None and \
            html.find("div", {"class": "words_fail_us_cont"}) is None
