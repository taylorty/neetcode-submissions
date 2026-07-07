# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        curr = head
        while curr:
            if curr.next:
                total += 2
                curr = curr.next.next
            else:
                total += 1
                curr = curr.next
        curr2 = head
        prev = None
        count2 = 0
        if count2 == total - n:
            return curr2.next
        while curr2:
            if count2 == total - n:
                if not prev:
                    return
                prev.next = curr2.next
                break
            prev = curr2
            curr2 = curr2.next
            count2 += 1

        return head