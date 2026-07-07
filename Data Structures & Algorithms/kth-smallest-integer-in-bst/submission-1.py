# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = 0
        
        self.count = 0
        self.helper(root, k)
        return self.val

    def helper(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        self.helper(root.left, k)
        self.count += 1
        if self.count == k:
            self.val = root.val
            return
        self.helper(root.right, k)