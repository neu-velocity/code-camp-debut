# encoding = utf-8
from collections import defaultdict


class Solution:
    # wjcnote 可以不用backtracking 直接检查行列格子 就行
    def isValidSudoku(self, board) -> bool:
        # check row
        row_set = set()
        col_set = set()
        grid_set = defaultdict(set)
        for i in range(9):
            row_set.clear()
            col_set.clear()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] not in col_set:
                        col_set.add(board[j][i])
                    else:
                        return False
                if board[i][j] != ".":
                    if board[i][j] not in row_set:
                        row_set.add(board[i][j])
                    else:
                        return False
                    grid_index = i // 3 * 3 + j // 3
                    if board[i][j] not in grid_set[grid_index]:
                        grid_set[grid_index].add(board[i][j])
                    else:
                        return False
        return True

    def test_solution(self):
        # case 1
        print("case 1")
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        # print(self.isValidSudoku(board))

        # case 2
        print("case 2")
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        print(self.isValidSudoku(board))


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
