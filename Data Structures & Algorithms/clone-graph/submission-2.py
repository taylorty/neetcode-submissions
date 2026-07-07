"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        m = defaultdict(Node)
        q = deque()
        q.append(node)
        copy = Node(node.val)
        m[node] = copy
        while q:
            curr = q.popleft()
            neigList = []
            for neig in curr.neighbors:
                copyNeig = None
                if neig in m:
                    copyNeig = m[neig]
                else:
                    copyNeig = Node(neig.val)
                    m[neig] = copyNeig
                    q.append(neig) 
                    # ensure that a node is added to the queue only the 
                    # first time you encounter it (when you create its copy)
                neigList.append(copyNeig)
            m[curr].neighbors = neigList
        return copy
            