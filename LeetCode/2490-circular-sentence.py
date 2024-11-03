"""
Runtime 0 ms Beats 100.00%
Memory 16.57 MB Beats 46.28%
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        start_letters = [w[0] for w in words]
        end_letters = [w[-1] for w in words]
        end_letters = [end_letters[-1]] + end_letters[:-1]

        for pack in zip(start_letters, end_letters):
            if pack[0] != pack[1]:
                return False
        return True


a = Solution()
assert a.isCircularSentence(sentence="leetcode exercises sound delightful")
