"""
Runtime
500ms
Beats 98.37%of users with Python3
Memory
29.61MB
Beats 74.46%of users with Python3
"""

from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = 0
        rounds_won = 0
        for i in range(1, len(arr)):
            if arr[winner] > arr[i]:
                rounds_won += 1
            else:
                winner = i
                rounds_won = 1
            if rounds_won >= k:
                return arr[winner]
        return arr[winner]
