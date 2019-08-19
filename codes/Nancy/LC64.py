class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = grid.copy()
        
        for j in range(1, n):
            memo[0][j] += memo[0][j - 1]
        
        for i in range(1, m):
            memo[i][0] += memo[i - 1][0]
        
        for x in range(1, m):
            for y in range(1, n):
                memo[x][y] += min(memo[x - 1][y], memo[x][y - 1])
        print(memo)
        return memo[m-1][n-1]