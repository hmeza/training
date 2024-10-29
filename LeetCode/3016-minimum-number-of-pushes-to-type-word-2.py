"""
Runtime 95ms Beats 94.07%
Memory 17.12 MB Beats 89.56%
"""


class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        c = Counter(word)
        b = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
        counter = 0
        result = 0
        increment = 1
        for i, n in b.items():
            counter += 1
            result += increment * n
            if counter == 8:
                counter = 0
                increment += 1
        return result


a = Solution()
assert a.minimumPushes(word="abcde") == 5
assert a.minimumPushes(word="xyzxyzxyzxyz") == 12
assert a.minimumPushes(word="aabbccddeeffgghhiiiiii") == 24
