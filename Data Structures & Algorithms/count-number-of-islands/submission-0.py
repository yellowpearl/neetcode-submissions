class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        checked = set()
        def check(i, j) -> bool | None:
            if (i, j) in checked:
                return None
            try:
                val = grid[i][j]
                checked.add((i, j))
                if val == "0":
                    return False
                elif val == "1":
                    check(i, j+1)
                    check(i, j-1)
                    check(i+1, j)
                    check(i-1, j)
                    return True
            except IndexError:
                return False
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in checked and check(i, j):
                    res += 1
        return res