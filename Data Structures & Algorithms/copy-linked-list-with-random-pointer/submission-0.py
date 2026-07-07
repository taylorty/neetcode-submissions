"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        m = {}
        curr = head
        newHead = Node(head.val)
        newCurr = newHead
        m[curr] = newCurr
        while curr:
            nextNode = curr.next
            if nextNode not in m and nextNode:
                m[nextNode] = Node(nextNode.val)
            if nextNode:
                newCurr.next = m[nextNode]

            randomNode = curr.random
            if randomNode not in m and randomNode:
                m[randomNode] = Node(randomNode.val)
            if randomNode:
                newCurr.random = m[randomNode]

            newCurr = newCurr.next
            curr = curr.next
        return newHead