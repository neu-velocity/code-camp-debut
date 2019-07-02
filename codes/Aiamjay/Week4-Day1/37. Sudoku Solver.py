# encoding=utf-8


class Solution:
    INDICES = list(range(9))
    INDICES_SET = set([str(num) for num in range(1, 10)])

    def __init__(self):
        self.board = None

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.backtracking(0)
        pass

    def backtracking(self, pos):
        while pos < 81 and self.board[pos // 9][pos % 9] != ".":
            pos += 1
        if pos == 81:
            return True
        row = pos // 9
        col = pos % 9
        allowed = self.bounding_condition(row, col)
        for num in allowed:
            self.board[row][col] = num
            if self.backtracking(pos + 1):
                return True
        self.board[row][col] = "."
        return False

    def bounding_condition(self, row, col):
        # row, column
        not_allowed = set()
        grid_row = row // 3 * 3
        grid_col = col // 3 * 3
        for index in self.INDICES:
            if self.board[row][index] != ".":
                not_allowed.add(self.board[row][index])
            if self.board[index][col] != ".":
                not_allowed.add(self.board[index][col])
            if self.board[grid_row + index // 3][grid_col + index % 3] != ".":
                not_allowed.add(self.board[grid_row + index // 3][grid_col + index % 3])
        return self.INDICES_SET.difference(not_allowed)

    def test_solution(self):
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
        self.solveSudoku(board)
        ans = [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '9'],
        ]
        assert board == ans

        # case 2 hard mode
        board = [
            [".", "9", ".", "2", "7", ".", ".", ".", "."],
            [".", ".", "2", ".", ".", "8", ".", ".", "4"],
            [".", ".", ".", ".", "3", ".", ".", "6", "."],
            [".", "4", ".", ".", ".", ".", ".", ".", "2"],
            ["2", ".", "1", ".", ".", ".", "4", ".", "7"],
            ["6", ".", ".", ".", ".", ".", ".", "1", "."],
            [".", "8", ".", ".", "1", ".", ".", ".", "."],
            ["5", ".", ".", "8", ".", ".", "9", ".", "."],
            [".", ".", ".", ".", "9", "7", ".", "8", "."],
        ]
        self.solveSudoku(board)
        ans = [
            ['4', '9', '6', '2', '7', '5', '1', '3', '8'],
            ['3', '1', '2', '9', '6', '8', '5', '7', '4'],
            ['8', '7', '5', '1', '3', '4', '2', '6', '9'],
            ['7', '4', '8', '3', '5', '1', '6', '9', '2'],
            ['2', '3', '1', '6', '8', '9', '4', '5', '7'],
            ['6', '5', '9', '7', '4', '2', '8', '1', '3'],
            ['9', '8', '3', '4', '1', '6', '7', '2', '5'],
            ['5', '6', '7', '8', '2', '3', '9', '4', '1'],
            ['1', '2', '4', '5', '9', '7', '3', '8', '6'],
        ]
        assert board == ans


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
    pass
