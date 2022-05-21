from typing import List, Dict


class WordCollection:
    """ Object for managing collection of words
    """

    def __init__(self, words: List[str]):
        """ Constructor for WordCollection
        Args:
            words:
        """
        self.__words = words

    def get_words(self) -> List[str]:
        """ Get words
        Returns:
            List[str]
        """
        return self.__words

    def filter(self, char_map: Dict[int, str]) -> List[str]:
        """ Filter words with character map
        Args:
            char_map (Dict[int, str]):          Character map with key as index and value is matching character
        Returns:
            List[str]
        """
        output = []
        for word in self.__words:
            found = True
            for index, c in char_map.items():
                if index < 0 or index > len(word) or word[index] != c:
                    found = False
                    break
            if found:
                output.append(word)
        return output
