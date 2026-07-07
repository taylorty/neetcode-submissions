# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        reach_end = False
        while q:
            
            size = len(q)
            children = []
            for i in range(size):
                
                curr = q.popleft()
                if not curr:
                    reach_end = True
                if reach_end and curr:
                    return False
                # if i == 0 and (curr.left or curr.right):
                #     hasChildren = True
                # if i == 0 and (curr.left or curr.right):
                #     hasChildren = False
                # if i != 0 and hasChildren == False:
                #     return False
                
                if curr and not curr.left and curr.right:
                    return False
                # if curr and (not curr.left and not curr.right) and q:
                #     return False
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                # if curr.left:
                #     if i != 0 and not children:
                #         return False
                #     children.append(curr.left)
                #     q.append(curr.left)
                # if curr.right:
                #     if i != 0 and not children:
                #         return False
                #     children.append(curr.right)
                    # q.append(curr.right)
            # if size % 2 != 0 and q:
            #     return False
        return True