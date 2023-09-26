"""
Answer:
"""
from collections import Counter
class Solution:
    def isValidSudoku(self, board):
        def isValid(list) :
            data = Counter(list).most_common(2)
            if data[0][0] == '.':
                data = data[1:]
            elif data[1][0] == '.':
                data = data[:1]
            if data:
                return data[0][1] == 1
            else:
                return True

        for i in range(9):
            if not isValid(board[i]) or not isValid([board[j][i] for j in range(9)]):
                return False
        for i in range(3):
            for j in range(3):
                if not isValid([board[m][n] for m in range(3*i, 3*i+3) for n in range(3*j, 3*j+3)]):
                    return False
        return True

"""
Tests:
"""
solution = Solution()
print(solution.isValidSudoku([[".","8","7","6","5","4","3","2","1"],
                               ["2",".",".",".",".",".",".",".","."],
                               ["3",".",".",".",".",".",".",".","."],
                               ["4",".",".",".",".",".",".",".","."],
                               ["5",".",".",".",".",".",".",".","."],
                               ["6",".",".",".",".",".",".",".","."],
                               ["7",".",".",".",".",".",".",".","."],
                               ["8",".",".",".",".",".",".",".","."],
                               ["9",".",".",".",".",".",".",".","."]]))

print(solution.isValidSudoku([[".",".",".",".",".",".",".",".","."],
                                 [".","4",".","3",".",".",".",".","."],
                                 [".",".",".",".",".","3",".",".","1"],
                                 ["8",".",".",".",".",".",".","2","."],
                                 [".",".","2",".",".",".",".",".","."],
                                 [".","1","5",".",".",".",".",".","."],
                                 [".",".",".",".",".","2",".",".","."],
                                 [".","2",".","9",".",".",".",".","."],
                                 [".",".","4",".",".",".",".",".","."]]))