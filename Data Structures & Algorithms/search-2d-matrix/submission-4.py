class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not (matrix[0][0] <= target <= matrix[-1][-1]):
            return False
        
        m = len(matrix) # 3
        n = len(matrix[0]) # 4

        size = m * n
        # [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
        l = 0
        r = m * n - 1 # 11
        while l <= r:
            mid = (l + r) // 2 # 5
            line = mid // n # 1
            idx = mid % n # 1
            if matrix[line][idx] > target:
                r = mid - 1
            elif matrix[line][idx] < target:
                l = mid + 1
            else:
                return True
        return False


