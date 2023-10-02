from typing import List


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        consecutive_a = 0
        consecutive_b = 0
        for i in range(1, len(colors) - 1):
            if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    consecutive_a += 1
                else:
                    consecutive_b += 1
        return consecutive_a > consecutive_b


a = Solution()
assert a.winnerOfGame(colors="AAABABB")
assert not a.winnerOfGame(colors="AA")
assert not a.winnerOfGame(colors="ABBBBBBBAAA")
assert not a.winnerOfGame(colors="ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB")
assert a.winnerOfGame(colors="AAAAAAAAA")
assert not a.winnerOfGame(colors="AAAABBBB")
