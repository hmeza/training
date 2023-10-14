from typing import List
from functools import cache
from math import inf


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def find_min_money(position: int, time_cost: int) -> inf:
            if n - position <= time_cost:
                return 0
            if position >= n:
                return inf
            result = min(
                find_min_money(position + 1, time_cost + time[position]) + cost[position],
                find_min_money(position + 1, time_cost - 1)
            )
            return result

        n = len(cost)
        return find_min_money(0, 0)


a = Solution()
assert a.paintWalls(cost=[1, 2, 3, 2], time=[1, 2, 3, 2]) == 3
assert a.paintWalls(cost=[2, 3, 4, 2], time=[1, 1, 1, 1]) == 4
assert a.paintWalls(cost=[8, 7, 5, 15], time=[1, 1, 2, 1]) == 12
assert a.paintWalls(cost=[26, 53, 10, 24, 25, 20, 63, 51], time=[1, 1, 1, 1, 2, 2, 2, 1]) == 55
assert a.paintWalls(cost=[5, 5, 5, 5, 5, 5, 5], time=[1, 2, 1, 2, 1, 1, 1]) == 15



