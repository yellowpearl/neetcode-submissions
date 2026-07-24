class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        # [1, 4, 1, 2, 1, 0, 0]
        # s=[(1, 38), (3, 36), (4, 35)]
        res = [0] * len(temperatures)
        s = []
        for idx, t in enumerate(temperatures):
            while s and s[-1][1] < t:
                    l_idx, l_t = s.pop()
                    res[l_idx] = idx-l_idx
            s.append((idx, t))
        return res