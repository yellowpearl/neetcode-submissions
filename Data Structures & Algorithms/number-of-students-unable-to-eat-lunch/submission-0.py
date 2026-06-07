from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        stack = sandwiches[::-1]

        l = len(stack)
        j = 0
        while l != j:
            l = len(stack)
            for i in range(len(stack)):
                s = queue.popleft()
                if stack[-1] == s:
                    stack.pop()
                else:
                    queue.append(s)
            j = len(stack)
        return j
            