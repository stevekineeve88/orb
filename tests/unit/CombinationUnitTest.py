import unittest

from modules.Combination.managers.CombinationManager import CombinationManager
import math


class CombinationUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.combination_manager: CombinationManager = CombinationManager()

    def test_get_unique_word_combos_no_conditions_returns_results(self):
        search_string = "ABC"
        combination = self.combination_manager.search(search_string)
        self.assertEqual(math.factorial(len(search_string)) - len(search_string), len(combination.get_result()))
