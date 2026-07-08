from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        q = deque()
        q.append((0, 0))
        visit.add((0, 0))
        if grid[0][0] == 1:
            return -1
        level = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == n-1 and c == n-1:
                    return level

                neighbors = [(1, 1),(1, 0),(0, 1),(-1, -1),(-1, 0),(0, -1),(1, -1),(-1, 1),]
                for dr, dc in neighbors:
                    nr = r + dr
                    nc = c + dc
                    if (
                        min(nr, nc) < 0
                    ) or (
                        nr == n
                    ) or (
                        nc == n
                    ) or (
                        (nr, nc) in visit
                    ) or (
                        grid[nr][nc] == 1
                    ):
                        continue

                    q.append((r+dr, c+dc))
                    visit.add((r+dr, c+dc))
            level += 1
        return -1



