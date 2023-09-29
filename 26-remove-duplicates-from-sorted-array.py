from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_element = -101
        last_index = 0
        for i in range(0, len(nums)):
            if nums[i] > last_element:
                last_element = nums[i]
                nums[last_index] = last_element
                last_index += 1
        return last_index


a = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = a.removeDuplicates(nums)
print(nums)
print(k)
