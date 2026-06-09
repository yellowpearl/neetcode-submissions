from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        for line in board:
            count = Counter(line)
            for s in symbols:
                if s in count and count[s] > 1:
                    return False
        
        for i in range(9):
            count = Counter([l[i] for l in board])
            for s in symbols:
                if s in count and count[s] > 1:
                    return False

        for i in range(3):
            for j in range(3):
                count = Counter(
                    [cell for cell in board[i*3][j*3:j*3+3]] +
                    [cell for cell in board[i*3+1][j*3:j*3+3]] +
                    [cell for cell in board[i*3+2][j*3:j*3+3]]
                )
                for s in symbols:
                    if s in count and count[s] > 1:
                        return False
        return True