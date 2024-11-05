"""
Runtime 0 ms Beats 100.00%
Memory 16.43 MB Beats 77.64%
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        rotations = 0
        max_rotations = len(s)
        while s != goal and rotations < max_rotations:
            s = s[1:] + s[0]
            rotations += 1
        return s == goal
