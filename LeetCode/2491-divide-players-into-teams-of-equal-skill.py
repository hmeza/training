from typing import List
"""
Runtime 46ms Beats 49.80%
Memory 27.36 MB Beats 98.96%
"""


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        skill_value = None
        chemistry = 0
        skills_len = len(skill)
        for i in range(0, int(skills_len / 2)):
            a, b = skill[i], skill[skills_len - i - 1]
            if skill_value and skill_value != a + b:
                return -1
            elif not skill_value:
                skill_value = skill[i] + skill[skills_len - i - 1]
            chemistry += skill[i] * skill[skills_len - i - 1]
        return chemistry


a = Solution()
assert a.dividePlayers(skill=[3, 2, 5, 1, 3, 4]) == 22
assert a.dividePlayers(skill=[3, 4]) == 12
assert a.dividePlayers(skill=[1, 1, 2, 3]) == -1
