class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not (matrix[0][0] <= target <= matrix[-1][-1]):
            return False
        
        l = 0
        r = len(matrix) - 1

        # [1,3,5,7]
        # [10,11,16,20]
        # [23,30,34,60]

        # 3
        line = None
        while l <= r:
            mid = (l+r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                line = mid
                break
        
        if line is None:
            return False
        
        # 1 2 4 8
        # 10 11 12 13
        # 14 20 30 40
        # 50 60 70 90
        # 91 92 93 94

        # 2

        l = 0
        r = len(matrix[line]) - 1
        while l <= r:
            mid = (l+r) // 2
            if matrix[line][mid] > target:
                r = mid - 1
            elif matrix[line][mid] < target:
                l = mid + 1
            else:
                return True
        return False


