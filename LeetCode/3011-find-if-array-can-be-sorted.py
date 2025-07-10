from typing import List


class Solution:
    def _get_1s(self, number):
        return len((bin(number)[2:]).replace("0", ""))

    def canSortArray(self, nums: List[int]) -> bool:
        current = 0
        nums_len = len(nums)
        can_be_sorted = True
        while current + 1 < nums_len:
            if nums[current] > nums[current+1]:
                bin_1 = self._get_1s(nums[current])
                bin_2 = self._get_1s(nums[current+1])
                if bin_1 == bin_2:
                    nums[current], nums[current+1] = nums[current+1], nums[current]
                    current = max(0, current - 1)
                else:
                    can_be_sorted = False
                    break
            else:
                current += 1

        return can_be_sorted
