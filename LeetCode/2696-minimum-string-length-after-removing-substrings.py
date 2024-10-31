"""
Runtime 11 ms Beats 26.05%
Memory 16.68 MB Beats 15.85%
"""


class Solution:
    def minLength(self, s: str) -> int:
        as_list = list(s)
        index = 0
        while index < len(as_list) - 1:
            if as_list[index:index+2] in [['A', 'B'], ['C', 'D']]:
                as_list.pop(index+1)
                as_list.pop(index)
                index = index - 1 if index > 0 else 0
            else:
                index += 1
        return len(as_list)


a = Solution()
assert a.minLength(s="ABFCACDB") == 2
