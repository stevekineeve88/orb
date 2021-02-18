import unittest
from unittest.mock import patch, MagicMock
from modules.Util.result import Result
from modules.Word.managers.DictionaryManager import DictionaryManager
from modules.Word.objects.Word import Word
from modules.Word.repositories.dictionary_repo import DictionaryRepo


class SequenceUnitTest(unittest.TestCase):

    @classmethod
    @patch("modules.Word.repositories.dictionary_repo.DictionaryRepo")
    def setUpClass(cls, dictionary_repo) -> None:
        cls.dictionary_repo: DictionaryRepo = dictionary_repo
        cls.dictionary_manager: DictionaryManager = DictionaryManager(
            dictionary_repo=cls.dictionary_repo
        )

    def test_is_word_returns_boolean(self):
        correct_word = "JUMP"
        wrong_word = "JMP"
        self.dictionary_repo.load_word = MagicMock(return_value=Result())
        insert_result = Result()
        insert_result.set_insert_id(1)
        self.dictionary_repo.insert_word = MagicMock(return_value=insert_result)
        self.assertTrue(self.dictionary_manager.is_word(correct_word))
        self.assertFalse(self.dictionary_manager.is_word(wrong_word))
        self.dictionary_repo.insert_word.assert_called_once()

    def test_get_dictionary_words_with_prefix_returns_words(self):
        sequence = "MPUJ"
        prefixes = ["JU"]
        result = Result()
        result.set_data([
            Word(1, "JUMP", "J")
        ])
        self.dictionary_repo.load_words = MagicMock(return_value=result)
        result = self.dictionary_manager.get_words()
