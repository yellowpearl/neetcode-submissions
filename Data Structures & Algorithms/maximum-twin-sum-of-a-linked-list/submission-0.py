# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        stack_head = head
        # 5 4 2 1
        while stack_head:
            stack.append(stack_head.val)
            stack_head = stack_head.next
        
        # 5 4 2 1
        # 5 4 2 1
        # 5 + 1 = 6
        # 4 + 2 = 6
        # 2 + 4 = 6
        # 1 + 5 = 6
        res = 0
        while head:
            res = max(res, head.val+stack.pop())
            head = head.next
        return res


