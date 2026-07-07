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
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)
        result = left + right + root.val
        self.result = max(self.result, result)
        return max(left, right) + root.val