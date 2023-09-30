from typing import List


class Solution:
        def mergeAlternately(self, word1: str, word2: str) -> str:
            i = 0
            j = 0
            result = ""
            while i < len(word1) or j < len(word2):
                if i < len(word1):
                    result += word1[i]
                if j < len(word2):
                    result += word2[j]
                i += 1
                j += 1
            return result


a = Solution()
assert a.mergeAlternately("abc", "pqr") == "apbqcr"
assert a.mergeAlternately("ab", "pqrs") == "apbqrs"
assert a.mergeAlternately("abcd", "pq") == "apbqcd"
assert a.mergeAlternately("", "") == ""
assert a.mergeAlternately("", "a") == "a"
assert a.mergeAlternately("a", "") == "a"

