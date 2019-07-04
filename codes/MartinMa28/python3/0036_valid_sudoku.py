class Solution:
    @staticmethod
    def no_reps_1_to_9(collection: list) -> bool:
        return True if len(set(collection)) == len(collection) else False

    def isValidSudoku(self, board: list) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            row_nums = list(filter(lambda x: x != '.', board[i]))
            if not Solution.no_reps_1_to_9(row_nums):
                return False

        for j in range(n):
            col = [row[j] for row in board]
            col_nums = list(filter(lambda x: x != '.', col))
            if not Solution.no_reps_1_to_9(col_nums):
                return False

        for box_i in range(0, 9, 3):
            for box_j in range(0, 9, 3):
                box = [board[i][j] for i in range(box_i, box_i + 3) for j in range(box_j, box_j + 3)]
                box_nums = list(filter(lambda x: x != '.', box))
                if not Solution.no_reps_1_to_9(box_nums):
                    return False

        return True


if __name__ == "__main__":
    solu = Solution()
    board = [
                ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ]
    print(solu.isValidSudoku(board))