from typing import List

"""
Runtime 48ms Beats 99.22%
Memory 35.74 MB Beats 44.69%
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for el in sorted(arr):
            if el not in rank:
                rank[el] = len(rank) + 1
        return list(map(rank.get, arr))


a = Solution()
assert a.arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]
assert a.arrayRankTransform([100, 100, 100]) == [1, 1, 1]
assert a.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]) == [5, 3, 4, 2, 8, 6, 7, 1, 3]
