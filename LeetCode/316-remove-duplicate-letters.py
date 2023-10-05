from typing import List


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            letter = s[i]
            if letter in result:
                index = result.index(letter)
                if ord(result[index + 1]) < ord(letter):
                    del result[index]
                    result.append(letter)
                # for j in range(index + 1, len(result)):
                #     if ord(result[j]) < ord(letter):
                #         del result[index]
                #         result.append(letter)
            else:
                result.append(letter)
            print(result)
        print("".join(result))
        return "".join(result)


a = Solution()
assert a.removeDuplicateLetters("bcabc") == "abc"
assert a.removeDuplicateLetters("cbacdcbc") == "acdb"
assert a.removeDuplicateLetters("abacb") == "abc"
assert a.removeDuplicateLetters("adacd") == "acd"
