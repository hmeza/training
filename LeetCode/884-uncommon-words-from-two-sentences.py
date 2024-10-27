from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        c1 = Counter(s1.split(" "))
        c2 = Counter(s2.split(" "))
        total = c1 + c2
        return [c for c, i in total.items() if i == 1]


a = Solution()
assert a.uncommonFromSentences(s1="this apple is sweet", s2="this apple is sour") == ["sweet", "sour"]
