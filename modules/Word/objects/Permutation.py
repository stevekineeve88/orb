from decorators.timeout import timeout


class Permutation:

    __SEPARATOR = "-"

    def __init__(self, characters: str):
        self.__result: dict = {}
        self.__characters = list(characters)
        character_dict = {}
        for character in characters:
            character_dict[character] = (character_dict[character] + 1) if character in character_dict else 1
        self.__character_dict = character_dict
        self.__prefixes = []
        self.__suffixes = []
        self.__contains = []
        self.__regexes = []
        self.__excludes = []

    def calculate(self, sequence_length: int):
        n = len(self.__characters)
        self.__get_permutations(self.__characters, "", n, sequence_length)

    def get_result(self) -> dict:
        return self.__result

    def get_result_set(self, offset: int, limit: int) -> dict:
        keys = list(self.__result.keys())
        ranged_keys = keys[offset: offset + limit]
        set_keys = {}
        for key in ranged_keys:
            set_keys[key] = self.__result[key]
        return set_keys

    def set_prefixes(self, prefixes: list):
        self.__prefixes = prefixes

    def set_suffixes(self, suffixes: list):
        self.__suffixes = suffixes

    def set_contains(self, contains: list):
        self.__contains = contains

    def set_regexes(self, regexes: list):
        self.__regexes = regexes

    def set_excludes(self, excludes: list):
        self.__excludes = excludes

    def __has_prefixes(self, characters: str) -> bool:
        prefixes = self.__prefixes
        for prefix in prefixes:
            if characters.startswith(prefix):
                return True
        return len(prefixes) == 0

    def __has_suffixes(self, characters: str) -> bool:
        suffixes = self.__suffixes
        for suffix in suffixes:
            if characters.endswith(suffix):
                return True
        return len(suffixes) == 0

    def __has_contains(self, characters: str) -> bool:
        contains = self.__contains
        for contain in contains:
            if contain in characters:
                return True
        return len(contains) == 0

    def __has_regexes(self, characters: str) -> bool:
        regexes = self.__regexes
        for regex in regexes:
            if self.__is_matching(characters, regex):
                return True
        return len(regexes) == 0

    def __not_has_excludes(self, characters: str) -> bool:
        excludes = self.__excludes
        for regex in excludes:
            if self.__is_matching(characters, regex):
                return False
        return True

    def __is_matching(self, characters: str, regex: str) -> bool:
        if len(regex) != len(characters):
            return False
        for i in range(0, len(regex)):
            if regex[i] != characters[i] and regex[i] != self.__SEPARATOR:
                return False
        return True

    def __is_allowed(self, characters: str) -> bool:
        return self.__has_prefixes(characters) and \
            self.__has_suffixes(characters) and \
            self.__has_contains(characters) and \
            self.__has_regexes(characters) and \
            self.__not_has_excludes(characters)

    def __check_correct(self, prefix: str) -> bool:
        prefix_dict = {}
        for character in prefix:
            prefix_dict[character] = (prefix_dict[character] + 1) if character in prefix_dict else 1
            if prefix_dict[character] > self.__character_dict[character]:
                return False
        return True

    def __get_permutations(self, characters, prefix, n, k):
        if k == 0:
            if self.__is_allowed(prefix):
                self.__result[prefix] = (self.__result[prefix] + 1) if prefix in self.__result else 1
            return

        for i in range(n):
            new_prefix = prefix + characters[i]
            if self.__check_correct(new_prefix):
                self.__get_permutations(characters, new_prefix, n, k - 1)
