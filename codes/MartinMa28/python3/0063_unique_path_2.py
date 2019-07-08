class Solution:
    def uniquePathWithObstacles(self, obstacleGrid: list) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 0:
            obstacleGrid[0][0] = 1
        else:
            return 0

        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                obstacleGrid[0][j] = obstacleGrid[0][j - 1]
            else:
                obstacleGrid[0][j] = 0
        
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]
            else:
                obstacleGrid[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0
        
        return obstacleGrid[m - 1][n - 1]


if __name__ == "__main__":
    solu = Solution()
    print(solu.uniquePathWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))