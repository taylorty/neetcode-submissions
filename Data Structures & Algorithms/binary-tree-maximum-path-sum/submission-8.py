# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = -float('inf')
        self.helper(root)
        return self.result
    
    def helper(self, root):
        if not root:
            return 0

        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        self.result = max(self.result, left + right + root.val)
        return max(0, max(left, right, 0) + root.val)