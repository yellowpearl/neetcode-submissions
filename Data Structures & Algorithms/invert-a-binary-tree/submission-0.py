# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = deque()
        if root:
            d.append(root)
        while d:
            curr = d.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                d.append(curr.left)
            if curr.right:
                d.append(curr.right)
        return root

