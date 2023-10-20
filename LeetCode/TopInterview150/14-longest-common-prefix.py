"""
Runtime
36ms
Beats 86.26%of users with Python3
Memory
16.22MB
Beats 78.06%of users with Python3
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_length = strs[0] if strs else ""
        current_common_letters = ""
        k = 0
        while k < len(strs) - 1:
            st1 = strs[k]
            st2 = strs[k+1]
            for i in range(min(len(st1), len(st2))):
                if st1[i] == st2[i]:
                    current_common_letters += st1[i]
                else:
                    break
            if len(current_common_letters) < len(max_length):
                max_length = current_common_letters
            current_common_letters = ""
            k += 1

        return max_length


a = Solution()
assert a.longestCommonPrefix(strs=["flower", "flow", "flight"]) == "fl"
assert a.longestCommonPrefix(strs=["dog", "racecar", "car"]) == ""
assert a.longestCommonPrefix(strs=["plate", "place"]) == "pla"
assert a.longestCommonPrefix(strs=["assertion", "assert"]) == "assert"
assert a.longestCommonPrefix(strs=["assertion", "assert", "no", "common"]) == ""
assert a.longestCommonPrefix(strs=["a"]) == "a"
assert a.longestCommonPrefix(strs=[]) == ""
