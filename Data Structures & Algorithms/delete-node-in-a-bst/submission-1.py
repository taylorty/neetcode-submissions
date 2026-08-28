# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
        
            # Finds the in-order successor (minimum node in the right subtree)
            node = curr = root.right
            while curr.left:
                curr = curr.left
            
            # Method 1:
            # curr.left = root.left
            # root = node

            # Method 2:
            # curr.left = root.left
            # return root.right

            # Method 3:
            # Replaces current node value and deletes successor
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        return root