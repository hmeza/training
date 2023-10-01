from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monotonic_increasing = None
        monotonic_decreasing = None
        is_monotonic = True
        try:
            for i in range(len(nums) - 1):
                if nums[i] == nums[i+1]:
                    # nothing to add
                    continue
                if not monotonic_increasing and not monotonic_decreasing:
                    if nums[i] < nums[i+1]:
                        monotonic_increasing = True
                    elif nums[i] > nums[i+1]:
                        monotonic_decreasing = True
                else:
                    if monotonic_increasing and nums[i] > nums[i+1]:
                        raise Exception(f"{i} ({nums[i]}) is not bigger than next one {i+1} ({nums[i+1]})")
                    if monotonic_decreasing and nums[i] < nums[i+1]:
                        raise Exception(f"{i} ({nums[i]}) is not smaller than next one {i+1} ({nums[i+1]})")
        except Exception as e:
            is_monotonic = False
        return is_monotonic


a = Solution()
assert a.isMonotonic(nums=[1, 2, 2, 3])
assert a.isMonotonic(nums=[6, 5, 4, 4])
assert a.isMonotonic(nums=[2, 2, 2, 2, 2, 2])
assert not a.isMonotonic(nums=[1, 3, 2])
assert not a.isMonotonic(nums=[1, 2, 3, 4, 5, 6, 5])
assert not a.isMonotonic(nums=[5, 4, 3, 2, 1, 1, 6])
