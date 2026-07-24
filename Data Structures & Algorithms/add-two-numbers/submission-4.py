# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        c = 0
        while l1 or l2:
            if l1:
                s += l1.val * (10 ** c)
                l1 = l1.next
            if l2:
                s += l2.val * (10 ** c)
                l2 = l2.next
            c += 1
        
        if s == 0:
            return ListNode(0)
        else:
            prev = None
            head = None
            while s > 0:
                node = ListNode(s%10)
                if not prev:
                    prev = node
                    head = node
                else:
                    prev.next = node
                    prev = node
                s //= 10
            return head
            
        
                


