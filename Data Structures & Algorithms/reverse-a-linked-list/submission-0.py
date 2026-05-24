# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        
        head = stack.pop()
        cur = head
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return head

            