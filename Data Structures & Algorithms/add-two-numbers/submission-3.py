# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def i(node):
            c = 0
            s = 0
            while node:
                s += node.val * (10 ** c)
                node = node.next
                c += 1
            return s
        
        num = i(l1) + i(l2)
        curr = None
        prev = None
        head = None
        if num == 0:
            return ListNode(0)
        while num > 0:
            node = ListNode(num%10)
            if not prev:
                prev = node
                head = node
            else:
                prev.next = node
                prev = node
            num //= 10
        return head
            
        
                


