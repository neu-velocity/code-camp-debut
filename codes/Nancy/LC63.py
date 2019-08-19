class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[0 for i in range(n)] for j in range(m)]
        
        for j in range(n):
            if obstacleGrid[0][j] != 1:
                memo[0][j] = 1
            if obstacleGrid[0][j] == 1:
                break
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                memo[i][0] = 1
            if obstacleGrid[i][0] == 1:
                break
                
        for x in range(1, m):
            for y in range(1, n):
                if obstacleGrid[x][y] != 1:
                    memo[x][y] = memo[x - 1][y] + memo[x][y - 1]
        return memo[m-1][n-1]