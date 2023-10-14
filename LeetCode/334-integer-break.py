from typing import List


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        n -= 3
        real_result = 3
        while n > 0:
            if n - 3 <= 4:
                if n == 4:
                    new = 4
                else:
                    new = 3 if n % 3 == 0 else 2
            else:
                new = 3
            n -= new
            real_result *= new
        return real_result


a = Solution()
assert a.integerBreak(n=2) == 1
assert a.integerBreak(n=3) == 2
assert a.integerBreak(n=4) == 4
assert a.integerBreak(n=5) == 6
assert a.integerBreak(n=6) == 9
assert a.integerBreak(n=7) == 12
assert a.integerBreak(n=8) == 18
assert a.integerBreak(n=10) == 36
