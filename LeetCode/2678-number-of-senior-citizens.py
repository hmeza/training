from typing import List
"""
Runtime 0ms Beats 100.00%
Memory 16.72 MB Beats 18.18%
"""


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details:
            age_char = passenger[11]
            if age_char in ['7', '8', '9']:
                count += 1
            elif age_char == '6' and passenger[12] != '0':
                count += 1
        return count
