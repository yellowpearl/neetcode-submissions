class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev = [0] * n

        # 3 2 1
        # 6 3 1
        # 
        for r in range(m-1, -1, -1):
            curr = [0] * n
            curr[-1] = 1
            for c in range(n-2, -1, -1):
                curr[c] = prev[c] + curr[c+1]
            prev = curr
        return curr[0]