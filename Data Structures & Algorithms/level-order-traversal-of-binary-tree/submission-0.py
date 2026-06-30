# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        d = deque([root])
        while len(d) > 0:
            r = []
            for i in range(len(d)):
                curr = d.popleft()
                r.append(curr.val)
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
            res.append(r)
        return res
