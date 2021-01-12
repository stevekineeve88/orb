from itertools import combinations, permutations


class Combination:

    def __init__(self, search_string):
        self.__result = self.__get_combinations(search_string)

    def get_result(self):
        return self.__result

    @classmethod
    def __get_combinations(cls, word: str) -> list:
        subsets = [''.join(p) for i in range(1, len(word)) for p in combinations(word, i+1)]
        result = []
        for subset in subsets:
            perms = [''.join(p) for p in permutations(subset)]
            for perm in perms:
                if perm not in result:
                    result.append(perm)
        return result
