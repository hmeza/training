"""
Runtime
31ms
Beats 96.05%of users with Python3
Memory
16.19MB
Beats 94.64%of users with Python3
"""

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        xy_max = max(abs(sx-fx), abs(sy-fy))
        if t == 1 and sx == fx and sy == fy:
            return False
        return xy_max <= t
