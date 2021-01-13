from decorators.timeout import timeout


class Permutation:

    __SEPARATOR = "-"

    def __init__(self, characters: str):
        self.__result: dict = {}
        self.__characters = characters
        self.__prefixes = []
        self.__suffixes = []
        self.__contains = []
        self.__regexes = []

    @timeout()
    def calculate(self, sequence_length: int):
        if sequence_length < 0 or sequence_length > len(self.__characters):
            raise Exception("Sequence length is out of bounds.")
        difference = len(self.__characters) - sequence_length
        self.__result = self.__get_permutations("", self.__characters, {}, difference)

    def get_result(self) -> dict:
        return self.__result

    def set_prefixes(self, prefixes: list):
        self.__prefixes = prefixes

    def set_suffixes(self, suffixes: list):
        self.__suffixes = suffixes

    def set_contains(self, contains: list):
        self.__contains = contains

    def set_regexes(self, regexes: list):
        self.__regexes = regexes

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
            if len(regex) != len(characters):
                continue
            is_regex = True
            for i in range(0, len(regex)):
                if regex[i] != characters[i] and regex[i] != self.__SEPARATOR:
                    is_regex = False
                    break
            if is_regex:
                return True
        return len(regexes) == 0

    def __is_allowed(self, characters: str) -> bool:
        return self.__has_prefixes(characters) and \
            self.__has_suffixes(characters) and \
            self.__has_contains(characters) and \
            self.__has_regexes(characters)

    def __get_permutations(self, subset: str, characters: str, permutations: dict, difference: int) -> dict:
        letters_length = len(characters)
        if letters_length == difference and self.__is_allowed(subset):
            if subset in permutations.keys():
                permutations[subset] = permutations[subset] + 1
            else:
                permutations[subset] = 1
        for i in range(0, letters_length):
            permutations.update(self.__get_permutations(
                subset + characters[i],
                characters[0:i] + characters[i + 1: letters_length],
                permutations,
                difference
            ))
        return permutations
