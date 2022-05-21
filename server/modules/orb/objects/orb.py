from typing import Dict


class Orb:
    """ Object for managing orb operations on characters
    """

    def __init__(self, characters: str):
        """ Constructor for Orb
        Args:
            characters (str):           Random characters
        """
        self.__characters = characters

    def get_permutations(self, size: int) -> Dict[str, int]:
        """ Get permutations of characters
        Args:
            size (int):             Size of permutations
        Returns:
            Dict[str, int]
        """
        return self.__permute(self.__characters, size)

    def __permute(self, string: str, size: int) -> Dict[str, int]:
        """ Permute recursively
        Args:
            string (str):           Random characters
            size (int):             Size of permutation
        Returns:
            Dict[str, int]
        """
        if size == 1:
            output = {}
            for c in string:
                output[c] = output[c] + 1 if c in output else 1
            return output

        output = {}
        for i in range(0, len(string)):
            subsets = self.__permute(string[i+1:] + string[0:i], size-1)
            for key, count in subsets.items():
                first_perm = string[i] + key
                second_perm = key + string[i]
                output[first_perm] = output[first_perm] + 1 if first_perm in output else 1
                output[second_perm] = output[second_perm] + 1 if second_perm in output else 1
        return output
