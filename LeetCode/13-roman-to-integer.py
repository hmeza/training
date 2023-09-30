from typing import List


class Solution:
    romanToIntValues = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        rti = 0
        i = 0
        romanToIntValueKeys = list(Solution.romanToIntValues.keys())
        while i < len(s):
            if i < len(s) - 1 and romanToIntValueKeys.index(s[i]) < romanToIntValueKeys.index(s[i+1]):
                rti += Solution.romanToIntValues[s[i+1]] - Solution.romanToIntValues[s[i]]
                i += 1
            else:
                rti += Solution.romanToIntValues[s[i]]
            i += 1
        return rti


a = Solution()
assert a.romanToInt("III") == 3
assert a.romanToInt("LVIII") == 58
assert a.romanToInt("MCMXCIV") == 1994

assert a.romanToInt("IV") == 4
assert a.romanToInt("IX") == 9
