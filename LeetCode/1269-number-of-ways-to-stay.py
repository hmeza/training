from typing import List
from math import inf


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        modulo = 1000000007

        result = [0] * min(steps // 2 + 1, arrLen)
        result[0] = 1

        for i in range(steps):
            new_ways = [0] * min(steps // 2 + 1, arrLen)
            for j, ways in enumerate(result):
                if ways > 0:
                    for possible_steps in (-1, 0, 1):
                        next_index = j + possible_steps
                        if 0 <= next_index < len(result):
                            new_ways[next_index] += ways
                            new_ways[next_index] %= modulo
            result = new_ways

        return result[0]


a = Solution()
# assert a.getWordsInLongestSubsequence(n=3, words=["bdb", "aaa", "ada"], groups=[2, 1, 3]) == ["aaa", "ada"]
