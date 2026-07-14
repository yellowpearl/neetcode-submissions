import heapq
import platform
class MedianFinder:

    def __init__(self):
        self.s, self.l = [], []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.s, num * -1)
        if self.s and self.l and (-1 * self.s[0] > self.l[0]):
            # длины равны, проверить что макс s < мин l
            val = -1 * heapq.heappop(self.s)
            heapq.heappush(self.l, val)

        if len(self.s) > len(self.l) + 1:
            val = -1 * heapq.heappop(self.s)
            heapq.heappush(self.l, val)
        if len(self.l) > len(self.s) + 1:
            val = heapq.heappop(self.l)
            heapq.heappush(self.s, val * -1)
        

    def findMedian(self) -> float:
        if len(self.s) == len(self.l):
            return (-1 * self.s[0] + self.l[0]) / 2
        elif len(self.s) > len(self.l):
            return -1 * self.s[0]
        else:
            return self.l[0]
        
        