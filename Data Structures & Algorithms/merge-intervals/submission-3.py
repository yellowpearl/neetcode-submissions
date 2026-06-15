class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = []
        l_min = None
        l_max = None

        for interval in intervals:
            if l_min is None and l_max is None:
                l_min = interval[0]
                l_max = interval[1]
                continue
            
            if interval[0] <= l_max:
                l_max = max(interval[1], l_max)
            else:
                res.append([l_min, l_max])
                l_min = interval[0]
                l_max = interval[1]
        res.append([l_min, l_max])
        return res
