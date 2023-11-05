"""
Runtime
54ms
Beats 92.68%of users with Python3
Memory
19.98MB
Beats 64.31%of users with Python3
"""

from typing import List

"""
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.integers = []
        for nested_integer in nestedList:  # type: NestedInteger
            self.__process_nested_integer(nested_integer)
        self.length = len(self.integers)
        self.index = -1

    def __process_nested_integer(self, nested_integer: NestedInteger):
        if nested_integer.isInteger():
            self.integers.append(nested_integer.getInteger())
        else:
            for even_more_nested_integer in nested_integer.getList():
                self.__process_nested_integer(even_more_nested_integer)

    def next(self) -> int:
        if self.index < self.length - 1:
            self.index += 1
        return self.integers[self.index]

    def hasNext(self) -> bool:
        return self.index < self.length - 1


# nestedList = [[1, 1], 2, [1, 1]]
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# assert v == [1, 1, 2, 1, 1]
#
# nestedList = [1, [4, [6]]]
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# assert v == [1, 4, 6]
