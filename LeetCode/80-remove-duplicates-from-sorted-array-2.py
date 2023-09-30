from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_considered_number = ()
        k = 0
        i = 0
        times_shifted = 0
        len_nums = len(nums)
        while i < len(nums) - times_shifted:
            if last_considered_number == () or nums[i] != last_considered_number[0]:
                last_considered_number = (nums[i], 1)
                k += 1
                i += 1
            elif nums[i] == last_considered_number[0] and last_considered_number[1] < 2:
                last_considered_number = (last_considered_number[0], last_considered_number[1] + 1)
                k += 1
                i += 1
            elif nums[i] == last_considered_number[0] and last_considered_number[1] >= 2:
                # swap next one with current
                # do not increase k
                times_shifted = self._shift_left_remaining_list(i, len_nums, nums, times_shifted)
        return k

    def _shift_left_remaining_list(self, i, len_nums, nums, times_shifted):
        nums[i:len_nums - 1] = nums[i + 1:len_nums]
        times_shifted += 1
        return times_shifted


a = Solution()
nums = [1, 1, 1, 2, 2, 3]
r = a.removeDuplicates(nums)
print(nums)
assert r == 5, f"{r}"

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
r = a.removeDuplicates(nums)
print(nums)
assert r == 7, f"{r}"

nums = [0]
r = a.removeDuplicates(nums)
print(nums)
assert r == 1, f"{r}"

nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
r = a.removeDuplicates(nums)
print(nums)
assert r == 2, f"{r}"
