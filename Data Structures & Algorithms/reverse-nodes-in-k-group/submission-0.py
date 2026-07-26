# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode()
        group_prev = dummy
        prev = None
        while curr:
            prev_head = curr

            check = curr
            count = 0
            while count < k and check:
                check = check.next
                count += 1
            
            if count == k:
                prev = None
                for i in range(k):
                    tmp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = tmp
            else:
                group_prev.next = curr
                break
            
            if not dummy.next:
                dummy.next = prev
            prev_head.next = curr

            group_prev.next = prev
            group_prev = prev_head

        return dummy.next

