"""
Runtime
693ms
Beats 70.80%of users with Python3
Memory
32.01MB
Beats 81.91%of users with Python3
"""

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for i in range(len(dist)):
            dist[i] = ceil(dist[i] / speed[i])
        dist = sorted(dist)

        current = 0
        for i in range(len(dist)):
            if dist[i] <= current:
                return current
            current += 1
        return len(dist)
