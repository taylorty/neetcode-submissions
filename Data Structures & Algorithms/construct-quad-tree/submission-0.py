"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, length):
            val = grid[r][c]
            isLeaf = True

            for i in range(r, r + length):
                for j in range(c, c + length):
                    if grid[i][j] != val:
                        isLeaf = False
                        break
                if not isLeaf:
                    break

            if isLeaf:
                return Node(val == 1, isLeaf, None, None, None, None)
            half = length // 2
            topLeft = dfs(r, c, half)
            topRight = dfs(r, c + half, half)
            bottomLeft = dfs(r + half, c, half)
            bottomRight = dfs(r + half, c + half, half)

            return Node(True, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
        return dfs(0, 0, len(grid))