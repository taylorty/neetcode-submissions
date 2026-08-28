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
            return None
        nodeCopy = Node(node.val)
        graph = {node: nodeCopy}
        q = deque()
        q.append(node)
        # graph[node] = nodeCopy
        while q:
            curr = q.popleft()
            if curr in graph:
                newNode = graph[curr]
            else:
                newNode = Node(curr.val)
                graph[curr] = newNode
            # neighbors = []
            for neighbor in curr.neighbors:
                if neighbor in graph:
                    # neighbors.append(neighbor)
                    newNodeNeighbor = graph[neighbor]
                else:
                    newNodeNeighbor = Node(neighbor.val)
                    graph[neighbor] = newNodeNeighbor
                    q.append(neighbor)
                newNode.neighbors.append(newNodeNeighbor)

            # newNode.neighbors = neighbors
            
        return graph[node]

