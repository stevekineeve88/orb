class Word:
    def __init__(self, word_id: int, word: str, category: str):
        self.__id = word_id
        self.__word = word
        self.__category = category

    def get_id(self):
        return self.__id

    def get_word(self):
        return self.__word

    def get_category(self):
        return self.__category
