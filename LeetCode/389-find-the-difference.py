from typing import List


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        b = sorted(list(s))
        c = sorted(list(t))
        while b:
            l_b = b.pop()
            l_c = c.pop()
            if l_b != l_c:
                return l_c
        return c[0]


a = Solution()
assert a.findTheDifference(s="abcd", t="abcde") == "e"
assert a.findTheDifference(s="", t="y") == "y"
assert a.findTheDifference(s="a", t="aa") == "a"
