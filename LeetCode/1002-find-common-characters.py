from typing import List
"""
Runtime 11 ms Beats 69.16%
Memory 16.74 MB Beats 35.62%
"""


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        counters = [dict(sorted(Counter(w).items())) for w in words]
        result = []
        for i in range(ord('a'), ord('z') + 1):
            c = chr(i)
            result += [c] * min([counter.get(c, 0) for counter in counters])
        return result


a = Solution()
print(a.commonChars(words=["bella", "label", "roller"]))
