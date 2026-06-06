# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next

        prev, cur = None, s
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        res = 0
        f, s = head, prev
        while s:
            res = max(res, f.val+s.val)
            s = s.next
            f = f.next
        return res
        



