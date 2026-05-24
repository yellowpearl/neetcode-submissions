class MinStack:

    def __init__(self):
        self._s = [] 

    def push(self, val: int) -> None:
        self._s.append(val)

    def pop(self) -> None:
        self._s.pop()

    def top(self) -> int:
        return self._s[-1]

    def getMin(self) -> int:
        return min(self._s)
