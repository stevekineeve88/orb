import re

from modules.Util.result import Result
from modules.Word.adapters.dictionary.WebsterAdapter import WebsterAdapter
from modules.Word.adapters.abstracts.DictionaryAdapter import DictionaryAdapter
from modules.Word.objects.Word import Word
from modules.Word.objects.WordArg import WordArg
from modules.Word.repositories.dictionary_repo import DictionaryRepo


class DictionaryManager:
    def __init__(self, **kwargs):
        self.dictionary_adapter: DictionaryAdapter = kwargs.get("dictionary_adapter") or WebsterAdapter()
        self.dictionary_repo: DictionaryRepo = kwargs.get("dictionary_repo") or DictionaryRepo()

    def is_word(self, word: str) -> bool:
        word = re.sub(r"^\W+|\W+$", "", word)
        if not self.dictionary_adapter.is_english(word) or \
                self.dictionary_adapter.contains_number(word) or \
                len(word) == 0:
            return False
        result = self.dictionary_repo.load_word(word.upper())
        if len(result.get_data()) > 0:
            return True
        return self.__create_word(word) is not None

    def get_words(self, args: WordArg, word_length: int) -> Result:
        pass

    def __create_word(self, word: str) -> Word or None:
        is_word = self.dictionary_adapter.is_word(word)
        if is_word:
            word = word.upper()
            result = self.dictionary_repo.insert_word(word)
            return Word(result.get_insert_id(), word, word[0])
        return None
