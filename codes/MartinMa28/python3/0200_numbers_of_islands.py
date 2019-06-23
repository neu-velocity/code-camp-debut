class Solution:
    def __init__(self):
        self.grid = [[]]
        self.directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def _valid_position(self, row_i, col_i):
            return row_i >= 0 and row_i < len(self.grid) and col_i >= 0 and col_i < len(self.grid[0])

    def _dfs(self, row_ind, col_ind) -> None:
        stack = []
        # top, down, left, right
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        # mark visited position as '0'
        self.grid[row_ind][col_ind] = '0'
        stack.append((row_ind, col_ind))

        while len(stack) > 0:
            row_ind, col_ind = stack.pop()

            for d in directions:
                new_row_ind = row_ind + d[0]
                new_col_ind = col_ind + d[1]

                if self._valid_position(new_row_ind, new_col_ind) and \
                     self.grid[new_row_ind][new_col_ind] == '1':
                    stack.append((new_row_ind, new_col_ind))
                    self.grid[new_row_ind][new_col_ind] = '0'
                else:
                    continue
        

    def _recursive_dfs(self, row_ind, col_ind) -> None:
        if self._valid_position(row_ind, col_ind) and self.grid[row_ind][col_ind] == '1':
            self.grid[row_ind][col_ind] = '0'
            for d in self.directions:
                new_row_ind = row_ind + d[0]
                new_col_ind = col_ind + d[1]
                self._recursive_dfs(new_row_ind, new_col_ind)
        else:
            return

    def numIslands(self, grid: list) -> int:
        if grid == [[]] or grid == [] or grid is None:
            return 0

        self.grid = grid
        m = len(self.grid)
        n = len(self.grid[0])
        islands_num = 0

        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == '1':
                    self._recursive_dfs(i, j)
                    islands_num += 1
        
        return islands_num