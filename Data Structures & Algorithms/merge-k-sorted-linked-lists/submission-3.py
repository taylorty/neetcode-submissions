# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(pq, (l.val, i, l))
        dummy = ListNode(0)
        curr = dummy
        while pq:
            val, i, nextNode = heapq.heappop(pq)
            curr.next = nextNode
            if nextNode.next:
                heapq.heappush(pq, (nextNode.next.val, i, nextNode.next))
            curr = curr.next
        return dummy.next