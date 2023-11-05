from typing import List


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = []
        tt = []
        for letter in s:
            if letter == '#' and len(ss) > 0:
                ss.pop(len(ss) - 1)
            elif letter != '#':
                ss.append(letter)
        for letter in t:
            if letter == '#' and len(tt) > 0:
                tt.pop(len(tt) - 1)
            elif letter != '#':
                tt.append(letter)

        return "".join(ss) == "".join(tt)


a = Solution()
assert a.backspaceCompare(s="ab#c", t="ad#c")
assert a.backspaceCompare(s="ab##", t="c#d#")
assert not a.backspaceCompare(s="a#c", t="b")
assert a.backspaceCompare(s="#########ab##", t="c#d#")
assert a.backspaceCompare(s="ab##", t="########c#d#")
