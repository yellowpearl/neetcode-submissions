# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        res = None
        cur1 = list1
        cur2 = list2
        min_cur = None
        while cur1 or cur2:
            if not cur1 or (cur2 and cur2.val <= cur1.val):
                min_cur = cur2
                cur2 = cur2.next
            elif not cur2 or (cur1 and cur1.val <= cur2.val):
                min_cur = cur1
                cur1 = cur1.next
            
            if not head:
                head = min_cur
                res = head
            else:
                head.next = min_cur
                head = head.next

        return res
