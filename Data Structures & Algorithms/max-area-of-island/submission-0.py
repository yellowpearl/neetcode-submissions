class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        area = 0
        max_r = len(grid)
        max_c = len(grid[0])

        def dfs(r, c) -> int:
            if (
                min(r,c) < 0
            ) or (
                r == max_r
            ) or (
                c == max_c
            ) or (
                (r,c) in visit
            ) or (
                grid[r][c] == 0
            ):
                return 0
            
            visit.add((r, c))
            count = 1
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)
            return count
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                area = max(area, dfs(r, c))
        return area