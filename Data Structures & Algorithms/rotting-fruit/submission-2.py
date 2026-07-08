from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit = set()
        fresh = set()
        q = deque()
        max_r = len(grid)
        max_c = len(grid[0])
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh.add((r,c))
        fresh_copy = fresh.copy()
        level = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh.remove((r,c))

                neighbors = [(1, 0),(0, 1),(-1, 0),(0, -1)]
                for dr, dc in neighbors:
                    nr = r + dr
                    nc = c + dc

                    if (
                        min(nr, nc) < 0
                    ) or (
                        nr == max_r
                    ) or (
                        nc == max_c
                    ) or (
                        grid[nr][nc] == 2
                    ) or (
                        grid[nr][nc] == 0
                    ) or (nr, nc) in visit:
                        continue
                    
                    visit.add((nr,nc))
                    q.append((nr,nc))


            level += 1

        if not fresh_copy:
            return 0
        if not fresh:
            return level - 1
        else:
            return -1


