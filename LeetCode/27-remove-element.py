from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
            i += 1
        return count


a = Solution()
nums = [3, 3]
r = a.removeElement(nums=nums, val=5)
assert r == 2
print(nums)
