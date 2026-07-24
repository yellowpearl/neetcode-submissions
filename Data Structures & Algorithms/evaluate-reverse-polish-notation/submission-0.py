class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == '+':
                t2 = s.pop()
                t1 = s.pop()
                s.append(t1+t2)
            elif t == '-':
                t2 = s.pop()
                t1 = s.pop()
                s.append(t1-t2)
            elif t == '*':
                t2 = s.pop()
                t1 = s.pop()
                s.append(t1*t2)
            elif t == '/':
                t2 = s.pop()
                t1 = s.pop()
                s.append(int(t1/t2))
            else:
                s.append(int(t))
        return s.pop()