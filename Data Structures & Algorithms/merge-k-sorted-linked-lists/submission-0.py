# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummyHead = ListNode()
        curr = dummyHead
        count = 0 # This acts as our tie-breaker
        for l in lists:
            if l:
                # Store (value, tie-breaker, node)
                heap.append((l.val, count, l))
                count += 1
        heapq.heapify(heap)
        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1
            curr = curr.next
        return dummyHead.next