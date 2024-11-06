"""
Runtime 23 ms Beats 47.30%
Memory 16.80 MB Beats 99.59%

"""


class Solution:
    def minChanges(self, s: str) -> int:
        s_len = len(s)
        n_changes = 0
        current = 0
        while current + 1 < s_len:
            if s[current] != s[current + 1]:
                n_changes += 1
            current += 2

        return n_changes


a = Solution()
assert a.minChanges(s="1001") == 2
assert a.minChanges(s="10") == 1
assert a.minChanges(s="0000") == 0
assert a.minChanges(s="010010") == 2
