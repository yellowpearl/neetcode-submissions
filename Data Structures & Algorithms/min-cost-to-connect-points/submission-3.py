import heapq

from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        x1, y1 = points[0]
        h = []
        for p in points:
            x2, y2 = p
            heapq.heappush(h, (abs(x2-x1)+abs(y2-y1), (x1, y1), (x2, y2)))
        
        visit = set()
        visit.add(tuple(points[0]))
        res = 0
        while h:
            val, p1, p2 = heapq.heappop(h)
            if p2 in visit:
                continue
            
            res += val
            visit.add(p2)
            for p in points:
                if tuple(p) not in visit:
                    x1, y1 = p2
                    x2, y2 = p
                    heapq.heappush(h, (abs(x2-x1)+abs(y2-y1), (x1, y1), (x2, y2)))

        
        return res


        
        