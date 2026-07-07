# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if not subRoot:
        #     return True
        # if not root:
        #     return False
        if self.isSubtreeHelper(root, subRoot):
            return True
        else:
            val = False
            if root.left:
                val = val or self.isSubtree(root.left, subRoot)
            if root.right:
                val = val or self.isSubtree(root.right, subRoot)
            return val

    
    def isSubtreeHelper(self, root, subRoot):
        if root and subRoot and root.val != subRoot.val:
            return False
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        # if root and subRoot and root.left == subRoot.left and root.right == subRoot.right:
        #     return True
        return self.isSubtreeHelper(root.left, subRoot.left) and self.isSubtreeHelper(root.right, subRoot.right)
        # if root and subRoot and root.val == subRoot.val:
        #     return self.isSubtreeHelper(root.left, subRoot.left) and self.isSubtreeHelper(root.right, subRoot.right)
        # return False