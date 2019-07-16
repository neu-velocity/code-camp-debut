class Solution:
    def __init__(self):
        self.pacific_reachable = []
        self.atlantic_reachable = []
        self.matrix = [[]]
        self.visited = []
        self.directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def _valid_position(self, row, col):
        return row >= 0 and row < len(self.matrix) and col >= 0 and col < len(self.matrix[0])

    def _dfs(self, row_i, col_i, ocean='pacific') -> None:
        self.visited.append([row_i, col_i])
        if ocean == 'pacific':
            self.pacific_reachable.append([row_i, col_i])
        else:
            self.atlantic_reachable.append([row_i, col_i])

        for d in self.directions:
            new_row_i = row_i + d[0]
            new_col_i = col_i + d[1]

            if self._valid_position(new_row_i, new_col_i) and \
                [new_row_i, new_col_i] not in self.visited and \
                self.matrix[row_i][col_i] <= self.matrix[new_row_i][new_col_i]:
                self._dfs(new_row_i, new_col_i, ocean=ocean)


    def pacificAtlantic(self, matrix: list) -> list:
        if matrix == [] or matrix == [[]] or matrix is None:
            return []

        self.matrix = matrix
        m = len(self.matrix)
        n = len(self.matrix[0])

        # do pacific
        self._dfs(0, 0)
        for i in range(1, m):
            if [i, 0] not in self.visited:
                self._dfs(i, 0)
        
        for j in range(1, n):
            if [0, j] not in self.visited:
                self._dfs(0, j)
        
        self.visited = []
        # then do atlantic
        self._dfs(m - 1, n - 1, ocean='atlantic')
        for i in range(0, m - 1):
            if [i, n - 1] not in self.visited:
                self._dfs(i, n - 1, ocean='atlantic')

        for j in range(0, n - 1):
            if [m - 1, j] not in self.visited:
                self._dfs(m - 1, j, ocean='atlantic')

        both_reachable = []
        for p_coor in self.pacific_reachable:
            if p_coor in self.atlantic_reachable:
                both_reachable.append(p_coor)

        return both_reachable


if __name__ == "__main__":
    solu = Solution()
    tc = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(solu.pacificAtlantic(tc))
    