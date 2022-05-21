import unittest
from server.modules.orb.objects.orb import Orb


class OrbTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.__orb = Orb("tca")

    def test_get_permutations_gets_correct_permutations(self):
        permutations = self.__orb.get_permutations(3)
        self.assertEqual(6, len(permutations))
        self.assertListEqual([
            "tca",
            "cat",
            "tac",
            "act",
            "atc",
            "cta"
        ], list(permutations.keys()))

    def test_get_permutations_returns_empty_on_size_too_large(self):
        self.assertEqual(0, len(self.__orb.get_permutations(4)))

    def test_get_permutations_returns_non_repeating(self):
        orb = Orb("cata")
        permutations = orb.get_permutations(3)
        self.assertEqual(12, len(permutations))
        self.assertTrue(permutations["tca"] > 1)
        self.assertTrue(permutations["cat"] > 1)
        self.assertTrue(permutations["tac"] > 1)
        self.assertTrue(permutations["act"] > 1)
        self.assertTrue(permutations["atc"] > 1)
        self.assertTrue(permutations["cta"] > 1)
