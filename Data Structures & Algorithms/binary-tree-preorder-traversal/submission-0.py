# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        curr = None
        res = []
        while stack or curr:
            if curr:
                res.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
                if stack:
                    curr = stack.pop()
                else:
                    curr = None
            else:
                if stack:
                    curr = stack.pop()
                else:
                    curr = None
        return res