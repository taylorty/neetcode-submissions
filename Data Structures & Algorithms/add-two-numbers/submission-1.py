# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        head = dummyNode
        carry = 0
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val + carry
                l1 = l1.next
            elif l2:
                val = l2.val + carry
                l2 = l2.next
            carry = val // 10
            val = val % 10
            head.next = ListNode(val)
            head = head.next
        if carry:
            head.next = ListNode(carry)
        return dummyNode.next