class Solution:
    def __init__(self):
        self.board = [[]]
        # up, down, left, right
        self.directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.dfs_results = {}

    def _valid_position(self, row, col):
        return row >= 0 and row < len(self.board) and col >= 0 and col < len(self.board[0])

    def _dfs(self, row_i, col_i) -> None:
        if self.board[row_i][col_i] == 'O':
            self.board[row_i][col_i] = 'N'
        
            for d in self.directions:
                new_row_i = row_i + d[0]
                new_col_i = col_i + d[1]

                if self._valid_position(new_row_i, new_col_i):
                    self._dfs(new_row_i, new_col_i)
        

    def solve(self, board: list) -> None:
        if board == [] or board == [[]] or board is None:
            return
        
        self.board = board
        m = len(board)
        n = len(board[0])

        for i in range(m):
            self._dfs(i, 0)
            self._dfs(i, n - 1)

        for j in range(n):
            self._dfs(0, j)
            self._dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                elif self.board[i][j] == 'N':
                    self.board[i][j] = 'O'
    


if __name__ == "__main__":
    solu = Solution()
    test = [["X","X","X","X","O","X"],["O","X","X","O","O","X"],["X","O","X","O","O","O"],["X","O","O","O","X","O"],["O","O","X","X","O","X"],["X","O","X","O","X","X"]]
    solu.solve(test)
    print(test)