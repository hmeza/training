from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # look nums
        # in case current number is odd, find an even and switch
        i = 0
        j = len(nums) - 1
        while i < len(nums):
            if nums[i] % 2 != 0:
                while j > i and nums[j] % 2 != 0:
                    j -= 1
                if j > i and nums[j] % 2 == 0:
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1


a = Solution()
nums = [1, 2, 6, 3, 1, 7, 8, 4, 3, 4, 5, 6, 8, 8, 4, 2, 2, 5, 6, 7, 2, 2, 5000, 1, 5, 7, 5634]
a.sortArrayByParity(nums)
print(nums)
