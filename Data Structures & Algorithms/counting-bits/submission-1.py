class Solution:
    def countBits(self, n: int) -> List[int]:
        # 100
        cache = {}
        res = []
        for i in range(n+1):
            c = 0
            n_c = i
            while n_c > 0:
                if n_c in cache:
                    c += cache[n_c]
                    break
                if n_c & 1 == 1:
                    c += 1
                n_c = n_c >> 1
            res.append(c)
            cache[i] = c
        return res