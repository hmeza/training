from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = sorted(arr, reverse=True)
        while arr:
            found = False
            i = arr.pop(0)
            for n, j in enumerate(arr):
                val = (i + j) % k
                if val == float(0):
                    arr.pop(n)
                    found = True
                    break
            if not found:
                return False
        return True


a = Solution()
assert a.canArrange(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5)
assert a.canArrange(arr=[1, 2, 3, 4, 5, 6], k=7)
assert not a.canArrange(arr=[1, 2, 3, 4, 5, 6], k=10)
