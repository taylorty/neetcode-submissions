# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        # Process Root -> Left -> Right
        left_str = self.serialize(root.left)
        right_str = self.serialize(root.right)
        # Don't forget to cast root.val to a string!
        return str(root.val) + "," + left_str + "," + right_str

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split the data and create an iterator
        vals = iter(data.split(","))
        
        def helper():
            # Get the next value in the sequence
            val = next(vals)
            
            # Base case: if it's our null marker, there's no node here
            if val == "#":
                return None
                
            # Create the node (remember to cast back to int!)
            node = TreeNode(int(val))
            
            # Recursively build the left and right subtrees
            node.left = helper()
            node.right = helper()
            
            return node
            
        return helper()
            