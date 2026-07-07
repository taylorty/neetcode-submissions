# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list1 = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        
        list2 = prev
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2
            # newHead = newHead.next