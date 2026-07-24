# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr, prev = head, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        curr, head2 = prev, prev
        prev = None
        c = 1
        while c < n:
            c += 1
            prev = curr
            curr = curr.next
        
        if prev:
            prev.next = curr.next
        else:
            head2 = curr.next

        curr, prev = head2, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev