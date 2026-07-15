import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h: list[tuple[int, int, int]] = [(grid[0][0], 0, 0)]
        t = 0

        visited = set()
        find = len(grid) - 1, len(grid) - 1
        while find not in visited:
            val, r, c = heapq.heappop(h)
            visited.add((r, c))
            t = max(t, val)

            neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in neighbors:
                nr = r + dr
                nc = c + dc
                if min(nr, nc) < 0 or nr == len(grid) or nc == len(grid) or (nr, nc) in visited:
                    continue
                else:
                    heapq.heappush(h, (grid[nr][nc], nr, nc))
        return t