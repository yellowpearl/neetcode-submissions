# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        head = None
        curr = None
        while True:
            min_link = None
            min_idx = None
            for idx, l in enumerate(lists):
                if l is None:
                    continue
                elif min_link is None:
                    min_link = l
                    min_idx = idx
                else:
                    if l.val < min_link.val:
                        min_link = l
                        min_idx = idx
            
            if min_link is None:
                break
            else:
                if head is None:
                    head = min_link
                    curr = min_link
                    lists[min_idx] = min_link.next
                else:
                    curr.next = min_link
                    curr = min_link
                    lists[min_idx] = min_link.next
        return head

            

            