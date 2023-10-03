from typing import List
from math import floor


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available_letters = {}
        for i in range(len(magazine)):
            letter = magazine[i]
            if letter not in available_letters.keys():
                available_letters[letter] = 0
            available_letters[letter] += 1

        for i in range(len(ransomNote)):
            letter = ransomNote[i]
            if letter not in available_letters.keys() or available_letters[letter] <= 0:
                return False
            available_letters[letter] -= 1
        return True


a = Solution()
assert not a.canConstruct("a", "b")
assert not a.canConstruct("aa", "ab")
assert a.canConstruct("aa", "aab")
