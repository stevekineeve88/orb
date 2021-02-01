import math

from modules.Word.objects.Permutation import Permutation


class SequenceManager:

    __COMPLEXITY = 500000

    @classmethod
    def search_permutations(cls, characters: str, **kwargs) -> Permutation:
        sequence_length = kwargs.get("sequence_length") or len(characters)
        if cls.__is_complex(len(characters), sequence_length):
            raise Exception("Too complex for calculating permutations")
        permutation = Permutation(characters)
        permutation.set_prefixes(kwargs.get("prefixes") or [])
        permutation.set_suffixes(kwargs.get("suffixes") or [])
        permutation.set_contains(kwargs.get("contains") or [])
        permutation.set_regexes(kwargs.get("regexes") or [])
        permutation.set_excludes(kwargs.get("excludes") or [])
        permutation.calculate(sequence_length)
        return permutation

    @classmethod
    def __is_complex(cls, n: int, r: int) -> bool:
        return math.factorial(n) / math.factorial(n-r) > cls.__COMPLEXITY
