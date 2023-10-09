from typing import List


class Solution:
    def __init__(self):
        self.target = None
        self.nums = None
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        self.target = target
        self.nums = nums

        result = [self.findMin(0, len(self.nums) - 1), self.findMax(0, len(nums) - 1)]
        print(result)
        return result

    def findMin(self, pivot_min, pivot_max):
        if pivot_max - pivot_min < 2:
            if self.nums[pivot_min] == self.target:
                return pivot_min
            return pivot_max if self.nums[pivot_max] == self.target else -1

        pivot = (pivot_max - pivot_min) // 2 + pivot_min
        if self.nums[pivot] >= self.target:
            return self.findMin(pivot_min, pivot)
        else:
            return self.findMin(pivot, pivot_max)

    def findMax(self, pivot_min, pivot_max):
        if pivot_max - pivot_min < 2:
            if self.nums[pivot_max] == self.target:
                return pivot_max
            return pivot_min if self.nums[pivot_min] == self.target else -1

        pivot = (pivot_max - pivot_min) // 2 + pivot_min
        if self.nums[pivot] <= self.target:
            return self.findMax(pivot, pivot_max)
        else:
            return self.findMax(pivot_min, pivot)


a = Solution()

# a.target = 6
# a.nums = [5, 7, 7, 8, 8, 10]
# assert a.findMin(0, len(a.nums) - 1) == -1
# a.target = 8
# a.nums = [5, 7, 7, 8, 8, 10]
# assert a.findMin(0, len(a.nums) - 1) == 3
# a.target = 7
# a.nums = [5, 7, 7, 8, 8, 10]
# assert a.findMin(0, len(a.nums) - 1) == 1
# a.target = 5
# a.nums = [5, 7, 7, 8, 8, 10]
# assert a.findMin(0, len(a.nums) - 1) == 0
# a.target = 10
# a.nums = [5, 7, 7, 8, 8, 10]
# assert a.findMin(0, len(a.nums) - 1) == 5

assert a.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
assert a.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
assert a.searchRange(nums=[], target=0) == [-1, -1]
nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
assert a.searchRange(nums=nums, target=8) == [0, len(nums) - 1]
assert a.searchRange(nums=[1, 3], target=1) == [0, 0]
assert a.searchRange(nums=[1, 2, 3], target=3) == [2, 2]
