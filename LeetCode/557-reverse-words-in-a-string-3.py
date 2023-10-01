from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([w[::-1] for w in s.split(" ")])


a = Solution()
assert a.reverseWords(s="Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert a.reverseWords("God Ding") == "doG gniD"
