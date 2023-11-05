"""
Runtime
37ms
Beats 76.59%of users with Python3
Memory
16.38MB
Beats 67.50%of users with Python3
"""
from typing import List
import re


class Solution:
    def reverseWords(self, s: str) -> str:
        ss = re.sub(r"(\s+)", " ", s.strip())
        ss = ss.split()
        ss.reverse()
        return " ".join(ss)


a = Solution()
assert a.reverseWords(s="the sky is blue") == "blue is sky the"
assert a.reverseWords(s="  hello world  ") == "world hello"
assert a.reverseWords(s="a good   example") == "example good a"
