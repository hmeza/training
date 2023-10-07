from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        minimum = len(nums) / 3

        current = None
        current_count = 0
        result = []
        for i in range(len(nums)):
            if current != nums[i]:
                if current_count > minimum:
                    result.append(current)
                current = nums[i]
                current_count = 1
            else:
                current_count += 1
        if current_count > minimum:
            result.append(current)
        return result

a = Solution()
assert a.majorityElement([3, 2, 3]) == [3]
assert a.majorityElement([1]) == [1]
assert a.majorityElement([1, 2]) == [1, 2]
