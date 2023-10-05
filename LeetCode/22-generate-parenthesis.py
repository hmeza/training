from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            # trivial case
            return ["()"]

        base_list = self.generateParenthesis(n - 1)

        # now add parenthesis to left if position is 0 and left is not "("
        # then balance right if right is not len(n) and right is not ")"
        result = []
        for formed_element in base_list:
            element_list = list(formed_element)
            i = 0
            while i < len(element_list):
                i += 1


a = Solution()
assert a.generateParenthesis(4) == ["(((())))", "((()()))", "((()))()", "()((()))", "(())(())", "(()()())", "()()()()"]
assert a.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
assert a.generateParenthesis(2) == ["(())", "()()"]
assert a.generateParenthesis(1) == ["()"]
