from modules.Word.objects.WordArg import WordArg


class Permutation(WordArg):

    __SEPARATOR = "-"

    def __init__(self, characters: str):
        super().__init__(characters)
        self.__result: dict = {}
        character_dict = {}
        for character in characters:
            character_dict[character] = (character_dict[character] + 1) if character in character_dict else 1
        self.__character_dict = character_dict

    def calculate(self, sequence_length: int):
        characters = list(self.get_characters())
        n = len(characters)
        self.__get_permutations(characters, "", n, sequence_length)

    def get_result(self) -> dict:
        return self.__result

    def get_result_set(self, offset: int, limit: int) -> dict:
        keys = list(self.__result.keys())
        ranged_keys = keys[offset: offset + limit]
        set_keys = {}
        for key in ranged_keys:
            set_keys[key] = self.__result[key]
        return set_keys

    def __check_correct_permutation(self, prefix: str) -> bool:
        prefix_dict = {}
        for character in prefix:
            prefix_dict[character] = (prefix_dict[character] + 1) if character in prefix_dict else 1
            if prefix_dict[character] > self.__character_dict[character]:
                return False
        return True

    def __get_permutations(self, characters, prefix, n, k):
        if k == 0:
            if self.checks_pass(prefix):
                self.__result[prefix] = (self.__result[prefix] + 1) if prefix in self.__result else 1
            return

        for i in range(n):
            new_prefix = prefix + characters[i]
            if self.__check_correct_permutation(new_prefix):
                self.__get_permutations(characters, new_prefix, n, k - 1)
