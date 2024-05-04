class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = version1.split(".")
        v2_parts = version2.split(".")

        v1 = 0
        v2 = 0
        mul = 1

        for i in range(max(len(v1_parts), len(v2_parts)) - 1, -1, -1):
            try:
                v1 += mul * int(v1_parts[i])
            except IndexError:
                pass

            try:    
                v2 += mul * int(v2_parts[i])
            except IndexError:
                pass

            j = i - 1
            try:
                mul_a = len(v1_parts[j])
            except IndexError:
                mul_a = 0

            try:
                mul_b = len(v1_parts[j])
            except IndexError:
                mul_b = 0

            try:
                mul *= 10 ** max(mul_a, mul_b)
            except IndexError:
                pass

        if v1 == v2:
            return 0
        return 1 if v1 > v2 else -1


