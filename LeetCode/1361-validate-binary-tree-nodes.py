from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        roots = [0 for i in range(n)]
        valid = True
        try:
            for i in range(n):
                if leftChild[i] != -1:
                    roots[leftChild[i]] += 1
                if rightChild[i] != -1:
                    roots[rightChild[i]] += 1

            root = None
            for i in range(n):
                if roots[i] > 1:
                    raise ValueError(f"Node {i} has more than one root, roots {roots}")
                if roots[i] == 0:
                    if root is not None:
                        raise ValueError(f"Either no root or more than one root: {roots}")
                    root = i

            visited = [0 for i in range(n)]
            self.validate(root, visited, leftChild, rightChild)
            for i in visited:
                if i != 1:
                    raise ValueError("Not every node has been visited")
        except Exception as e:
            print(f"Error: {str(e)}")
            valid = False

        return valid

    def validate(self, node, visited, leftChild, rightChild):
        if node == -1:
            return False
        visited[node] += 1
        if sum(visited) >= len(leftChild):
            return False
        if leftChild[node] == -1 and rightChild[node] == -1:
            return False
        self.validate(leftChild[node], visited, leftChild, rightChild)
        self.validate(rightChild[node], visited, leftChild, rightChild)


a = Solution()
assert a.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1])
assert not a.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1])
assert not a.validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1])
assert not a.validateBinaryTreeNodes(n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1])
assert a.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1])
assert a.validateBinaryTreeNodes(n=4, leftChild=[3, -1, 1, -1], rightChild=[-1, -1, 0, -1])
assert not a.validateBinaryTreeNodes(n=4, leftChild=[1, 0, 3, -1], rightChild=[-1, -1, -1, -1])
assert a.validateBinaryTreeNodes(n=5, leftChild=[1, 3, -1, -1, -1], rightChild=[-1, 2, 4, -1, -1])
assert a.validateBinaryTreeNodes(n=4, leftChild=[3, -1, 1, -1], rightChild=[-1, -1, 0, -1])
assert not a.validateBinaryTreeNodes(n=4, leftChild=[1, 2, 0, -1], rightChild=[-1, -1, -1, -1])
