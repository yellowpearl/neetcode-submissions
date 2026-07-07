class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visit = set()
        # [[1,1,1],[1,2,0],[1,0,1]] 1 1 2, m=3, n=3
        # (1,1) ()
        # 1 1
        # 2 1 - r
        # 0 1
        # 
        #
        #
        def dfs(r, c, c_paint):
            if (
                min(r, c) < 0
            ) or (
                r >= m
            ) or (
                c >= n
            ) or (
                image[r][c] != c_paint
            ) or (
                (r,c) in visit
            ):

                visit.add((r,c))
                return
            
            visit.add((r,c))
            image[r][c] = color
            dfs(r+1, c, c_paint)
            dfs(r-1, c, c_paint)
            dfs(r, c+1, c_paint)
            dfs(r, c-1, c_paint)
        dfs(sr, sc, image[sr][sc])
        return image