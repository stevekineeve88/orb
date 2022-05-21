import json
from server.modules.orb.objects.orb import Orb
from server.modules.orb.objects.word_collection import WordCollection


class OrbManager:
    """ Manager for searching orbs
    """

    def __init__(self):
        """ Constructor for OrbManager
        """
        with open("server/words.json") as file:
            self.__words = json.load(file)

    def search_words(self, characters: str, size: int) -> WordCollection:
        """ Search for words in character string
        Args:
            characters (str):           Random characters
            size (int):                 Size of outputted words
        Returns:
            WordCollection
        """
        orb = Orb(characters.lower())
        permutations = orb.get_permutations(size)

        output = []
        for key, value in permutations.items():
            if key in self.__words:
                output.append(key)
        return WordCollection(output)
