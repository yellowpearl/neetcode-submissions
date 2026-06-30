# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        d = deque([root])
        res = [root.val]
        while len(d) > 0:
            first = None
            for i in range(len(d)):
                curr = d.popleft()
                if curr.right:
                    d.append(curr.right)
                    if first is None:
                        first = curr.right
                if curr.left:
                    d.append(curr.left)
                    if first is None:
                        first = curr.left
            if first is not None:
                res.append(first.val)

            
        return res

        