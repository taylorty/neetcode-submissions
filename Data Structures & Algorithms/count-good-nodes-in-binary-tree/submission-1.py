# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper2(root, root.val)
        self.result = 0
        self.helper(root, root.val)
        return self.result

    def helper2(self, root, maxSoFar):
        if not root:
            return 0
        result = 0
        if root.val >= maxSoFar:
            result += 1
        maxSoFar = max(maxSoFar, root.val)
        result += self.helper2(root.left, maxSoFar)
        result += self.helper2(root.right, maxSoFar)
        return result

    def helper(self, root, maxSoFar):
        if not root:
            return
        if root.val >= maxSoFar:
            self.result += 1
        maxSoFar = max(maxSoFar, root.val)
        self.helper(root.left, maxSoFar)
        self.helper(root.right, maxSoFar)
