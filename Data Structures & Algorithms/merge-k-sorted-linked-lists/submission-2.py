# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Tell Python how to compare ListNodes (by their values)
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        heap = []
        
        # 1. Add the head of each valid linked list to the heap array
        for l in lists:
            if l:
                heap.append(l)
                
        # 2. Transform the array into a valid min-heap
        heapq.heapify(heap)
        
        # 3. Dummy node to build our final merged list easily
        dummyHead = ListNode()
        curr = dummyHead
        
        # 4. Process the heap until it's empty
        while heap:
            # Pop the node with the smallest value
            node = heapq.heappop(heap) 
            
            # Attach it to our result list and move the pointer forward
            curr.next = node
            curr = curr.next
            
            # If there are more nodes in the list we just popped from, 
            # push the next node into the heap
            if node.next:
                heapq.heappush(heap, node.next)
                
        return dummyHead.next
        
"""
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummyHead = ListNode()
        curr = dummyHead
        count = 0 # This acts as our tie-breaker
        for l in lists:
            if l:
                heapq.heappush(heap, NodeWrapper(l))
                # Store (value, tie-breaker, node)
                # heap.append((l.val, count, l))
                # count += 1
        heapq.heapify(heap)
        while heap:
            node_wrapper = heapq.heappop(heap)
            # val, _, node = heapq.heappop(heap)
            curr.next = node_wrapper.node
            if node_wrapper.node.next:
                heapq.heappush(heap, NodeWrapper(node_wrapper.node.next))
                # heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1
            curr = curr.next
        return dummyHead.next
"""