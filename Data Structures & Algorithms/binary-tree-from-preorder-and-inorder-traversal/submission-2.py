# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        length = inorder.index(preorder[0])
        # print(preorder[1: min(length + 2, len(preorder))], inorder[:index])
        # print(preorder[length + 2:], inorder[index + 2:])
        root.left = self.buildTree(preorder[1: length + 1], inorder[:length])
        root.right = self.buildTree(preorder[length + 1:], inorder[length + 1:])
        return root