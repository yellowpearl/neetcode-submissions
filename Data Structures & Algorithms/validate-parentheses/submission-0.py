class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for sym in s:
            if not stack or m.get(sym) != stack[-1]:
                stack.append(sym)
            else:
                stack.pop()
        return not bool(stack)