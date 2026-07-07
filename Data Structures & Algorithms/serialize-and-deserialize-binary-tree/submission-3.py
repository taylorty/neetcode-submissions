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

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split the string into a list of values
        vals = data.split(",")
        index = 0
        
        def helper():
            nonlocal index # Tells Python to use the 'index' from the outer function
            
            # Prevent out-of-bounds errors (good safety practice)
            if index >= len(vals):
                return None
                
            val = vals[index]
            index += 1 # Move the pointer forward for the next recursive call
            
            # Base case: null marker
            if val == "#":
                return None
                
            # Create node and build subtrees
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            
            return node
            
        return helper()

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split the string and immediately convert it into a queue
        vals = deque(data.split(","))
        
        def helper():
            # Pop the very first element off the queue
            val = vals.popleft()
            
            # Base case: if it's our null marker, return None
            if val == "#":
                return None
                
            # Create the node (remember to convert back to integer)
            node = TreeNode(int(val))
            
            # Recursively build the left and right subtrees
            # Because we are popping from the queue, the remaining values
            # naturally shrink as the tree gets built.
            node.left = helper()
            node.right = helper()
            
            return node
            
        return helper()

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
            