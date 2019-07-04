class Solution:
    @staticmethod
    def valid_sudoku(board: list, row_i: int, col_i: int) -> bool:
        for j in range(len(board[0])):
            if j == col_i:
                continue
            else:
                if board[row_i][j] == board[row_i][col_i]:
                    return False
        
        for i in range(len(board)):
            if i == row_i:
                continue
            else:
                if board[i][col_i] == board[row_i][col_i]:
                    return False
        
        box_row = 3 * (row_i // 3)
        box_col = 3 * (col_i // 3)

        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if i == row_i and j == col_i:
                    continue
                else:
                    if board[i][j] == board[row_i][col_i]:
                        return False

        return True

    
    @staticmethod
    def recursive_solve(board: list, start_row=0) -> bool:
        for i in range(start_row, 9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                
                for num in range(1, 10):
                    board[i][j] = str(num)
                    if Solution.valid_sudoku(board, i, j) and Solution.recursive_solve(board, i):
                        return True
                    
                board[i][j] = '.'
                return False
        
        return True
                    


    def solveSudoku(self, board: list) -> None:
        Solution.recursive_solve(board)


if __name__ == "__main__":
    solu = Solution()

    sudoku = [
                [".",".","7",".",".","6","2",".","."],
                [".",".","4",".","1",".","6","8","."],
                [".",".","2",".",".","9",".","3","7"],
                [".","7","6",".","9",".",".","4","."],
                [".","4","9",".",".",".",".","2","."],
                ["3",".",".",".",".","4",".",".","."],
                [".","2","3",".",".",".","8","6","."],
                ["1",".",".",".",".",".",".",".","."],
                [".",".","8",".",".","3",".","7","."]
            ]
    solu.solveSudoku(sudoku)
    for row in sudoku:
        print(row)