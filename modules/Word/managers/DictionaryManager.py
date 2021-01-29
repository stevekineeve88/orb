from modules.Word.adapters.dictionary.WebsterAdapter import WebsterAdapter
from modules.Word.adapters.abstracts.DictionaryAdapter import DictionaryAdapter


class DictionaryManager:
    def __init__(self, **kwargs):
        self.dictionary_adapter: DictionaryAdapter = kwargs.get("dictionary_adapter") or WebsterAdapter()

    def is_word(self, word: str) -> bool:
        return self.dictionary_adapter.is_word(word)
