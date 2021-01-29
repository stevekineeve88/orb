import unittest
from modules.Word.managers.DictionaryManager import DictionaryManager


class SequenceUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.dictionary_manager: DictionaryManager = DictionaryManager()

    def test_is_word_returns_boolean(self):
        correct_word = "JUMP"
        wrong_word = "JMP"
        self.assertTrue(self.dictionary_manager.is_word(correct_word))
        self.assertFalse(self.dictionary_manager.is_word(wrong_word))
