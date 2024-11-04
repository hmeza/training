"""
Runtime 199 ms Beats 72.79%
Memory 18.83 MB Beats 93.11%
"""


class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        j = 1
        counter = 9
        word_len = len(word)
        comp = ""
        while i < word_len:
            c = word[i]
            while j < word_len and word[j] == c and counter > 1:
                counter -= 1
                j += 1
            comp += f"{9-counter+1}{c}"
            counter = 9
            i = j
            j += 1
        return comp


a = Solution()
assert a.compressedString(word="abcde") == "1a1b1c1d1e"
assert a.compressedString(word="aaaaaaaaaaaaaabb") == "9a5a2b"
