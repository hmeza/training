from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums = sorted(nums)
        numbers_set = {}
        for i in range(len(nums)):
            if nums[i] not in numbers_set.keys():
                numbers_set[nums[i]] = 1
            else:
                numbers_set[nums[i]] += 1

        good_pairs = 0
        for k, number in numbers_set.items():
            good_pairs += self._get_sum(number)
        return good_pairs

    def _get_sum(self, number):
        pairs = 0
        for i in range(number):
            pairs += i
        return pairs


a = Solution()
assert a.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]) == 4
assert a.numIdenticalPairs(nums=[1, 1, 1, 1]) == 6
assert a.numIdenticalPairs(nums=[1, 2, 3]) == 0
