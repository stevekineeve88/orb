from modules.Combination.objects.Combination import Combination


class CombinationManager:

    @classmethod
    def search(cls, search_string: str) -> Combination:
        return Combination(search_string)
