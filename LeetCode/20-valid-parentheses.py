"""
Runtime 2ms Beats 26.76%
Memory 18.00MB Beats 10.02%
"""

class Solution:
    CORRESPONDENCE = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    def isValid(self, s: str) -> bool:
        i = 0
        stack = []
        while i < len(s):
            c = s[i]
            if c in Solution.CORRESPONDENCE.keys():
                if not stack:
                    return False
                d = stack[-1]
                if (d != Solution.CORRESPONDENCE[c]) :
                    return False
                stack.pop(-1)
            if c in Solution.CORRESPONDENCE.values():
                stack.append(s[i])
            i += 1
        return not stack

