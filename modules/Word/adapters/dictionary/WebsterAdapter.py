from modules.Word.adapters.abstracts.DictionaryAdapter import DictionaryAdapter


class WebsterAdapter(DictionaryAdapter):
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.merriam-webster.com"

    def is_word(self, word: str):
        return self.parse_html(
            f'{self.base_url}/dictionary/{word}'
        ).find("h1", {"class": "mispelled-word"}) is None
