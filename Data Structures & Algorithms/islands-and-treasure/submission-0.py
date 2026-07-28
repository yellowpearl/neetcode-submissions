from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        n = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((-1,r,c))
        
        while q:
            lvl, h_r, h_c = q.popleft()
            lvl += 1
            for dr, dc in n:
                nr = h_r + dr
                nc = h_c + dc
                if (
                    min(nr, nc) < 0
                ) or (
                    nr > len(grid) - 1
                ) or (
                    nc > len(grid[0]) - 1
                ) or (
                    grid[nr][nc] < lvl
                ):
                    continue
                q.append((lvl, nr, nc))
            if grid[h_r][h_c] > 0 and grid[h_r][h_c] > lvl:
                grid[h_r][h_c] = lvl
