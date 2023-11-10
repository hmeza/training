"""
Runtime
113ms
Beats 70.77%of users with Python3
Memory
17.14MB
Beats 93.66%of users with Python3
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        mod_val = 1_000_000_007
        result = 0
        count = 0
        current = None

        for c in s:
            count = count + 1 if c == current else 1
            current = c
            result += count
            result %= mod_val

        return result
