from typing import List
"""
Runtime 0ms Beats 100.00%
Memory 16.94 MB Beats 16.18%
"""


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter
        a = Counter(arr)
        not_repeated = [el for el, n in a.items() if n == 1]
        return not_repeated[k-1] if len(not_repeated) >= k else ""
