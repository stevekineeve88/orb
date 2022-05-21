import unittest
from server.modules.orb.managers.orb_manager import OrbManager


class OrbManagerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.__orb_manager = OrbManager()

    def test_search_words_finds_correct_words(self):
        known = self.__orb_manager.search_words("WEIRPVE", 6)
        words = known.get_words()
        self.assertEqual(2, len(words))
        self.assertListEqual(["review", "viewer"], words)
