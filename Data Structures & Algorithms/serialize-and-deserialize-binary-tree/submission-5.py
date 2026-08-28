# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        def helper(root):
            if not root:
                return "#"
            
            return "{},{},{}".format(str(root.val), helper(root.left), helper(root.right))
        return helper(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # print(data)
        splitted = data.split(",")
        index = 0
        def helper():
            nonlocal index
            if splitted[index] == "#":
                index += 1
                return None

            root = TreeNode(int(splitted[index]))
            index += 1

            root.left = helper()
            root.right = helper()
            return root
        return helper()
