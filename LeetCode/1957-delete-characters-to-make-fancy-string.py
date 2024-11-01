"""
Runtime 271 ms Beats 82.88%
Memory 18.39 MB Beats 83.28%
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        index = 0
        window = 1
        fancy_string = ""
        s_len = len(s)
        while index < s_len:
            c = s[index]
            while window < s_len and s[window] == c:
                window += 1
            fancy_string += c if window - index == 1 else c+c
            index = window
            window += 1
        return fancy_string
