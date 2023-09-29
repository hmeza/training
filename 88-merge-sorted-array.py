from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        m = m - 1
        n = n - 1
        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1


a = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
a.merge(nums1=nums1, m=3, nums2=[2, 5, 6], n=3)
assert nums1 == [1, 2, 2, 3, 5, 6]
nums1 = [1]
a.merge(nums1=[1], m=1, nums2=[], n=0)
assert nums1 == [1]
nums1 = [0]
a.merge(nums1=[0], m=0, nums2=[1], n=1)
assert nums1 == [1]
