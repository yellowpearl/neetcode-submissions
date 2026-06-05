class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix) + 1
        n = len(matrix[0]) + 1

        pref = [[0] * n for _ in range(m)]
        l_no = 1
        for line in matrix:
            n_no = 1
            for num in line:
                pref[l_no][n_no] = pref[l_no][n_no-1] + pref[l_no-1][n_no] - pref[l_no-1][n_no-1] + num
                n_no += 1
            l_no += 1
        
        self.pref = pref

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: # 
        return self.pref[row2+1][col2+1] - self.pref[row1][col2+1] - self.pref[row2+1][col1] + self.pref[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)