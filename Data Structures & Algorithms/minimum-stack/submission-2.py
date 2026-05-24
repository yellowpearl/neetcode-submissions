class MinStack:

    def __init__(self):
        self._s = [] 
        self._min_s = []

    def push(self, val: int) -> None:
        self._s.append(val)
        if not self._min_s or val <= self._min_s[-1]:
            self._min_s.append(val)

    def pop(self) -> None:
        val = self._s.pop()
        if self._min_s[-1] == val:
            self._min_s.pop()

    def top(self) -> int:
        return self._s[-1]

    def getMin(self) -> int:
        return self._min_s[-1]
