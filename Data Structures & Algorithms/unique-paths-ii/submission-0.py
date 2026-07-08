class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r_max = len(obstacleGrid)
        c_max = len(obstacleGrid[0])
        o = obstacleGrid
        
        prev = [0] * c_max
        prev[-1] = 1
        for r in range(r_max-1, -1, -1):
            curr = [0] * c_max
            for c in range(c_max-1, -1, -1):
                if o[r][c] == 1:
                    curr[c] = 0
                else:
                    if c == c_max-1:
                        curr[c] = prev[c]
                    else:
                        curr[c] = prev[c]+curr[c+1]
            prev = curr
        return curr[0]