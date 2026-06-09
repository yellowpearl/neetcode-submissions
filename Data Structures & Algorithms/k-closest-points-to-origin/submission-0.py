

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        coord = []
        for idx, p in enumerate(points):
            coord.append((p[0]*p[0] + p[1]*p[1], idx))
        
        coord.sort(key=lambda p: p[0])
        res = []
        i = 0
        while i <= k - 1:
            res.append(points[coord[i][1]])
            i += 1
        return res