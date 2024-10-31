from typing import List
"""
Runtime 0ms Beats 100.00%
Memory 16.56 MB Beats 81.70%
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        odd_found = False
        longitude = 0
        for k, n in c.items():
            if n % 2 == 0:
                longitude += n
            else:
                odd_found = True
                longitude += n - 1
        if odd_found:
            longitude += 1
        return longitude
