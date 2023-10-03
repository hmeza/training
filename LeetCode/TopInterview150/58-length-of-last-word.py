from typing import List
from math import floor


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


a = Solution()
assert a.lengthOfLastWord("Hello World") == 5
assert a.lengthOfLastWord("fly me   to   the moon") == 4
assert a.lengthOfLastWord("luffy is still joyboy") == 6
