from typing import List
from math import ceil


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        result = self.getRow(rowIndex - 1)

        rowIndex += 1
        result_len = ceil(rowIndex / 2)
        result = result[:result_len]
        new_result = [1]
        for i in range(1, result_len):
            new_result.append(result[i] + result[i - 1])
            i += 1

        result = new_result
        inverted = result.copy()
        if rowIndex % 2 != 0:
            inverted = inverted[:-1]
        inverted.reverse()
        return result + inverted


a = Solution()
assert a.getRow(0) == [1]
assert a.getRow(1) == [1, 1]
assert a.getRow(2) == [1, 2, 1]
assert a.getRow(3) == [1, 3, 3, 1]
assert a.getRow(4) == [1, 4, 6, 4, 1]
assert a.getRow(5) == [1, 5, 10, 10, 5, 1]
