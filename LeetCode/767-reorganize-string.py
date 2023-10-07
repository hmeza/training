import operator


class Solution:
    def reorganizeString(self, s: str) -> str:
        letters = {}
        for letter in list(s):
            if letter not in letters.keys():
                letters[letter] = 0
            letters[letter] += 1

        result = []
        letters = dict(sorted(letters.items(), key=operator.itemgetter(1), reverse=True))
        index = list(letters.keys())[0]
        last = None
        delete_index = None
        while letters:
            if index == last:
                return ""
            result.append(index)
            last = index
            letters[index] -= 1

            # mark to delete
            if letters[index] <= 0:
                delete_index = index

            # find next index
            keys = list(letters.keys())
            index_position = keys.index(index)
            index = keys[index_position + 1] if len(keys) > index_position + 1 else keys[0]

            # delete
            if delete_index:
                del letters[delete_index]
                delete_index = None

        print("".join(result))
        return "".join(result)


a = Solution()
assert a.reorganizeString("vvvlo")
# assert a.reorganizeString("aab") == "aba"
# assert a.reorganizeString("aaab") == ""
# assert a.reorganizeString("aaabb") == "ababa"
# assert a.reorganizeString("aaabba") == ""
# assert a.reorganizeString("aaabbc")  # example "ababac", "abcaba
