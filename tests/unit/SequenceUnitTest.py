import unittest

from modules.Sequence.managers.SequenceManager import SequenceManager
import math


class SequenceUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.sequence_manager: SequenceManager = SequenceManager()

    def test_get_permutations_no_conditions_returns_results(self):
        characters = "ABC"
        results = self.sequence_manager.search_permutations(characters)
        self.assertEqual(math.factorial(len(characters)), len(results))

    def test_get_permutations_too_long_raises_exception(self):
        characters = "AAAAAAAAAAAAA"
        with self.assertRaises(Exception) as context:
            self.sequence_manager.search_permutations(characters)

    def test_get_permutations_with_length_returns_result(self):
        characters = "ABC"
        sequence_length = 2
        results = self.sequence_manager.search_permutations(characters, sequence_length=sequence_length)
        n = len(characters)
        count = int(math.factorial(n) / math.factorial(n - sequence_length))
        self.assertEqual(count, len(results))

    def test_get_permutations_with_prefix_returns_result(self):
        characters = "PPU"
        prefixes = ["PU"]
        results = self.sequence_manager.search_permutations(characters, prefixes=prefixes)
        self.assertEqual(1, len(results))
        self.assertIsNotNone(results.get("PUP"))

    def test_get_permutations_with_suffixes_returns_result(self):
        characters = "PPU"
        suffixes = ["UP"]
        results = self.sequence_manager.search_permutations(characters, suffixes=suffixes)
        self.assertEqual(1, len(results))
        self.assertIsNotNone(results.get("PUP"))

    def test_get_permutations_with_contains_returns_result(self):
        characters = "PPU"
        contains = ["PUP"]
        results = self.sequence_manager.search_permutations(characters, contains=contains)
        self.assertEqual(1, len(results))
        self.assertIsNotNone(results.get("PUP"))

    def test_get_permutations_with_regex_returns_result(self):
        characters = "PPU"
        regexes = ["P-P"]
        results = self.sequence_manager.search_permutations(characters, regexes=regexes)
        self.assertEqual(1, len(results))
        self.assertIsNotNone(results.get("PUP"))
