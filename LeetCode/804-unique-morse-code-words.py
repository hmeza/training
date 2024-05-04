from typing import List, Type


class Solution:
    letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        word_dict = {}
        for word in words:
            # convert word to morse
            # index word in word_dict
            word_dict[self._morse_representation(word)] = word
        return len(word_dict)

    def _morse_representation(self, word):
        morse_word = ''
        for letter in word:
            pos = ord(letter) - ord('a')
            morse_word += Solution.letters[pos]
        return morse_word


a = Solution()
assert 2 == a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
