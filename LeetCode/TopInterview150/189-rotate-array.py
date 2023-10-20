"""
Runtime
170ms
Beats 93.33%of users with Python3
Memory
27.80MB
Beats 21.59%of users with Python3
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2:
            return
        k = k % length
        if k < 1:
            return
        nums[0:k], nums[k:] = nums[-k:], nums[0:length - k]


a = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
a.rotate(nums=nums, k=3)
assert nums == [5, 6, 7, 1, 2, 3, 4]

nums = [-1, -100, 3, 99]
a.rotate(nums=nums, k=2)
assert nums == [3, 99, -1, -100]
