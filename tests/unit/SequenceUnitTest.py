import unittest
from modules.Word.managers.SequenceManager import SequenceManager
import math


class SequenceUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.sequence_manager: SequenceManager = SequenceManager()

    def test_get_permutations_no_conditions_returns_results(self):
        characters = "ABC"
        permutation = self.sequence_manager.search_permutations(characters)
        self.assertEqual(math.factorial(len(characters)), len(permutation.get_result()))

    def test_get_permutations_too_complex_raises_exception(self):
        characters = "AAAAAAAAAAAAA"
        with self.assertRaises(Exception) as context:
            self.sequence_manager.search_permutations(characters)

    def test_get_permutations_with_length_returns_result(self):
        characters = "ABC"
        sequence_length = 2
        permutation = self.sequence_manager.search_permutations(characters, sequence_length=sequence_length)
        n = len(characters)
        count = int(math.factorial(n) / math.factorial(n - sequence_length))
        self.assertEqual(count, len(permutation.get_result()))

    def test_get_permutations_with_prefix_returns_result(self):
        characters = "PPU"
        prefixes = ["PU"]
        permutation = self.sequence_manager.search_permutations(characters, prefixes=prefixes)
        results = permutation.get_result()
        self.assertEqual(1, len(results))
        self.assertIsNotNone(results.get("PUP"))

    def test_get_permutations_with_suffixes_returns_result(self):
        characters = "PPU"
        suffixes = ["UP"]
        permutation = self.sequence_manager.search_permutations(characters, suffixes=suffixes)
        results = permutation.get_result()
        self.assertEqual(1, len(results))
        self.assertIsNotNone(results.get("PUP"))

    def test_get_permutations_with_contains_returns_result(self):
        characters = "PPU"
        contains = ["PUP"]
        permutation = self.sequence_manager.search_permutations(characters, contains=contains)
        results = permutation.get_result()
        self.assertEqual(1, len(results))
        self.assertIsNotNone(results.get("PUP"))

    def test_get_permutations_with_regex_returns_result(self):
        characters = "PPU"
        regexes = ["P-P"]
        permutation = self.sequence_manager.search_permutations(characters, regexes=regexes)
        results = permutation.get_result()
        self.assertEqual(1, len(results))
        self.assertIsNotNone(results.get("PUP"))

    def test_get_permutations_with_excludes_returns_result(self):
        characters = "PPU"
        excludes = ["P-P", "-PP"]
        permutation = self.sequence_manager.search_permutations(characters, excludes=excludes)
        results = permutation.get_result()
        self.assertEqual(1, len(results))
        self.assertIsNotNone(results.get("PPU"))
