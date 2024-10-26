"""
Runtime 34ms Beats 99.93%
Memory 17.13MB Beats 97.73%
"""


class Solution:
    def minimumSteps(self, s: str) -> int:
        zeroes = 0
        acum = 0
        for s in reversed(s):
            if s == '0':
                zeroes += 1
            else:
                acum += zeroes
        return acum


a = Solution()
assert a.minimumSteps("101") == 1
assert a.minimumSteps("100") == 2
assert a.minimumSteps("") == 0
assert a.minimumSteps("10101010") == 10
