import unittest
from server.modules.orb.objects.word_collection import WordCollection


class WordCollectionTest(unittest.TestCase):
    def test_filter_filters_word_collection(self):
        words = ["test", "tast"]
        word_collection = WordCollection(words)
        filtered = word_collection.filter({
            1: "e"
        })
        self.assertEqual(1, len(filtered))
        self.assertEqual("test", filtered[0])
