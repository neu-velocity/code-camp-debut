class Solution:
    """
    recursively dfs move forward in 4 directions to see how far we can get, also mark True for the furthest place
    we can get
    """
    def dfs(self, matrix, x, y, visited, prev):
        #when to stop searching
        m = len(matrix)
        n = len(matrix[0])
        if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < prev:
            return
        
        visited[x][y] = True
        self.dfs(matrix, x + 1, y, visited, matrix[x][y])
        self.dfs(matrix, x - 1, y, visited, matrix[x][y])
        self.dfs(matrix, x, y + 1, visited, matrix[x][y])
        self.dfs(matrix, x, y - 1, visited, matrix[x][y])
        
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0:
            return []
        #create pacific and atlantic visited matrix to record the dfs path
        row = len(matrix)
        col = len(matrix[0])
        p = [[False for y in range(col)] for x in range(row)] 
        a = [[False for y in range(col)] for x in range(row)] 
        
        #perform dfs on each starting points: points at the top:pacific and points at the bottom:atlantic
        for y in range(col):
            self.dfs(matrix, 0, y, p, matrix[0][y])
            self.dfs(matrix, row - 1, y, a, matrix[row - 1][y])
        
        #perform dfs on each starting points: points on the left edge: pacific and points on the right edge: atlantic
        for x in range(row):
            self.dfs(matrix, x, 0, p, matrix[x][0])
            self.dfs(matrix, x, col - 1, a, matrix[x][col - 1])
        res = []
        for i in range(row):
            for j in range(col):
                if p[i][j] and a[i][j]:#if both p and a visted are True, position[i,j] can flow to both ocean
                    res.append([i, j])
        return res