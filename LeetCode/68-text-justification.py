from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        current_length = len(words[0])
        current_line = words[0]
        result = []
        for i in range(1, len(words)):
            if current_length + len(words[i]) + 1 > maxWidth:
                current_line = self.cjust(current_line, maxWidth)
                result.append(current_line)
                current_line = words[i]
                current_length = len(current_line)
            else:
                current_line += " " + words[i]
                current_length += len(words[i]) + 1
        current_line = current_line.ljust(maxWidth, " ")
        result.append(current_line)
        return result

    def cjust(self, string, maxWidth):
        split = string.split(" ")
        index = 0
        while len("".join(split)) < maxWidth:
            split[index] += " "
            index += 1
            if index >= len(split) - 1:
                index = 0
        return "".join(split)


a = Solution()
assert a.fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16) == [
    "This    is    an",
    "example  of text",
    "justification.  "
]
assert a.fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16) == [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
]

assert a.fullJustify(words=["The", "important", "thing", "is", "not", "to", "stop", "questioning.", "Curiosity", "has", "its", "own", "reason", "for", "existing."], maxWidth=17) == [
    "The     important",
    "thing  is  not to",
    "stop questioning.",
    "Curiosity has its",
    "own   reason  for",
    "existing.        "
]

assert a.fullJustify(
    words=["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do", "for",
           "your", "country"], maxWidth=16) == [
    "ask   not   what", "your country can", "do  for  you ask",
    "what  you can do", "for your country"
]
