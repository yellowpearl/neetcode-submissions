# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 
# 1 2 3

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        # [1, 2, 3]
        n_head = head
        if head.next:
            n_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return n_head



        
        

            