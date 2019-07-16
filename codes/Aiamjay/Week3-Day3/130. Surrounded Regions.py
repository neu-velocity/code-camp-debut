class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def explore(row_index, col_index):
            if row_index == -1 or row_index == height \
                    or col_index == -1 or col_index == width:
                return
            if board[row_index][col_index] == 'X' or board[row_index][col_index] == '$':
                return
            board[row_index][col_index] = '$'
            explore(row_index - 1, col_index)
            explore(row_index + 1, col_index)
            explore(row_index, col_index - 1)
            explore(row_index, col_index + 1)

        if not board or not board[0]:
            return
        height = len(board)
        width = len(board[0])
        # wjcnote 如果与四条边上的相连接，则不需要改变，除此之外的，都是需要变的
        for row in [0, height - 1]:
            for col in range(width):
                explore(row, col)
        for col in [0, width - 1]:
            for row in range(1, height - 1):
                explore(row, col)

        for row in board:
            for index in range(width):
                if row[index] is 'O':
                    row[index] = 'X'
                if row[index] == '$':
                    row[index] = 'O'

    def test_solution(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        print(self.solve(board))
        # case2
        print("case2")
        board = [
            ["O", "X", "X", "X", "X", "O"],
            ["X", "O", "O", "X", "O", "X"],
            ["X", "X", "O", "X", "X", "O"],
            ["X", "O", "X", "X", "O", "X"],
            ["X", "O", "O", "O", "X", "O"],
            ["X", "O", "X", "O", "O", "X"],
            ["X", "O", "X", "O", "X", "O"]
        ]
        self.solve(board)
        for item in board:
            print(item)
        # case3
        print("case3")
        board = [
            ["X", "X", "O"],
            ["X", "O", "X"],
            ["X", "O", "X"],
            ["X", "O", "X"],
            ["X", "O", "X"]
        ]
        self.solve(board)
        for item in board:
            print(item)

        # case4
        print("case4")
        board = [
            ["X", "X", "X", "X", "X", "O"],
            ["X", "O", "O", "O", "O", "X"],
            ["X", "X", "O", "X", "X", "O"],
            ["X", "X", "O", "X", "X", "X"],
            ["X", "O", "O", "X", "X", "O"],
            ["X", "O", "O", "O", "O", "X"],
            ["X", "X", "X", "X", "X", "O"]
        ]
        self.solve(board)
        for item in board:
            print(item)

        # case5
        print("case5")
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        self.solve(board)
        for item in board:
            print(item)


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
