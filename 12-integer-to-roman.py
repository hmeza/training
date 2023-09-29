from typing import List
from math import floor


class Solution:
    romanToIntValues = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }

    def intToRoman(self, num: int) -> str:
        itr = ""
        keys = list(Solution.romanToIntValues.keys())
        while num > 0:
            k = keys[-1]
            keys.pop()
            if floor(num / k) > 0 or num == 1:
                letters = floor(num / k)
                num -= letters * k
                itr += Solution.romanToIntValues[k] * letters
            if len(keys) > 1 and num > keys[-2] and k > 1 and str(k)[0] == '1' and k - num <= keys[-2]:
                itr += "{}{}".format(Solution.romanToIntValues[keys[-2]], Solution.romanToIntValues[k])
                num -= (k - keys[-2])
            if len(keys) > 0 and num > keys[-1] and str(k)[0] == '5' and k - num <= keys[-1]:
                itr += "{}{}".format(Solution.romanToIntValues[keys[-1]], Solution.romanToIntValues[k])
                num -= (k - keys[-1])
        return itr


a = Solution()
assert a.intToRoman(3) == "III"
assert a.intToRoman(58) == "LVIII"
assert a.intToRoman(14) == "XIV"
assert a.intToRoman(1994) == "MCMXCIV", a.intToRoman(1994)

assert a.intToRoman(1) == "I"
assert a.intToRoman(4) == "IV"
assert a.intToRoman(49) == "XL"
assert a.intToRoman(9) == "IX"
assert a.intToRoman(99) == "XCIX"
assert a.intToRoman(900) == "CM"
assert a.intToRoman(400) == "CD"
assert a.intToRoman(41) == "XLI", a.intToRoman(41)
