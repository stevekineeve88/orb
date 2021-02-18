class WordArg:
    __SEPARATOR = "-"

    def __init__(self, characters: str):
        self.__characters = characters
        self.__prefixes = []
        self.__suffixes = []
        self.__contains = []
        self.__regexes = []
        self.__excludes = []

    def get_characters(self) -> str:
        return self.__characters

    def set_prefixes(self, prefixes: list):
        self.__prefixes = prefixes

    def get_prefixes(self) -> list:
        return self.__prefixes

    def set_suffixes(self, suffixes: list):
        self.__suffixes = suffixes

    def get_suffixes(self) -> list:
        return self.__suffixes

    def set_contains(self, contains: list):
        self.__contains = contains

    def get_contains(self) -> list:
        return self.__contains

    def set_regexes(self, regexes: list):
        self.__regexes = regexes

    def get_regexes(self) -> list:
        return self.__regexes

    def set_excludes(self, excludes: list):
        self.__excludes = excludes

    def get_excludes(self) -> list:
        return self.__excludes

    def __check_prefixes(self, characters: str) -> bool:
        prefixes = self.__prefixes
        for prefix in prefixes:
            if characters.startswith(prefix):
                return True
        return len(prefixes) == 0

    def __check_suffixes(self, characters: str) -> bool:
        suffixes = self.__suffixes
        for suffix in suffixes:
            if characters.endswith(suffix):
                return True
        return len(suffixes) == 0

    def __check_contains(self, characters: str) -> bool:
        contains = self.__contains
        for contain in contains:
            if contain in characters:
                return True
        return len(contains) == 0

    def __check_regexes(self, characters: str) -> bool:
        regexes = self.__regexes
        for regex in regexes:
            if self.__is_matching_regex(characters, regex):
                return True
        return len(regexes) == 0

    def __check_excludes(self, characters: str) -> bool:
        excludes = self.__excludes
        for regex in excludes:
            if self.__is_matching_regex(characters, regex):
                return False
        return True

    def __is_matching_regex(self, characters: str, regex: str) -> bool:
        if len(regex) != len(characters):
            return False
        for i in range(0, len(regex)):
            if regex[i] != characters[i] and regex[i] != self.__SEPARATOR:
                return False
        return True

    def checks_pass(self, characters: str) -> bool:
        return self.__check_prefixes(characters) and \
               self.__check_suffixes(characters) and \
               self.__check_contains(characters) and \
               self.__check_regexes(characters) and \
               self.__check_excludes(characters)
