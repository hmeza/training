from typing import List
"""
Runtime 0 ms Beats 100.00%
Memory 16.41 MB Beats 76.59%

"""


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        for c1, c2 in zip(heights, sorted_heights):
            count += 1 if c1 != c2 else 0
        return count
